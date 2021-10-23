# Import Module
import time,os # curly brace means Module , in java its called packet

while True:
    os.system('cls')
    lt=time.localtime()
    # print(time.strftime('%I:%M:%S %p',lt))  # ctrl +c = to interrupt loop
    print(time.strftime('%H:%M:%S %p',lt))  # ctrl +c 
    time.sleep(1)

