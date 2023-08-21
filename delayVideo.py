import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('/home/pi/delayImg/img{counter:03d}.jpg', resize=(1920, 1080)):
        print('Captured %s' % filename)
        time.sleep(180) # 休眠5分钟


# with picamera.PiCamera() as camera:
#     camera.resolution = (1920, 1080)
#     camera.start_preview()
#     #摄像头预热2秒
#     time.sleep(2)
#     camera.capture('/home/pi/delayImg/foo.jpg')
