import jetson_utils
import cv2

cams = []

def create_camera(csi_port): 
    cams.append(jetson_utils.videoSource("rtsp://192.168.144.108:554/stream=1"))

def get_image_size(camera_id):
	return cams[camera_id].GetWidth(), cams[camera_id].GetHeight()

def get_video(camera_id):
    return cv2.cvtColor(jetson_utils.cudaToNumpy(cams[camera_id].Capture()),cv2.COLOR_RGB2BGR)

def close_cameras():
    for cam in cams:
        cam.Close()    

if __name__ == "__main__":
    create_camera(0)
    
    while True:
        img = get_video(0)
        cv2.imshow("camera", img)
        cv2.waitKey(1)
    
    close_cameras()