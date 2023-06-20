import cv2
capture = cv2.VideoCapture(0)
while True:
	ret,image = capture.read()
	cv2.imshow('nicholas',image)
	key = cv2.waitKey(5000)
	if key == 27:
		cv2.imwrite('munyao.jpg',image)
	break
capture.release()
cv2.destroyAllWindows()
SHADRACK NGUMBAU7:56 AM
if cv2.waitKey(5000) & 0xFF == ord('q'):
Omondi Steve8:00 AM
import cv2 as cv
cap = cv.VideoCapture(0)
while True:
	ret,img = cap.read()
	cv.imshow ('myphoto', img)
	key = cv.waitKey(5000) 
	if cv.waitKey(5000) & 0xFF == ord('q'):
		cv.imwrite('SteveOmondi.jpg',img)
	break
cap.release()
cv.destroyAllWindows()

SHADRACK NGUMBAU8:25 AM
ret, im = cap.read()
    cv2.imshow('playvideotest',im)
    if cv2.waitKey(3600000) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
Omondi Steve8:36 AM
import cv2 as cv
cap = cv.VideoCapture('Cars.mp4')
while True:
	ret, im = cap.read()
	cv.imshow('playvideotest',im)
	if cv.waitKey(20) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()
SHADRACK NGUMBAU8:45 AM
*************
import cv2

cap = cv2.VideoCapture('Cars.mp4')


car_cascade = cv2.CascadeClassifier('cars.xml')


while True:
	
	ret, frames = cap.read()
	
	
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)	

	
	cars = car_cascade.detectMultiScale(gray, 1.1, 4)	
	
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('carsvideo', frames)	
	
	if cv2.waitKey(33) == 27:
		break
cap.release()
cv2.destroyAllWindows()
