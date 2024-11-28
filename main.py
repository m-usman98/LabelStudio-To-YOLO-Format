import argparse
from decimal import Decimal
import cv2
import json
import os

def video_to_images(video_file, json_file, output_img_pth, output_txt_pth):
    directories = [output_img_pth, output_txt_pth]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    load_video = cv2.VideoCapture(video_file)

    if not load_video.isOpened():
        print("Error: Could not open video.")
        exit()

    with open(json_file, 'r') as f:
        load_json = json.load(f)
    labels = load_json[0]

    Object_One = labels['annotations'][0]['result'][0]
    print(f"The number of total frames are {Object_One['value']['framesCount']}.")

    for i in Object_One['value']['sequence']:
        frame_counter = i['frame']
        x = Decimal(i['x'])
        y = Decimal(i['y'])
        width = Decimal(i['width'])
        height = Decimal(i['height'])
        time = (i['time']) * 1000

        x = x / Decimal(100)
        y = y / Decimal(100)
        width = width / Decimal(100)
        height = height / Decimal(100)

        load_video.set(cv2.CAP_PROP_POS_MSEC, time)
        ret, frame = load_video.read()
        if not ret:
            break

        x = int(x * frame.shape[1])
        y = int(y * frame.shape[0])
        xx2 = int(width * frame.shape[1])
        yy2 = int(height * frame.shape[0])

        x1, y1 = x, y
        x2, y2 = x + xx2, y
        x3, y3 = x + xx2, y + yy2
        x4, y4 = x, y + yy2

        string = ("0 " + str(x1 / frame.shape[1]) + " " + str(y1 / frame.shape[0]) + " " + str(
            x2 / frame.shape[1]) + " " + str(y2 / frame.shape[0]) + " " + str(x3 / frame.shape[1]) + " " + str(
            y3 / frame.shape[0]) + " " + str(x4 / frame.shape[1]) + " " + str(y4 / frame.shape[0]) + "\n")

        with open(f'{output_img_pth}/{frame_counter}.txt', 'w') as f:
            f.write(f"{string}")
            f.close()
        cv2.imwrite(f'{output_txt_pth}/{frame_counter}.jpg', frame)

    load_video.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_video', '-i', default= r"", help='Path of the video file.')
    parser.add_argument('--input_json', default=r"", help='Path of the json file.')
    parser.add_argument('--output_image', '-o', default="./output/images",
                        help='Path of the output directory of .jpg files.')
    parser.add_argument('--output_txt', '-o', default="./output/labels",
                        help='Path of the output directory of .txt files.')
    args = parser.parse_args()
    video_to_images(args.input_video, args.input_json, args.output_image, args.output_txt)
