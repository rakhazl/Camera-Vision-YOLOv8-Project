import cv2
from flask import Flask, Response, render_template
import threading

app = Flask(__name__)

camera0 = cv2.VideoCapture("C:\Camera Roll\WIN_20240206_13_11_31_Pro.mp4")
camera1 = cv2.VideoCapture("C:\Camera Roll\WIN_20240206_10_19_49_Pro.mp4")

def generate_frames0():
    while True:
        success0, frame0 = camera0.read()
        if not success0:
            break
        ret0, buffer0 = cv2.imencode('.jpg', frame0)
        frame_encoded0 = buffer0.tobytes()
        yield (b'--frame0\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_encoded0 + b'\r\n\r\n')

def generate_frames1():
    while True:
        success1, frame1 = camera1.read()
        if not success1:
            break
        ret1, buffer1 = cv2.imencode('.jpg', frame1)
        frame_encoded1 = buffer1.tobytes()
        yield (b'--frame1\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_encoded1 + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed0')
def video_feed0():
    return Response(generate_frames0(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(generate_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    while True:
            generate_frames0()
            generate_frames1()