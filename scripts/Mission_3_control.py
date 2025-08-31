import rospy
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from gpiozero import Motor
from jun_msgs.msg import objects, object_info

class Driving_lidar():
    def __init__(self):
        rospy.init_node("driving_lidar")

        rospy.Subscriber("/scan_objects", objects, self.lidar_sub)

        self.motor = Motor(forward=13, backward=19)
        factory = PiGPIOFactory()
        self.servo = AngularServo(12, pin_factory=factory)

        self.add = 90
        self.index_half = 859 // 2
        self.left_objects = []
        self.left_dist = []
        self.right_objects = []
        self.right_dist = []
        self.servo.angle = 0
        self.servo_value = 0

        rospy.Timer(rospy.Duration(1.0/5), self.time_callback)
           
    def lidar_sub(self, msg):
        self.objects = msg.objects_info

    def separate(self):
        if self.object_num:
            self.left_objects.append(self.objects[-1])
            self.right_objects.append(self.objects[0])
            for l_obj in self.left_objects:
                if l_obj.start_idx > self.index_half:
                    self.left_dist.append(l_obj.end_dist)
            for r_obj in self.right_objects:
                if r_obj.start_idx < self.index_half:
                    self.right_dist.append(r_obj.start_dist)


    def steering(self):
        self.separate()
        if self.left_dist[-1] > self.right_dist[-1]:
            self.servo_value = -((self.left_dist[-1] - self.right_dist[-1]) * self.add)
            if self.servo_value < -35:
                self.servo.angle = -35
            self.servo.angle = self.servo_value

        if self.left_dist[-1] < self.right_dist[-1]:
            self.servo_value = ((self.right_dist[-1] - self.left_dist[-1]) * self.add)
            if self.servo_value > 35:
                self.servo.angle = 35
            self.servo.angle = self.servo_value



    def time_callback(self, event):
        self.steering()
        self.motor.forward(0.7)
        self.left_dist = []
        self.right_dist = []
           
  

if __name__ == "__main__":
    try:
        dl = Driving_lidar()
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass