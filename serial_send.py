import serial
import time


# -------------------------- 配置区域 --------------------------
#这里填你在VSPE创建虚拟串口对第一个，比如COM1
SEND_PORT='COM1'
BAUDRATE=9600
# -------------------------------------------------------------


#初始化串口
ser_send=serial.Serial(
    port='COM1',#改成你创建的第一个串口号！
    baudrate=9600,
    timeout=1
)
#检查串口是否打开
if ser_send.is_open:
    print(f'✅️发送端串口{ser_send.port}已打开,准备发数据...')
else:
    print('❌️发送端串口打开失败！')
    exit()

try:
        #循环发送数据
        count=1
        while True:
            #构造数据，必须加\n,接收端readline()才能识别
            data_to_send=f'Hello机器人!这是第{count}条信息\n'.encode('utf-8')
            #发送数据
            ser_send.write(data_to_send)
            print(f'📤已发送:第{count}条信息')
            count+=1
            time.sleep(1)#每隔一秒发一次
        
except KeyboardInterrupt:
        print('\n🛑发送停止')
        ser_send.close()
        print('✅️串口已释放')


