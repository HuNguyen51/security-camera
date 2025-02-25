# Tiền xử lý dữ liệu
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.detection.face_detector import FaceDetector
from src.utils.face_utils import align_face, resize_face

import yaml

face_detector = FaceDetector()

with open("configs/model_config.yaml", "r", encoding='utf8') as f:
    config = yaml.safe_load(f)['face_recognition']
with open("configs/config.yaml", "r", encoding='utf8') as f:
    ouput_paths = yaml.safe_load(f)['ouput_paths']

size = (config['image_size']['w'], config['image_size']['h'])

# hình ảnh từ raw sẽ được tiền xử lý như xoay và cắt ảnh khuôn mặt rồi đưa vào database
def crop_image(image):
    # input: human image
    # output: their face
    face = face_detector.detect_faces(image)[0]
    
    x1,y1,x2,y2 = face['box']
    eyes = face['eyes']

    image = align_face(image, eyes[0], eyes[1])

    return image[y1:y2, x1:x2]
def process_raw():
    raw_root = ouput_paths['raw']
    database_root = ouput_paths['database']
    names = os.listdir(raw_root)
    
    for name in names:
        filenames = os.listdir(raw_root + name)
        for filename in filenames:
            img = cv2.imread(raw_root + name + '/' + filename)
            img = crop_image(img)

            cv2.imwrite(database_root + name + '/' + filename, img)

def storage_to_database():
    processed_root = ouput_paths['processed']
    database_root = ouput_paths['database']
    names = os.listdir(processed_root)
    
    for name in names:
        filenames = os.listdir(processed_root + name)
        for filename in filenames:
            img = cv2.imread(processed_root + name + '/' + filename)
            img = resize_face(img, size)

            cv2.imwrite(database_root + name + '/' + filename, img)


if __name__ == "__main__":
    import cv2
    # raw -> processed
    process_raw()
    # processed -> database
    storage_to_database()
