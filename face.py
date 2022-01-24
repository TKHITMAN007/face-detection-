import cv2

cap = cv2.VideoCapture('C:/Users/tanay/Downloads/tbbt.mp4')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, 0)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    count = 0
    for (x, y, w, h) in faces:
        c = 0
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        count = count + 1

        # Display the box and faces
        cv2.putText(frame, 'face num' + str(count), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print('box dimension and no. of faces',(x, y, w, h), count)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
