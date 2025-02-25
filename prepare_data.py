from roboflow import Roboflow
rf = Roboflow(api_key="bfM7naaFPZ6sIb6kY7UB")
project = rf.workspace("catargiuconstantin").project("firesmokedataset")
version = project.version(2)
dataset = version.download("yolov8")
                