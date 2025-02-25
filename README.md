# FireEye Smart System
- Hệ thống hỗ trợ nhận diện đám cháy thông qua camera
- Cảnh báo bằng âm thanh và tin nhắn tới các thiết bị kết nối

## Dataset
- Sử dụng dữ liệu được chọn lọc và thực tế

## Model
- Huấn luyện mô hình YOLO (v8s, v10m)
  - yolov8s nhận diện lửa ( ưu tiên cho các thiết bị camera CPU)
  - yolov10m tăng cường độ chính xác khi nhận diện lửa và khói
- Quá trình huấn luyện được theo dõi trên W&B

<details>
  <summary>Demo Videos</summary>

https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/Fire%201_result.mp4

</details>

![Yolov10mVideoInference](https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/Fire%201_result.mp4)

# Reference:
- https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels