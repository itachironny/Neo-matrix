import cv2
import numpy as np
from random import randint
"""vid= cv2.VideoCapture(0)
ret, frame= vid.read()
danny=cv2.imread("danny.png")
height, width=np.size(img,0),np.size(img,1)
print (height, width)
for i in range(0,10,1):
    h=random.randint(20,height-20)
    w=random.randint(20,width-20)
    cv2.circle(img, (h,w), 2, (0,0,255), -1)
gdanny=cv2.cvtColor(danny,cv2.COLOR_BGR2GRAY)
ret, dmask=cv2.threshold(gdanny,150,255,cv2.THRESH_BINARY)

c=95

img= np.zeros((512,512,3), np.uint8)
for i in range(512):
    for j in range(512):
        img[i][j]=[255,0,0]"""
def greenscale(image,r=480,c=640):
    #r,c,cl=image.shape
    #img=np.zeros((r,c,3), np.uint8)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range(r):
        for j in range(c):
            image[i][j]=[0,gray_image[i][j],0]
    return image
def mov(l):
    m=[randint(0,9) for i in range(95)]
    l.pop()
    l.insert(0,m)
    return l
def num(l,c):
    img=np.zeros((480,640,3), np.uint8)
    for i in range(0,95):
        for j in range(0,95):
            cv2.putText(img,str(l[i][j]),(j*7,i*7+c), font, 0.2,(255,255,255),1,cv2.LINE_AA)
    return img
def supim(image,letter):
    a=greenscale(image)
    #img=np.zeros((480,640,3), np.uint8)
    for i in range(480):
        for j in range(640):
            if letter[i][j][0]<125:
                a[i][j]=[0,0,0]
    return a

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
print("Welcome to the MATRIX!\nPlease wait a second. Your MATRIX is being prepared.")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
l=[[randint(0,9) for i in range(95)] for j in range(95)]
c=0
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#s=input("Enter name of file:")
#out = cv2.VideoWriter(s+'.mp4', fourcc, 20.0, (640,480),True)
print("Your MATRIX is ready now. Please enjoy your stay.")
while True:
    if c==7:
        c=0
    ret, frame = cap.read()
    img=supim(frame,num(l,c))
    #out.write(img)
    cv2.imshow("Matrix",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    c+=1
    l=mov(l)
cv2.destroyAllWindows()
print("We are sorry to see you go. Please visit again soon.")
