import cv2
import numpy as np

class matrix_rain():
	"""each number takes 7 rows and 7 columns in any given colour image
	This needs to be initialized with an image of the required size. Then it can work
	on any image of that size.
	   outputs simple number rain or edged number rain depending on flag"""
	def __init__(self,image,flag=0,mul=1.0):
		self.flag=flag  #determines whether number rain or edge detected matrix would come out
		self.font,self.lin_type=cv2.FONT_HERSHEY_SIMPLEX,cv2.LINE_AA
		self.imshape=image.shape
		self.brightness_factor=np.array([mul])   #just to make things brighter
		self.transform=np.float32([ [1,0,0], [0,1,1] ])
		self.row,self.col=int(self.imshape[0]/7)+1,int(self.imshape[1]/7)+1
		self.rain_buffer=np.random.randint(low=0,high=10,size=self.col)
		self.c=0                     #counter;counts for 7 times
		self.rain_draw=np.zeros((self.imshape[0]+7,self.imshape[1]),dtype=np.uint8)
		self.begin_rain_draw()
	def cvt2rain(self,image):
		if image.shape!=self.imshape: return 0
		img=self.superimpose(image)
		self.c+=1
		if self.c==7:
			self.use_buffer()
			self.c=0
		return cv2.multiply(img,self.brightness_factor)
	def superimpose(self,image):
		thresholdable=self.rain_draw[7:]
		_,mask=cv2.threshold(thresholdable,100,255,cv2.THRESH_BINARY)
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		gray_edged=self.gray_edging(gray)
		raining=cv2.bitwise_and(gray_edged,gray_edged,mask=mask)
		ret_image=np.zeros(self.imshape,dtype=np.uint8)
		ret_image[:,:,0],ret_image[:,:,1],ret_image[:,:,2]=0,raining,0
		self.update_rain_draw()
		return ret_image
	def use_buffer(self):
		for j in range(self.col):
			cv2.putText(self.rain_draw,str(self.rain_buffer[j]),(j*7,7),self.font,0.2,255,1,self.lin_type)
		self.rain_buffer=np.random.randint(low=0,high=10,size=self.col)  #update buffer
		return
	def update_rain_draw(self):
		self.rain_draw=cv2.warpAffine(self.rain_draw,self.transform,(self.imshape[1],self.imshape[0]+7))
		return
	def begin_rain_draw(self):
		rain=np.random.randint(low=0,high=10,size=(self.row+1,self.col))
		for i in range(self.row+1):
			for j in range(self.col):
				cv2.putText(self.rain_draw,str(rain[i][j]),(j*7,(i+1)*7),self.font,0.2,255,1,self.lin_type)
		return
	def gray_edging(self,img):
		if self.flag: img=cv2.Canny(img, 150, 246)
		return img







#main

if __name__=="__main__":
	ret,cap = False,cv2.VideoCapture(0)
	while not ret:
		ret,frame=cap.read()
	num_rainer=matrix_rain(frame,mul=2.0)
	line_rainer=matrix_rain(frame,flag=1)
	rainer=matrix_rain(frame,flag=1)
	while True:
	    ret, frame = cap.read()
	    if not ret: continue
	    frame=cv2.flip(frame,1)
	    num_img=num_rainer.cvt2rain(frame)
	    line_img=line_rainer.cvt2rain(frame)
	    img=rainer.cvt2rain(num_img)
	    cv2.imshow("Doubly Worked Matrix",img)
	    cv2.imshow("Edge Detected Matrix",line_img)
	    cv2.imshow("Number Raining Matrix",num_img)
	    if cv2.waitKey(1) & 0xFF==ord("q"):
	        break
	cap.release()
	cv2.destroyAllWindows()