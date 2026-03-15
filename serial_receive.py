import serial

# -------------------------- 配置区域 --------------------------
#这里填你在VSPE里创建的虚拟串口对的第二个，比如COM2
RECEIVE_PORT='COM2'
BAUDRATE=9600
# ----------------------------------------------------------------


#初始化串口
ser_receive=serial.Serial(
    port='COM2',#改成你创建的第二个串口号！
    baudrate=9600,
    timeout=1
)
#检查串口是否打开
if ser_receive.is_open:
    print(f'✅️接收端串口{ser_receive.port}已打开,正在监听数据...')
else:
    print('❌️接收端串口打开失败！')
    exit()

try:
    #循环监听数据
    while True:
        #读取一行数据(最多等1秒)
        received_data=ser_receive.readline().decode('utf-8').strip()
        #如果收到了数据，就打印出来
        if received_data:
            print(f'📥收到消息：{received_data}')

except KeyboardInterrupt:
    print('\n🛑接收停止')
    ser_receive.close()
    print('✅️串口已释放')

