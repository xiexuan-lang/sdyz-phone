import pressure
import RPi.GPIO as GPIO
import xuan_DATABASE as xuan
from face import main as face
import wechat_opin
import time
while(1):
    if pressure.buttom1():
        print('buttom1 on')
        id = face.face_reco()
        print('face on ')
        print(id)
        if xuan.get_enroll_state(id):
            print('get_enroll state yes ')
            name = xuan.idtoname(id)
            print("saving isornot:"+str(xuan.savingornot(name)))
            if xuan.savingornot(name):
                print('get ')
                print("right:"+str(xuan.getisornot_name(name)[1]))
                if xuan.getisornot_name(name)[1]:
                    from gpiozero.pins.pigpio import PiGPIOFactory
                    from gpiozero import Servo
                    pigpio_factory = PiGPIOFactory()
                    print("where(get):"+str(xuan.get_IS_data2('test','STATE',str(name))))
                    servo = Servo(xuan.get_IS_data2('test','STATE',str(name)), pin_factory= pigpio_factory)
                    servo.value= -0.6
                    time.sleep(5)
                    servo.value =1
                    GPIO.cleanup()
    
                    name = '''"'{a}'" '''.format(a=name)
                    xuan.del_data2('test','STATE',name)#phoneid
                    wechat_opin.Db_isornotupdata('{name1}','False'.format(name1=name))
                    wechat_opin.Db_sync
                    print("get finish")
                    servo=0
                else:
                    print("现在不允许拿手机哦")
            else:
                print("save")
                place =xuan.get_diaodu_where({18,23})#现存的柜子id
                if place == 0:
                    print("没位置了")
                else:
                    from gpiozero.pins.pigpio import PiGPIOFactory
                    from gpiozero import Servo
                    pigpio_factory = PiGPIOFactory()
                    print(place)
                    servo = Servo(place, pin_factory= pigpio_factory)
                    servo.value= -0.6
                    time.sleep(5)
                    servo.value =1
                    GPIO.cleanup()
                    name = '''"'{a}'" '''.format(a=name)
                    xuan.add_data2('test','STATE',name,place)
                    wechat_opin.Db_isornotupdata('{name1}','True'.format(name1=name))
                    wechat_opin.Db_sync
                    print("save finish")
                    servo = 0 
        else:
            print("请先注册")
        
