from face import main
from time import sleep
list = main.face_reco()
if list ==2:
    import servo
    servo.open()
    sleep(2)
    servo.close()
else:
    print("no")