# Kiểm tra vùng cấm
import numpy as np
import ujson
import cv2

class RoiChecker:
    def __init__(self):
        self.zones = ujson.load(open('configs/roi_config.json', encoding='utf8'))
        
    def _draw(self, frame, point):
        cv2.polylines(frame, np.array([zone['coordinates'] for zone in self.zones]), True, (0, 0, 255), 1)
        cv2.putText(frame, '.', point, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)

    def is_inside_forbidden_zone(self, frame, point, draw=False):
        flag = False
        if draw:
            self._draw(frame, point)
            
        for zone in self.zones:
            flag = cv2.pointPolygonTest(np.array(zone['coordinates']), point, False) >= 0

        return flag
    
if __name__ == '__main__':
    src = './data/videos/cashier.mp4'
    cap = cv2.VideoCapture(src)
    rc = RoiChecker()

    import random
    import time
    t = time.time()
    point = (0,0)
    while True:
        _, frame = cap.read()
        if time.time() - t > 1:
            point = (random.randint(0, frame.shape[1]), random.randint(0, frame.shape[0]))
            t = time.time()

        print(rc.is_inside_forbidden_zone(point, draw=True))
        
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break