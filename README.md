# LabelStudio-To-YOLO-Format
This repository provides a solution to the limitation of Label Studio's video annotation format, which does not natively support the YOLO (You Only Look Once) format. Label Studio is a powerful tool for annotating data, but for users working with YOLO-based object detection, the lack of direct YOLO export has been a hurdle.

This project bridges that gap by converting Label Studio annotations into the YOLO format, making it easier to integrate your annotated datasets with YOLO-based training pipelines. With just a few simple steps, you can seamlessly transform your Label Studio annotations into the precise format YOLO expects.

# Logs
11/11/2024: the script to change fps has been released.
11/28/2024: the main script to extract images and labels has been released.

# How to use?
To use this, ensure that you have the necessary libraries installed. 
```angular2html
moviepy           1.0.3
opencv-python     4.10.0.84

```

Next, you’ll need two files: the video file and the annotation file in JSON format. Convert the video using the script provided in the repository to match the FPS with Label Studio. Then, adjust the main’s arguments to specify the required files.
