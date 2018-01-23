import serial
import time
import config
import nncl_prim
from config import com_rel
from config import ch
from config import com
from config import mac
from config import data

class Switch:
	def __init__(self, port):
		self.sw = serial.Serial(port = port, dsrdtr = False, rtscts = False, xonxoff = False)

	def SwitchOn(self):
		self.sw.setDTR(True)

	def SwitchOff(self):
		self.sw.setDTR(False)

mySw = Switch(com_rel)



def rel():
    mySw.SwitchOn()
    print('sw on')
    time.sleep(3)
    mySw.SwitchOff()
    print('sw off')
    time.sleep(2)



def req():
    t=time.localtime()
    mySw.SwitchOn()
    print('on')
    time.sleep(5)
    command_intro = "amode 1 achno {} data :-{} 0 hex {}".format(ch, mac, data)
    command_ism = "amode 2 achno {} data :-{} 0 hex {}".format(ch, mac, data)

    res=nncl_prim.nncltool_exec_2(command_ism)
    #res=nncl_prim.nncltool_exec_2(command_intro)
    if res["mess"].find('DATA',1,300)>0:
        print(res,time.asctime(t))
    else:
        print(res)
        print('#######        повтор через 3 сек    #########')
        time.sleep(10)
        res=nncl_prim.nncltool_exec_2(command_intro)
        
        if res["mess"].find('DATA',1,300)>0:
            print(res,time.asctime(t))
        else:
            print(res,'--no answer !!!!!!!!!!!!!!!!')
            time.sleep(60)    
    mySw.SwitchOff()
    print('off')
    print('--------------------------------')
    time.sleep(2) 


while True:
    req()
    #rel()