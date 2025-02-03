import motor_control
import time

# Test motor control functions

def test_motor_control():
    print("Testing Motor 1 Forward")
    motor_control.motor1_forward()
    time.sleep(2)
    motor_control.stop_all_motors()
    time.sleep(1)

    print("Testing Motor 1 Backward")
    motor_control.motor1_backward()
    time.sleep(2)
    motor_control.stop_all_motors()
    time.sleep(1)

    print("Testing Motor 2 Forward")
    motor_control.motor2_forward()
    time.sleep(2)
    motor_control.stop_all_motors()
    time.sleep(1)

    print("Testing Motor 2 Backward")
    motor_control.motor2_backward()
    time.sleep(2)
    motor_control.stop_all_motors()
    time.sleep(1)

    print("All tests completed.")

if __name__ == "__main__":
    try:
        test_motor_control()
    finally:
        motor_control.cleanup() 