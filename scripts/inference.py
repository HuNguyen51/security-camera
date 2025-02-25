# Chạy dự đoán trên video
import cv2
import os
import yaml
import time

from src.utils.face_utils import get_face_image

from src.detection.object_detector import ObjectDetector
from src.detection.tracker import ObjectTracker

from src.detection.face_detector import FaceDetector
from src.recognition.face_recognizer import FaceRecognizer

from src.alert.alert_manager import AlertTypes

from scripts.alert_system import roi_check, alert

object_detector = ObjectDetector()
object_tracker = ObjectTracker()
face_detector = FaceDetector()
face_recognizer = FaceRecognizer()

with open("configs/config.yaml", "r", encoding='utf8') as f:
    config = yaml.safe_load(f)
valid_names = os.listdir(config['output_paths']['database'])

def detect(frame, tracking_data: dict):
    clean_frame = frame.copy()
    # theo dõi đối tượng
    people_detections = object_detector.detect_objects(frame, filter=['person'])
    tracking_result = object_tracker.track(people_detections, frame)
    # các đối tượng trong vùng cấm
    obj_in_roi = []

    # tìm được từng đối tượng là person
    for tracking_id, bounding_box in tracking_result.items():
        if tracking_id not in tracking_data.keys():
            tracking_data[tracking_id] = {'time': time.time(), 'im_path': [], 'alert': False}
        # lấy box
        x1, y1, x2, y2 = bounding_box
        person_img = clean_frame[y1:y2, x1:x2]

        # phát hiện xâm nhập
        if roi_check(frame, [(x1+x2)//2, (y1+y2)//2], draw=True): # nếu có trong vùng 
            obj_in_roi.append(tracking_id)
            if not tracking_data[tracking_id]['alert']: # và chưa thông báo
                alert(AlertTypes.INFO, f'Đối tượng {tracking_id} vào vùng cảnh báo')
                tracking_data[tracking_id]['alert'] = True

        # phát hiện khuôn mặt
        have_face, faces = face_detector.detect_faces(person_img)
        if have_face:
            face_imgs = get_face_image(person_img, faces)
            names = face_recognizer.recognize_faces(face_imgs)
            if names[0][0]:
                print(names[0][0])
            else:
                if (time.time() - tracking_data[tracking_id]['time'] > config['existed_time']) \
                                or (tracking_data[tracking_id]['im_path'] == []):
                    
                    folder = f"{config['output_paths']['alerts']}/{tracking_id}"
                    os.makedirs(folder, exist_ok=True)

                    fname = f"{folder}/{time.strftime('%Y-%m-%d_%H-%M-%S')}.jpg" 
                    cv2.imwrite(fname, person_img)

                    tracking_data[tracking_id]['time'] = time.time()
                    tracking_data[tracking_id]['im_path'].append(fname)

    # xóa dữ liệu của các đối tượng đã đi khỏi khung hình (có thể thêm thời gian biến mất thay vì mất là mất ngay)
    deleted_list = []
    for tracking_id in tracking_data.keys():
        if tracking_id not in obj_in_roi:
            tracking_data[tracking_id]['alert'] = False

        if tracking_id not in tracking_result.keys():
            deleted_list.append(tracking_id)

    for tracking_id in deleted_list:
        tracking_data.pop(tracking_id)

    return tracking_data
