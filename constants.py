import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
SPINNER = 2
RMOTOR = 0

# Digital ports
LEFT_BUTTON = 0
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

#Analog ports
BACK_TOPHAT = 0
FRONT_TOPHAT = 5
STARTLIGHT = 2
ET = 3

IS_CLONE = w.digital(CLONE_SWITCH)

# Thresholds
THRESHOLD_GYRO = 200
THRESHOLD_TOPHAT = 2000
THRESHOLD_ET = 1000

# Servos
SERVO_BIN_ARM = 2
SERVO_JOINT = 0
SERVO_BOT_GUY_HITTER = 3


OFFSET_ARM = -57
OFFSET_JOINT = -183
if IS_CLONE:
    OFFSET_ARM = -80
    OFFSET_JOINT = -48

# Servo values
ARM_RAMP_APPROACH = 260 + OFFSET_ARM
ARM_APPROACH = 280 + OFFSET_ARM
ARM_MAX = 2047
ARM_ALL_UP = 1700 + OFFSET_ARM
ARM_TUCKED = 130 + OFFSET_ARM
ARM_SPINNER_TEST = 350 + OFFSET_ARM
ARM_SWING = 580 + OFFSET_ARM
ARM_RAMP_ON = 900 + OFFSET_ARM
ARM_TILT = 480 + OFFSET_ARM
ARM_HIT = 1447 + OFFSET_ARM

JOINT_RAMP_APPROACH = 1205 + OFFSET_JOINT
JOINT_APPROACH = 1175 + OFFSET_JOINT
JOINT_TUCKED = 0 + OFFSET_JOINT
JOINT_HOLD = 625 + OFFSET_JOINT
JOINT_MID = 575 + OFFSET_JOINT
JOINT_ROTATE = 300 + OFFSET_JOINT
JOINT_PARALLEL = 775 + OFFSET_JOINT
JOINT_GROUND = 1025 + OFFSET_JOINT
JOINT_SWING = 950 + OFFSET_JOINT
JOINT_RAMP_ON = 400 + OFFSET_JOINT
JOINT_DELIVER = 1900 + OFFSET_JOINT
JOINT_ARM_TILT = 728 + OFFSET_JOINT

HITTER_IN = 0
HITTER_OUT = 2047
HITTER_ET = 1024

WHEELS_DEPLOYED = 0
WHEELS_UP = 850

LOGFILE = "" # Leave empty
ROBOT_NAME = "Rampy"

HIT_BOTGUY = False
