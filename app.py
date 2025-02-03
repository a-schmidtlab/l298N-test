from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import motor_control

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('control')
def handle_control(command):
    if command == 'motor1_forward':
        motor_control.motor1_forward()
        emit('status', {'motor1': 'Forward', 'motor2': 'Stopped'})
    elif command == 'motor1_backward':
        motor_control.motor1_backward()
        emit('status', {'motor1': 'Backward', 'motor2': 'Stopped'})
    elif command == 'motor2_forward':
        motor_control.motor2_forward()
        emit('status', {'motor1': 'Stopped', 'motor2': 'Forward'})
    elif command == 'motor2_backward':
        motor_control.motor2_backward()
        emit('status', {'motor1': 'Stopped', 'motor2': 'Backward'})
    elif command == 'stop_all_motors':
        motor_control.stop_all_motors()
        emit('status', {'motor1': 'Stopped', 'motor2': 'Stopped'})

if __name__ == '__main__':
    try:
        socketio.run(app, host='0.0.0.0', port=5000)
    finally:
        motor_control.cleanup() 