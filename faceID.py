import cv2

model = cv2.face.LBPHFaceRecognizer_create()
model.read('/home/nano1/cvtest/faces.data')
print('loading training data finished')

face_cascade = cv2.CascadeClassifier('/home/nano1/opencv/data/haarcascades_cuda/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    cap.open()


cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

names = ['TIM']

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    
    for (x,y,w,h) in faces:
        frame = cv2.rectangle( frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (400,400))

        val = model.predict(face_img)
        print('label:{}, conf:{:.1f}'.format(val[0], val[1]))
        if val[1]<50:
            cv2.putText(
                    frame ,names[val[0]], (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0),3)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) ==27:
        cv2.destroyAllWindows()
        break
