# Phát hiện đối tượng
import yaml
import onnxruntime as ort
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, engine="pytorch"): # onnx 1.19.* require cuDNN 9.* and CUDA 12.* 
        with open("configs/model_config.yaml", "r", encoding='utf8') as f:
            config = yaml.safe_load(f)['object_detection']

        self.model_name = config['model_name']
        self.confidence_threshold = config['confidence_threshold']
        self.nms_threshold = config['nms_threshold']

        self.model = YOLO(config['weights_path'][engine])


    def detect_objects(self, image, filter = ['person']):
        results = self.model.predict(image, conf=self.confidence_threshold, iou=self.nms_threshold, save=False)
        detections = []
        for box in results[0].boxes:
            class_id = int(box.cls.cpu().numpy().flatten()[0])
            class_name = self.model.names[class_id]

            if class_name.lower() in filter: # filter class
                coords = box.xyxy.cpu().numpy().flatten()
                x1, y1, x2, y2 = map(int, coords)
                w, h = x2 - x1, y2 - y1

                conf = float(box.conf.cpu().numpy().flatten()[0])

                detections.append(([x1, y1, w, h], conf, class_name))
            
        return detections
    
    def __str__(self):
        return f"ObjectDetector(model_name={self.model_name}, confidence_threshold={self.confidence_threshold}, nms_threshold={self.nms_threshold})"

if __name__ == "__main__":
    import cv2

    detector = ObjectDetector()
    frame = cv2.imread("data/raw/traffic.jpg")
    detections = detector.detect_objects(frame)

    print(detections)
