from scripts.inference import detect
import cv2

def run(source):
    cap = cv2.VideoCapture(source)
    prev_time = cv2.getTickCount()
    tracking_data = dict()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Main function
        tracking_data = detect(frame, tracking_data)


        # Tính toán FPS
        curr_time = cv2.getTickCount()
        time_elapsed = (curr_time - prev_time) / cv2.getTickFrequency()
        fps = 1 / time_elapsed
        prev_time = curr_time
        # Hiển thị FPS
        cv2.putText(frame, f'FPS: {int(fps)}', (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(f'{source}', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    source = './data/videos/cashier.mp4'
    run(source)

    