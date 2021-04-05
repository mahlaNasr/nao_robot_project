#!/usr/bin/python3.8

##########################################################################
# Author: Mahla Nasrollahi
# Last Updated: 28/03/2021
# File Name: take_process_img.py
#
# This script taken a given number of images and process them to see if they
# are clear to be recognised in the image and if they are able to be decoded
############################################################################


# import the necessary packages
from pyzbar import pyzbar
import time, datetime
import pandas as pd
import argparse, os
import numpy as np
import cv2 as cv

# Determine the number of images you want to take in order to be analysed
maxFrames = 1
cpt = 0


decode_result = []
confidence_score = []
image_direc = 'taken_images/'
decoded_img_path = 'decoded_img/'
final_path = 'results/'
crop_dir = 'crop_img/'

try:
    vidStream = cv.VideoCapture(0) # index of your camera
except:
    print ("problem opening input stream")
    sys.exit(1)

while cpt < maxFrames:
    ret, frame = vidStream.read() # read frame and return code.
    if not ret: # if return code is bad, abort.
        sys.exit(0)
    cv.imshow("test window", frame) # show image in window
    cv.imwrite("taken_images/image%i.jpg" %cpt, frame)
    cpt += 1

def analye_img():
    for filename in os.listdir(image_direc):
        # Read the image files in directory specified
        if filename.endswith(".jpg"):
            image_path = str(os.path.join(image_direc, filename))
            # load the input image
            image = cv.imread(image_path)


            # find the barcodes in the image and decode each of the barcodes
            barcodes = pyzbar.decode(image)
            font = cv.FONT_HERSHEY_SIMPLEX

            # if no barcode is detected
            if not barcodes :
                result_txt = "Decoding Failed"
                # get boundary of this text
                textsize = cv.getTextSize(result_txt, font, 1, 2)[0]
                # get coords based on boundary
                textX = (image.shape[1] - textsize[0]) / 2
                textY = (image.shape[0] + textsize[1]) / 2
                cv.putText(image, result_txt, (int(textX), int(textY)), font, 2, (0, 0, 255), 2)

                save_decode = str(os.path.join(decoded_img_path, filename))
                cv.imwrite(save_decode, image)

                cv.destroyAllWindows()
                cv.waitKey(1)

                decode_result.append(result_txt)


            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw the
                # bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

                # the barcode data is a bytes object so if we want to draw it on
                # our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                result_txt = "Decoding Passed"
                cv.putText(image, result_txt, (x, y - 10), font, 1, (0, 255, 0), 1)

                save_decode = str(os.path.join(decoded_img_path, filename))
                cv.imwrite(save_decode, image)

                cv.destroyAllWindows()
                cv.waitKey(1)

                decode_result.append(result_txt)


def conf_score():
    for filename in os.listdir(decoded_img_path):
        if filename.endswith(".jpg"):
            image = str(os.path.join(decoded_img_path, filename))
            # Load an image
            frame = cv.imread(image)

            threshold = 0.6
            maxWidth = 1280; maxHeight = 720
            imgHeight, imgWidth = frame.shape[:2]
            hScale = 1; wScale = 1
            thickness = 1

            if imgHeight > maxHeight:
                hScale = imgHeight / maxHeight
                thickness = 6

            if imgWidth > maxWidth:
                wScale = imgWidth / maxWidth
                thickness = 6

            # Load class names and YOLOv3-tiny model
            classes = open('../qrcode.names').read().strip().split('\n')
            net = cv.dnn.readNetFromDarknet('../qrcode-yolov3-tiny.cfg', '../qrcode-yolov3-tiny.weights')
            net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
            # net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU) # DNN_TARGET_OPENCL DNN_TARGET_CPU DNN_TARGET_CUDA

            start_time = time.monotonic()
            # Convert frame to blob
            blob = cv.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
            elapsed_ms = (time.monotonic() - start_time) * 1000
            # print('blobFromImage in %.1fms' % (elapsed_ms))

            def postprocess(frame, outs):
                frameHeight, frameWidth = frame.shape[:2]

                classIds = []
                confidences = []
                boxes = []

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        classId = np.argmax(scores)
                        confidence = scores[classId]
                        if confidence > threshold:
                            x, y, width, height = detection[:4] * np.array([frameWidth, frameHeight, frameWidth, frameHeight])
                            left = int(x - width / 2)
                            top = int(y - height / 2)
                            classIds.append(classId)
                            confidences.append(float(confidence))
                            boxes.append([left, top, int(width), int(height)])

                indices = cv.dnn.NMSBoxes(boxes, confidences, threshold, threshold - 0.1)

                for i in indices:
                    i = i[0]
                    box = boxes[i]
                    left = box[0]
                    top = box[1]
                    width = box[2]
                    height = box[3]
                    cropped_image = frame[top:top + height, left:left + width]

                    try:
                        # cv.imshow('cropped', cropped_image)
                        crop_img = str(os.path.join(crop_dir, filename))
                        cv.imwrite(crop_img, cropped_image)
                    except:
                        pass

                    # Draw bounding box for objects
                    cv.rectangle(frame, (left, top), (left + width, top + height), (255, 0, 255), thickness)
                    # Draw class name and confidence
                    label = '%s:%.2f' % (classes[classIds[i]], confidences[i])
                    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 1)
                    confidence_score.append(confidences[i])

            # Determine the output layer
            ln = net.getLayerNames()
            ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

            net.setInput(blob)
            start_time = time.monotonic()
            # Compute
            outs = net.forward(ln)
            elapsed_ms = (time.monotonic() - start_time) * 1000
            # print('forward in %.1fms' % (elapsed_ms))

            start_time = time.monotonic()
            postprocess(frame, outs)
            # print(postprocess(frame, outs))
            elapsed_ms = (time.monotonic() - start_time) * 1000
            # print('postprocess in %.1fms' % (elapsed_ms))

            if hScale > wScale:
                frame = cv.resize(frame, (int(imgWidth / hScale), maxHeight))
            elif hScale < wScale:
                frame = cv.resize(frame, (maxWidth, int(imgHeight / wScale)))

            #cv.imshow('QR Detection', frame)
            save_img = str(os.path.join(final_path, filename))
            cv.imwrite(save_img, frame)
            cv.destroyAllWindows()
            cv.waitKey(1)

def main():
    print("[INFO] Scanning images...")
    analye_img()
    conf_score()
    print("[INFO] Finished scanning.")
    print("Date and Time: {}".format(datetime.datetime.now()))

    # Save resutls in excel
    df = pd.DataFrame(columns=['Image number','Confidence Score', 'Decoding Passed'])
    counter=0
    for i, j in zip(confidence_score, decode_result):
        df = df.append({'Image number' : counter, 'Confidence Score': i, 'Decoding Passed':j}, ignore_index=True)
        counter += 1
    writer = pd.ExcelWriter('taken_picture.xlsx')

    df.to_excel(writer, sheet_name='taken_picture', index=False)
    writer.save()

if __name__ == "__main__":
    main()
