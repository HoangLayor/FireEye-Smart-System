# FireEye Smart System
- The system supports fire detection through cameras.
- Alerts are sent via sound and messages to connected devices.

## Dataset 
[DATASET REPO](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels)

$\color{red}{\textsf{Dataset Composition:}}$
  
  a) Frames extracted and annotated from approximately`1200 videos`.
  
  b) Images manually downloaded from the internet.
       
  c)`4312`images sourced from various public datasets.
  
  From a) and b) i collected `22970` images.
  
$\color{red}{\textsf{Repartition of scenes in dataset (22970 in total)}}$

The dataset is hosted on the Roboflow platform and consists of two projects. This dataset is public and can be downloaded and utilized for your own applications if desired. The links to the projects are: [`FireSmokeDataset_part1`](https://universe.roboflow.com/catargiuconstantin/firesmokedataset/dataset/2) and [`FireSmokeDataset_part2`](https://universe.roboflow.com/catargiuconstantin2/firesmokenewdataset/dataset/1).

<details>
  <summary>Dataset details</summary>


`FireSmokeDataset_part1`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/82d91027-216f-4f9c-ada6-41c4431cc51b)

`FireSmokeDataset_part2`
![image](https://github.com/CostiCatargiu/FireSmokeDetection_BestDataset/assets/70476115/adb582b8-6d95-4fc3-9f66-855ca31b4742)

</details>

The distribution of the dataset for Training, Validation, and Testing tasks is illustrated in the figure below.

![image](https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels/assets/70476115/e4bf539d-6cfc-4f45-bdbe-c9bc85480477)


## Model
- Training the YOLO model (v8s, v10m):
  - YOLOv8s prioritizes detection speed for camera devices using CPUs.
  - YOLOv10m prioritizes accuracy in detecting fire and smoke.
- The training process is monitored on W&B.
  - https://api.wandb.ai/links/giahoang481-h-c-vi-n-c-ng-ngh-b-u-ch-nh-vi-n-th-ng/jhq0xx2j

<details>
  <summary>Demo Videos</summary>

https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/video.gif

</details>

![Yolov10mVideoInference](https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/video.gif)

![Image Demo](https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/test_image_1.jpg)

![Image Demo](https://github.com/HoangLayor/FireEye-Smart-System/blob/main/results/v2.0/test_image_2.jpg)

# Reference:
- https://github.com/CostiCatargiu/NEWFireSmokeDataset_YoloModels