# Phát hiện khuôn mặt
import yaml
from facenet_pytorch import MTCNN 

class FaceDetector:
    def __init__(self):
        with open("configs/model_config.yaml", "r", encoding='utf8') as f:
            config = yaml.safe_load(f)['face_detection']

        self.model_name = config['model_name']
        self.detection_threshold = config['detection_threshold']

        self.model = MTCNN(image_size=config['image_size'], margin=config['margin'])

    def detect_faces(self, image):
        # input: full image
        # outputs: (tọa độ khuôn mặt, tọa độ mắt)
        try:
            faces = self.model.detect(image, landmarks=True)
        except:
            return False, 'detect error'
        
        if faces[0] is None:
            return False, 'model dont see person face'
        
        faces_boxes = []
        for face, confidence, landmark in zip(faces[0], faces[1], faces[2]):
            if confidence > self.detection_threshold:
                landmark = landmark.astype(int)
                face = face.astype(int)
                face[face < 0] = 0
                faces_boxes.append({'box': face, 'eyes': [landmark[0], landmark[1]]})
        if faces_boxes == []:
            return False, 'detection confidence is too low'
        
        return True, faces_boxes
    
    def __str__(self):
        return f"FaceDetector(model_name={self.model_name}, detection_threshold={self.detection_threshold})"
    

    

    