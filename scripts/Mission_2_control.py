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
        self.objects_start = []
        self.objects_start_dist = 0
        self.objects_start_index = 0
        self.left_index = 400
        self.servo.angle = 0
        self.servo_value = 0
        rospy.Timer(rospy.Duration(1.0/3), self.time_callback)
           
    def lidar_sub(self, msg):
        self.objects = msg.objects_info
        self.objects_start_dist = self.objects[0].start_dist
        self.objects_start_index = self.objects[0].start_idx

        
    def steering(self):
        if self.objects_start_index > self.left_index:
            self.servo_value = -(self.objects_start_index - self.left_index)
            if self.servo_value < -35:
                self.servo_value = -35
            self.servo.angle = self.servo_value
        elif self.objects_start_index < self.left_index:
            self.servo_value = abs(self.objects_start_index - self.left_index)
            if self.servo_value > 35:
                self.servo_value = 35
            self.servo.angle = self.servo_value
        if self.object_num == 0:
            self.servo.angle = 0

    def motor_control(self):
        self.steering()
        if self.servo_value > 35:
            self.servo.angle = 35
        if self.servo_value < -35:
            self.servo.angle = -35

    def time_callback(self, event):
        self.motor_control()
        self.motor.forward(0.9)
        if self.objects_start_dist < 0.09:
            self.motor.forward(0.0)
        if 0.09 < self.objects_start_dist < 0.15:
            self.motor.forward(0.70)
        if self.objects_start_dist > 0.15:
            self.motor.forward(0.85)


if __name__ == "__main__":
    try:
        dl = Driving_lidar()
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass