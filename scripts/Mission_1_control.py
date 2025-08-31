import rospy
import time
from jun_msgs.msg import cam_info
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from gpiozero import Motor
from jun_msgs.msg import objects, object_info

class Controller():
    def __init__(self):
        rospy.init_node("controller")
        rospy.Subscriber("/camera_point", cam_info, self.camera_sub)
        rospy.Subscriber("/scan_objects", objects, self.lidar_sub)
        self.motor = Motor(forward=13, backward=19)
        factory = PiGPIOFactory()
        self.servo = AngularServo(12, pin_factory=factory)
        self.middle = 0
        self.cam_point = cam_info()
        self.l_center, self.r_center = 0, 71
        self.lx, self.rx = 0, 71
        self.object_detect_bool = False
        self.objects_start = []
        self.objects_end = []
        self.objects_start_dist = 0
        self.objects_end_dist = 0
        self.servo.angle = self.middle
        self.l_steer, self.r_steer = 0, 0
        self.servo_value = 0
        rospy.Timer(rospy.Duration(1.0/3), self.time_callback)
           
    def lidar_sub(self, msg):
        self.objects = msg.objects_info
        self.object_num = msg.no
        self.objects_start_dist = self.objects[0].start_dist
        self.objects_end_dist = self.objects[0].end_dist

    
    def object_detect(self):
        if self.object_num:
            self.object_detect_bool = True
        else:
            self.object_detect_bool = False

    def camera_sub(self, msg):
        self.cam_point = msg
        self.lx = self.cam_point.lx
        self.rx = self.cam_point.rx
        self.red_stop = msg.red_detect
        self.green_go = msg.green_detect
        self.stopline_stop = msg.stopline_detect
        self.left_sign = msg.left_detect
        
    def steering(self):
        self.l_steer = self.l_center - self.lx
        self.r_steer = self.r_center - self.rx
        self.servo_value_r = (self.middle - self.r_steer)
        self.servo_value_l = (self.middle - self.l_steer)

    def motor_control(self):
        self.steering()
        if self.servo_value > 35:
            self.servo.angle = 35
        if self.servo_value < -35:
            self.servo.angle = -35

        if self.rx < 5 or self.rx > 90:
            self.servo.angle = self.servo_value_l
        else:
            self.servo.angle = self.servo_value_r

    def time_callback(self, event):
        self.object_detect()
        self.motor_control()
        self.motor.forward(1)
        if self.object_detect_bool:
            self.motor.forward(0)
        if self.red_stop:
            self.motor.forward(0)
            time.sleep(3)
        if self.green_go:
            self.motor.forward(1)
        if self.left_sign:
            self.motor.forward(1)
            self.servo.angle = -31
            time.sleep(11)

  

if __name__ == "__main__":
    try:
        ct = Controller()
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass
