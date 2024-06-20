# MIT License
# Copyright (c) 2019 JetsonHacks
# See license
# Using an Ethernet camera connected to a NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2

# URL for the IP camera stream
# Replace 'your_camera_ip_address' and 'your_stream_url' with the actual IP address and stream URL of your camera
ethernet_camera_url = "rtsp://192.168.144.108:554/stream=0"

def show_camera():
    # Open the IP camera stream
    cap = cv2.VideoCapture(ethernet_camera_url)

    if cap.isOpened():
        window_handle = cv2.namedWindow("Ethernet Camera", cv2.WINDOW_AUTOSIZE)
        # Window
        while cv2.getWindowProperty("Ethernet Camera", 0) >= 0:
            ret_val, img = cap.read()
            cv2.imshow("Ethernet Camera", img)
            keyCode = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if keyCode == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")

if __name__ == "__main__":
    show_camera()
