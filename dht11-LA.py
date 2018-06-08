#coding:utf-8
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)

count = 0
ave_humid = 0
print("DHT11が起動しました")
while True:
    result = instance.read()
    if result.is_valid():
        humid = result.humidity
        if humid < 20:
            humid += 10
        else:
            pass
        #print("Humidity: %d %%" % humid)
        if count < 5:
            ave_humid += humid
            #print("ave_umidity: %d %%" % ave_humid)
            count += 1
        else:
            pass
        if count == 5:
            humid = ave_humid / 5 + 10
            temp = result.temperature + 1
            print("温度・湿度の取得に成功しました")
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % temp)
            print("Humidity: %d %%" % humid)
            fout = open('/home/pi/Desktop/AoLA/data.txt','w')
            fout.write("%d " % temp)
            fout.write("%d" % humid)
            fout.close()
            break
    else:
        print("温度・湿度の取得に失敗しました")
        print("もう一度取得します")
    time.sleep(1)
