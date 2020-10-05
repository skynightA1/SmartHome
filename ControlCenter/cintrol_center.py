import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import serial
import time

def sendEmailAlert(msg):    
    with smtplib.SMTP(host="smtp.nlhs.tyc.edu.tw", port="25") as smtp:
        content = MIMEMultipart()
        content["subject"] = "[警報]"+msg
        content["from"] = "s8103720@email.nlhs.tyc.edu.tw"
        content["to"] = "s810372@email.nlhs.tyc.edu.tw"
        content.attach(MIMEText(msg))
        try:
            smtp.ehlo()
            smtp.send_message(content)
            print("訊息已發送!")
        except Exception as e:
            print("Error message: ", e)

IntruderAlert = False
S = serial.Serial('com5', 9600, timeout=2)
while True:
    data = S.readline().decode().rstrip()
    if data == "alert" and not IntruderAlert:
        IntruderAlert = True
        print("入侵警報！！！")
        sendEmailAlert("入侵警報！！！")
    elif data == "normal" and IntruderAlert:
        IntruderAlert = False
        print("警報解除")
        sendEmailAlert("警報解除")
    time.sleep(1)