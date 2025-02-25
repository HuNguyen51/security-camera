# Theo dõi đối tượng
import cv2
import yaml

from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self):
        with open("configs/model_config.yaml", "r", encoding='utf8') as f:
            config = yaml.safe_load(f)['object_tracking']

        self.tracker_type = config['tracker_type']
        self.max_age = config['max_age']
        self.n_init = config['n_init']

        self.tracker = DeepSort(max_age=self.max_age, n_init=self.n_init)

        self.color = self.get_random_color()

    @staticmethod
    def get_random_color(n=10): 
        import random
        return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(n)]
    
    def track(self, detections, frame, draw_frame=True):
        # Update tracker with the new detections. The tracker returns a list of track objects.
        tracks = self.tracker.update_tracks(detections, frame=frame)
        # Loop through tracked objects and draw bounding boxes with track IDs
        tracking_info = dict()
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            # class_name = track.get_det_class()
            
            # Get the bounding box in [left, top, right, bottom] format
            ltrb = track.to_ltrb()  
            x1, y1, x2, y2 = map(int, ltrb)
            tracking_info[track_id] = [x1, y1, x2, y2]
            # Draw the bounding box and track ID on the frame
            if draw_frame:
                color = self.color[int(track_id) % len(self.color)]
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        return tracking_info
    
    def __str__(self):
        return f"ObjectTracker(tracker_type={self.tracker_type}, max_age={self.max_age}, n_init={self.n_init})"
    

if __name__ == "__main__":
    from object_detector import ObjectDetector
    detector = ObjectDetector()
    tracker = ObjectTracker()

    cap = cv2.VideoCapture('.\\data\\raw\\vehicle.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()

        detections = detector.detect_objects(frame)      
        tracker.track(detections, frame)

        cv2.imshow("Object Tracking", frame)
        
        # Press 'q' to exit the video loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()