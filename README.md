# 🎥 Security Camera  
Hệ thống giám sát video thông minh

Phát hiện & nhận diện khuôn mặt thời gian thực + phát hiện & theo dõi vật thể + cảnh báo thông minh.

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## ✨ Tính năng chính
- Phát hiện khuôn mặt (MTCNN) + nhận diện (FaceNet)
- Phát hiện vật thể (YOLOv5) + theo dõi (DeepSort)
- Cảnh báo thông minh thời gian thực
- Hỗ trợ: webcam, camera IP (RTSP), file video
- Cấu hình qua YAML
- Cơ sở dữ liệu khuôn mặt người quen

## 📦 Yêu cầu
- Python 3.8+
- RAM 8–16 GB (khuyến nghị GPU)
- Thư viện: opencv-python, torch, torchvision, mtcnn, facenet-pytorch, yolov5, deep-sort-realtime, pyyaml

## 📁 Cấu trúc chính
```
security-camera/
├── main.py
├── configs/           # model, detection, tracking, alert
├── src/
│   ├── face_recognition/
│   ├── object_detection/
│   ├── alert_system/
│   └── inference/
├── scripts/           # download_models, preprocess,...
└── data/
    ├── raw/
    ├── processed/
    └── database/      # encodings khuôn mặt
```

## ⚡ Thêm người quen vào database
1. Đặt ảnh vào `data/raw/known_faces/Tên_Người/`
2. Chạy:
```bash
python scripts/preprocess.py --input data/raw/known_faces/ --output data/database/
```

## 🔮 Dự định phát triển trong tương lai

### Gần (v1.1 - v1.3)
- Cải thiện độ chính xác nhận diện khuôn mặt
- Nâng cấp lên YOLO cao hơn
- Cảnh báo qua email, SMS, push notification, webhook

### Trung hạn (v2.0)
- Hỗ trợ triển khai edge (NVIDIA Jetson, camera thông minh)
- Xử lý phân tán, đa luồng

### Dài hạn (v3.0)
- Tối ưu GPU toàn diện (CUDA, FP16)
- Phân tích hành vi, phát hiện bất thường
- Bảng điều khiển trực quan
- Tối ưu mô hình (quantization, distillation)
