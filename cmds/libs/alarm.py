import time
import threading

class Alarm():
    def transfer_to_sec(self ,statement):
        time_pack = statement.split(':')
        
        totalSecond = int(time_pack[0])*3600 + int(time_pack[1])*60 + int(time_pack[2])*1
        
        return totalSecond
    
    def seperate_msg_to_time_and_msg(self, msg):
        para_list = msg.split('msg:')

        return para_list

   

