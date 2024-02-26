from ultralytics import YOLO
from flask import Flask, render_template
from ultralytics.utils.plotting import Annotator, colors
import cv2
import os
import threading
import datetime
import pytz


app = Flask(__name__)

model = YOLO("result_training") #file "best.pt" or path your file best.pt
camera0 = cv2.VideoCapture("C:\Camera Roll\(3. Left Video - Fortuner 2.mp4")
camera1 = cv2.VideoCapture("C:\Camera Roll\(4. Right Video - Fortuner 2.mp4")

# Folder for saving capture
capture_folder = "C:\clip-roof-toso\capture"

capture_count = 1

# Variable to mark whether the object has exceeded the coordinate limits or not
object_passed_boundary0 = False
object_passed_boundary1 = False
# Function to ensure capturing occurs only once
boundary2_crossed0 = False
boundary2_crossed1 = False
# Coordinate limits defined for camera 0
y_min_boundary1 = 553
y_max_boundary1 = 621
y_min_boundary2 = 801
y_max_boundary2 = 870

# Coordinate limits defined for camera 1
y_min_boundary3 = 553
y_max_boundary3 = 621
y_min_boundary4 = 801
y_max_boundary4 = 870

def draw_label(frame, model, result):
        for r in result:
                annotator = Annotator(frame, line_width=1)
                boxes = r.boxes
                result = model(camera0, camera1)
                for box in boxes:
                        b = box.xyxy[0]
                        c = box.cls

                        key = model.names[int(c)]
                        probs = box.conf[0].item()
                        annotator.box_label(b,
                                        model.names[int(c)]+str(round(box.conf[0].item(), 2)),
                                        color=colors(c, True))

                        print(box.xyxy)

# Function to get the current date and time in the desired time zone
def get_current_time():
        # Specify the desired time zone (Western Indonesian Time)
        jakarta_timezone = pytz.timezone('Asia/Jakarta')
        # Retrieve the current time in the Jakarta time zone
        current_time = datetime.datetime.now(jakarta_timezone)
        return current_time

# Function to detect objects and capture if an object exceeds the coordinate limits on camera0
def detect_and_capture0(frame):
        global object_passed_boundary0
        global boundary2_crossed0
        global capture_count

        result = model(frame, verbose=False, conf=0.5, imgsz=640)
        result = model.track(frame, persist=True)
        draw_label(frame, model, result)

        if not object_passed_boundary0:
                for r in result:
                        if len(r.boxes) > 0:
                                for box in r.boxes:
                                        y_min = box.xyxy[0][1]
                                        y_max = box.xyxy[0][3]
                                if y_min >= y_min_boundary1 and y_max <= y_max_boundary1:
                                        current_time = get_current_time().strftime('%d%b_%H.%M')
                                        capture_path = os.path.join(capture_folder, f"cliproof_capture-{capture_count}_{current_time}.jpg")
                                        cv2.imwrite(capture_path, frame)
                                        print("Camera 0 Mendeteksi Objek. Melakukan capture. Melakukan capture.")
                                        object_passed_boundary0 = True
                                        capture_count += 1
                                break
        # Function to re-enable capture functionality after it has been disabled
        elif object_passed_boundary0 and not boundary2_crossed0:
                for r in result:
                        if len(r.boxes) > 0:
                                for box in r.boxes:
                                        y_min = box.xyxy[0][1]
                                        y_max = box.xyxy[0][3]
                                if y_min >= y_min_boundary2 and y_max <= y_max_boundary2:
                                                print("Trigger On. Reset capture.")
                                                print("Fungsi Capture Telah Siap Kembali")
                                                boundary2_crossed0 = True
                                break
        elif object_passed_boundary0 and boundary2_crossed0:
                object_passed_boundary0 = False
                boundary2_crossed0 = False


# Function to detect objects and capture if an object exceeds the coordinate limits on camera1
def detect_and_capture1(frame):
        global object_passed_boundary1
        global boundary2_crossed1
        global capture_count

        result = model(frame, verbose=False, conf=0.5, imgsz=640)
        result = model.track(frame, persist=True)
        draw_label(frame, model, result)

        if not object_passed_boundary1:
                for r in result:
                        if len(r.boxes) > 0:
                                for box in r.boxes:
                                        y_min = box.xyxy[0][1]
                                        y_max = box.xyxy[0][3]
                                if y_min >= y_min_boundary3 and y_max <= y_max_boundary3:
                                        current_time = get_current_time().strftime('%d%b_%H.%M')
                                        capture_path = os.path.join(capture_folder, f"cliproof_capture-{capture_count}_{current_time}.jpg")
                                        cv2.imwrite(capture_path, frame)
                                        print("Camera 1 Mendeteksi Objek. Melakukan capture.")
                                        object_passed_boundary1 = True
                                        capture_count += 1
                                break
        # Function to re-enable capture functionality after it has been disabled
        elif object_passed_boundary1 and not boundary2_crossed1:
                for r in result:
                        if len(r.boxes) > 0:
                                for box in r.boxes:
                                        y_min = box.xyxy[0][1]
                                        y_max = box.xyxy[0][3]
                                if y_min >= y_min_boundary4 and y_max <= y_max_boundary4:
                                        print("Objek berada di antara batas koordinat y4 dan terdeteksi. Reset capture.")
                                        print("Fungsi Capture Telah Siap Kembali")
                                        boundary2_crossed1 = True
                                break
        elif object_passed_boundary1 and boundary2_crossed1:
                object_passed_boundary1 = False
                boundary2_crossed1 = False


# Function to generate frames from camera0
def generate_frames0():
        while True:
                success0, frame0 = camera0.read()
                if not success0:
                        break

                detect_and_capture0(frame0)

                ret, buffer = cv2.imencode('.jpg', frame0)
                frame0 = buffer.tobytes()

# Function to generate frames from camera1
def generate_frames1():
        while True:
                success1, frame1 = camera1.read()
                if not success1:
                        break

                detect_and_capture1(frame1)

                ret, buffer = cv2.imencode('.jpg', frame1)
                frame1 = buffer.tobytes()


if __name__ == '__main__':
        print("File app.py telah berjalan.")
        t1 = threading.Thread(target=generate_frames0)
        t2 = threading.Thread(target=generate_frames1)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()