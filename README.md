# Raspberry Pi DC Motor Control System

## Overview
This project is a web-based control system for bidirectional operation of two DC motors using a Raspberry Pi 5 and ARCELI L298N motor driver. The system allows real-time control through a web interface using keyboard inputs (WASD keys).

## Setup Instructions
1. Ensure you have a Raspberry Pi 5 with Debian OS installed.
2. Connect the ARCELI L298N motor driver to the Raspberry Pi as per the GPIO configuration in `design.md`.
3. Install the required Python packages using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.

## Usage
- Access the web interface through your browser.
- Use the WASD keys to control the motors:
  - W: Motor 1 Forward
  - S: Motor 1 Backward
  - A: Motor 2 Forward
  - D: Motor 2 Backward
- Release any key to stop the corresponding motor. 