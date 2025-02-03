from gpiozero import LED
from time import sleep

def test_gpio():
    try:
        # Create an LED object using GPIO18
        led = LED(18)
        
        print("Testing GPIO pin 18")
        
        # Blink LED
        for _ in range(3):
            led.on()
            print("Pin ON")
            sleep(1)
            led.off()
            print("Pin OFF")
            sleep(1)
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    print("Starting GPIO test with gpiozero...")
    test_gpio() 