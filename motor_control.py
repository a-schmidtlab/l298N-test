import RPi.GPIO as GPIO

# GPIO pin configuration
MOTOR1_ENA = 25
MOTOR1_IN1 = 24
MOTOR1_IN2 = 23
MOTOR2_ENB = 17
MOTOR2_IN3 = 27
MOTOR2_IN4 = 22

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR1_ENA, MOTOR1_IN1, MOTOR1_IN2, MOTOR2_ENB, MOTOR2_IN3, MOTOR2_IN4], GPIO.OUT)

# Initialize PWM
pwm1 = GPIO.PWM(MOTOR1_ENA, 1000)
pwm2 = GPIO.PWM(MOTOR2_ENB, 1000)
pwm1.start(0)
pwm2.start(0)

# Motor control functions
def motor1_forward():
    GPIO.output(MOTOR1_IN1, GPIO.LOW)
    GPIO.output(MOTOR1_IN2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(100)

def motor1_backward():
    GPIO.output(MOTOR1_IN1, GPIO.HIGH)
    GPIO.output(MOTOR1_IN2, GPIO.LOW)
    pwm1.ChangeDutyCycle(100)

def motor2_forward():
    GPIO.output(MOTOR2_IN3, GPIO.LOW)
    GPIO.output(MOTOR2_IN4, GPIO.HIGH)
    pwm2.ChangeDutyCycle(100)

def motor2_backward():
    GPIO.output(MOTOR2_IN3, GPIO.HIGH)
    GPIO.output(MOTOR2_IN4, GPIO.LOW)
    pwm2.ChangeDutyCycle(100)

def stop_all_motors():
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    GPIO.output([MOTOR1_IN1, MOTOR1_IN2, MOTOR2_IN3, MOTOR2_IN4], GPIO.LOW)

# Cleanup GPIO on exit
def cleanup():
    stop_all_motors()
    GPIO.cleanup() 