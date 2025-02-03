from gpiozero import OutputDevice, PWMOutputDevice
from time import sleep

# GPIO pin configuration
MOTOR1_ENA = PWMOutputDevice(25)  # Enable pin for Motor 1
MOTOR1_IN1 = OutputDevice(24)     # Input 1 for Motor 1
MOTOR1_IN2 = OutputDevice(23)     # Input 2 for Motor 1
MOTOR2_ENB = PWMOutputDevice(17)  # Enable pin for Motor 2
MOTOR2_IN3 = OutputDevice(27)     # Input 3 for Motor 2
MOTOR2_IN4 = OutputDevice(22)     # Input 4 for Motor 2

# Control parameters
MAX_DUTY_CYCLE = 0.5
STABILIZATION_DELAY = 0.05  # Longer delay for pin stabilization

def safe_motor_sequence(enable_pin, in1_pin, in2_pin, forward=True):
    """Safe sequence for motor control with enhanced stabilization"""
    # Start with everything off and wait for settling
    enable_pin.value = 0
    in1_pin.off()
    in2_pin.off()
    sleep(STABILIZATION_DELAY)
    
    if forward:
        # Forward: Set pins before enabling
        in1_pin.on()
        sleep(0.01)
        in2_pin.off()
        sleep(0.01)
        # Now enable motor
        enable_pin.value = MAX_DUTY_CYCLE
    else:
        # Backward: Different sequence for stability
        # First set the primary pin
        in2_pin.on()
        sleep(STABILIZATION_DELAY)
        # Then set the secondary pin
        in1_pin.off()
        sleep(0.01)
        # Now enable motor with a gradual ramp
        for duty in range(0, int(MAX_DUTY_CYCLE * 100), 10):
            enable_pin.value = duty/100
            sleep(0.01)

def motor1_forward():
    print("Motor 1 Forward")
    safe_motor_sequence(MOTOR1_ENA, MOTOR1_IN1, MOTOR1_IN2, forward=True)

def motor1_backward():
    print("Motor 1 Backward")
    safe_motor_sequence(MOTOR1_ENA, MOTOR1_IN1, MOTOR1_IN2, forward=False)

def motor2_forward():
    print("Motor 2 Forward")
    safe_motor_sequence(MOTOR2_ENB, MOTOR2_IN3, MOTOR2_IN4, forward=True)

def motor2_backward():
    print("Motor 2 Backward")
    safe_motor_sequence(MOTOR2_ENB, MOTOR2_IN3, MOTOR2_IN4, forward=False)

def stop_all_motors():
    print("Stopping all motors")
    # Gradually decrease power first
    for duty in range(int(MAX_DUTY_CYCLE * 100), -1, -10):
        MOTOR1_ENA.value = duty/100
        MOTOR2_ENB.value = duty/100
        sleep(0.01)
    
    # Then set all control pins LOW
    for pin in [MOTOR1_IN1, MOTOR1_IN2, MOTOR2_IN3, MOTOR2_IN4]:
        pin.off()
    sleep(STABILIZATION_DELAY)

def cleanup():
    print("Cleaning up GPIO")
    stop_all_motors()
    # gpiozero handles cleanup automatically

# Initialize everything to safe state
stop_all_motors() 