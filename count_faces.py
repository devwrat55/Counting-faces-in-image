# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:46:41 2020

@author: MLops
"""
#IMP
#https://myaccount.google.com/lesssecureapps
#go here and change the security of the account so that email can be sent
senders_emailid = "enter your's"
password = "enter your's"
subject = "Attendance count"
emids=["devwratneve@gmail.com"] #reciever's

imgname = ["img12.jpg", "img15.jpg", "img25.jpg"]

import random
selected = random.choice(imgname)

#https://myaccount.google.com/lesssecureapps
#go here and change the security of the account
def send_email(user, pwd, recipient, subject, body):
    import smtplib
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()

import cv2

photo = cv2.imread(selected)
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cor = face_model.detectMultiScale(photo)

count_msg = "Number of people/student(s) present in pucture : "+str(len(face_cor))
   
if len(face_cor) == 0:
    for i in range(len(emids)):
        send_email(senders_emailid,password,emids[i],subject,count_msg)
    pass
else:
    for j in range(len(face_cor)):
        x1  = face_cor[j][0]
        y1 = face_cor[j][1]
        x2 = x1 + face_cor[j][2]
        y2 = y1 + face_cor[j][3]
        photo = cv2.rectangle(photo , (x1,  y1) , (x2, y2), [0,255,0], 3)  
    font = cv2.FONT_HERSHEY_SIMPLEX 
    # org 
    org = (10, 25) 
    # fontScale 
    fontScale = 0.7
    # Blue color in BGR 
    color = (0,0,0) 
    # Line thickness of 2 px 
    thickness = 2
    # Using cv2.putText() method 
    photo = cv2.putText(photo, "count : " + str(len(face_cor)) , org, font, 
                        fontScale, color, thickness, cv2.LINE_AA) 
    # Displaying the image 
    cv2.imshow("IMAGE", photo)  
    #cv2.imshow('IMAGE' , photo)
    cv2.waitKey()
    
    cv2.destroyAllWindows()
    for i in range(len(emids)):
        send_email(senders_emailid,password,emids[i],subject,count_msg)
#print(len(face_cor))       
cv2.destroyAllWindows()