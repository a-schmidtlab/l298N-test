import RPi.GPIO as GPIO
import time

def test_gpio():
    try:
        # Set up GPIO using BCM numbering
        GPIO.setmode(GPIO.BCM)
        
        # Set up a single pin for testing
        test_pin = 18
        GPIO.setup(test_pin, GPIO.OUT)
        
        print(f"Testing GPIO pin {test_pin}")
        
        # Blink LED or test output
        for _ in range(3):
            GPIO.output(test_pin, GPIO.HIGH)
            print("Pin HIGH")
            time.sleep(1)
            GPIO.output(test_pin, GPIO.LOW)
            print("Pin LOW")
            time.sleep(1)
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        GPIO.cleanup()
        print("GPIO cleanup completed")

if __name__ == "__main__":
    print("Starting GPIO test...")
    test_gpio() 