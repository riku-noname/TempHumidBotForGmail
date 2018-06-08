#coding:utf-8

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# メイン関数
if __name__ == '__main__':
    temp = 0
    humid = 0

    for line in open('/home/pi/Desktop/AoLA/data.txt','r'):
        data = line.split()
        temp += float(data[0])
        humid += float(data[1])
        #print("%d" % temp)
        #print("%d" % humid)
        

    # 以下の内容を変更する
    # me : 自分のGmail アドレス, you : 送信先のアドレス, passwd : Gmailパスワード
    me = "frommail@gmail.com"
    passwd = "xxxxxxxxxxxxx"
    you = "tomail@gmail.com"
    titletext = "KC104の温度・湿度報告【18時】"
    body = "研究室の皆様\n \nアオラです．\n現在のKC104の温度，湿度に関して報告致します．\n \n---------------\n時間 : 18時\n温度 : " + str(int(temp)) + " ℃\n湿度 : " + str(int(humid)) + "％\n---------------\n \n以上です．\n失礼致します．\n \n--------------------\n同志社大学 理工学部\n知的システムデザイン研究室\nアオラ <Assistant of LA>\nmail : aola@mikilab.doshisha.ac.jp\n--------------------"

    msg = MIMEText(body)
    msg['Subject'] = titletext
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)
    s.send_message(msg)
    s.close()
