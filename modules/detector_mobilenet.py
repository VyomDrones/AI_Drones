import jetson_inference
import jetson_utils
from jetson_utils import cudaImage, cudaToNumpy
import cv2
import numpy as np

net = None
camera = None

def initialize_detector():
	global net, camera
	net = jetson_inference.detectNet("ssd-mobilenet-v2")
	camera = jetson_utils.videoSource("rtsp://192.168.144.108:554/stream=0")      # '/dev/video0' for V4L2
	print("fakka")

def get_image_size():
	return camera.GetWidth(), camera.GetHeight()

def close_camera():
	camera.Close()

def get_detections():
	person_detections = []
	img = camera.Capture()
	detections = net.Detect(img)

	# Convert the CUDA image to a NumPy array
	frame_np = cudaToNumpy(img)

	for detection in detections:
		if detection.ClassID == 1: #remove unwanted classes
			person_detections.append(detection)
	fps = net.GetNetworkFPS()

	return person_detections, fps, frame_np
    
