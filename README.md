

**Security Camera Project**
==========================

**Tổng quan**
------------

Dự án này là một hệ thống camera an ninh sử dụng công nghệ thị giác máy tính và máy học để phát hiện và nhận dạng khuôn mặt, theo dõi các đối tượng trong khung hình và cảnh báo người dùng về các mối đe dọa an ninh tiềm ẩn.

**Các tính năng**
------------

* Phát hiện và nhận dạng khuôn mặt bằng mô hình học sâu
* Phát hiện và theo dõi đối tượng bằng mô hình học sâu
* Hệ thống cảnh báo thông báo cho người dùng về các mối đe dọa bảo mật tiềm ẩn
* Hỗ trợ đầu vào video từ nhiều nguồn khác nhau

**Requirements**
---------------

* Python 3.x
* OpenCV
* FaceNet (for face recognition)
* MTCNN (for face detection)
* YOLO (for object detection)
* DeepSort (for object tracking)
* YAML (for configuration files)

**Cấu hình**
---------------

Dự án sử dụng các tệp cấu hình YAML để lưu trữ các thiết lập cho mô hình nhận dạng khuôn mặt, mô hình phát hiện đối tượng và hệ thống cảnh báo. Các tệp này nằm trong thư mục `configs`

**Cách dùng**
-----

1. Cài đặt các dependencies cần thiết.
2. Cấu hình mô hình nhận dạng khuôn mặt, mô hình phát hiện đối tượng và hệ thống cảnh báo bằng cách chỉnh sửa các tệp cấu hình YAML.
3. Chạy tập lệnh `main.py` để khởi động hệ thống camera an ninh.

**Scripts**
---------

* `main.py`: Tập lệnh chính chạy hệ thống camera an ninh.
* `inference.py`: Tập lệnh thực hiện phát hiện và theo dõi đối tượng trên đầu vào video.
* `preprocess.py`: Tập lệnh xử lý trước hình ảnh đưa vào database để nhận dạng khuôn mặt.
* `alert_system.py`: Tập lệnh gửi cảnh báo tới người dùng khi phát hiện mối đe dọa bảo mật tiềm ẩn.

**Data**
------

* `data/raw`: Thư mục chứa dữ liệu hình ảnh và video thô.
* `data/processed`: Thư mục chứa dữ liệu hình ảnh đã xử lý trước.
* `data/database`: Thư mục chứa dữ liệu nhận dạng khuôn mặt.

**Future Work**
--------------

Trong khi việc triển khai hệ thống camera an ninh hiện tại cung cấp nền tảng vững chắc cho việc nhận dạng khuôn mặt, phát hiện vật thể và cảnh báo, vẫn có một số lĩnh vực có thể được cải thiện và mở rộng trong tương lai:

* **Improve Face Recognition Accuracy**: Mô hình nhận dạng khuôn mặt hiện tại có thể được cải thiện bằng cách tinh chỉnh nó trên một tập dữ liệu lớn hơn hoặc sử dụng các kỹ thuật tiên tiến hơn như học chuyển giao hoặc cơ chế attention.
* **Enhance Object Detection**: Mô hình phát hiện đối tượng có thể được cải thiện bằng cách sử dụng các kỹ thuật tiên tiến hơn như multi-scale training, data augmentation hoặc sử dụng các mô hình mạnh hơn như Faster R-CNN hoặc RetinaNet.
* **Integrate with Other Sensors**: Hệ thống có thể được tích hợp với các cảm biến khác như cảm biến chuyển động, cảm biến nhiệt độ hoặc cảm biến âm thanh để cung cấp giải pháp an ninh toàn diện hơn.
* **Implement Real-time Alerting**: Hệ thống có thể được sửa đổi để cung cấp cảnh báo thời gian thực cho người dùng qua email, tin nhắn SMS hoặc thông báo trên ứng dụng di động.
* **Explore Edge Deployment**: Hệ thống có thể được khám phá để triển khai trên các thiết bị biên như camera thông minh, chuông cửa thông minh hoặc các thiết bị IoT khác để giảm độ trễ và cải thiện xử lý thời gian thực.
* **Split Thread**: Việc chia hệ thống thành nhiều luồng có thể cải thiện hiệu suất bằng cách cho phép nhiều thành phần khác nhau chạy đồng thời, chẳng hạn như một luồng để xử lý video và thực hiện object tracking và một luồng khác để phát hiện khuôn mặt và chụp ảnh, cảnh báo.
* **Optimize Inference with GPU**: Việc sử dụng Bộ xử lý đồ họa (GPU) có thể tăng tốc đáng kể quá trình suy luận cho các mô hình nhận dạng khuôn mặt và phát hiện vật thể, giúp xử lý dữ liệu video nhanh hơn và hiệu quả hơn.
