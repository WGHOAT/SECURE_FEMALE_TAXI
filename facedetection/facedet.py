import cv2
import os
import numpy as np

# Loading Haar Cascade for face detection
haar_cascade_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_cascade_file)

dataset_path = 'datasets'

print("Training...")

(images, labels, names, id) = ([], [], {}, 0)

for (subdirs, dirs, files) in os.walk('/home/rohith/Documents/vscode/facedetection/getpic'):
    for subdir in dirs:
        names[id] = subdir
        subject_path = os.path.join('/home/rohith/Documents/vscode/facedetection/getpic', subdir)

        for filename in os.listdir(subject_path):
            label = id
            path = os.path.join(subject_path, filename)
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

images = np.array(images)
labels = np.array(labels)

(width, height) = (130, 100)

# Create the LBPH face recognizer
model = cv2.face.LBPHFaceRecognizer_create()

model.train(images, labels)

cam = cv2.VideoCapture(0)
cnt = 0

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < 95:
            cv2.putText(im, f'{names[prediction[0]]}-{prediction[1]:.2f}', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 0, 255))
            print(names[prediction[0]])
            cnt = 0
        else:
            cnt += 1
            cv2.putText(im, 'unknown', (x + 10, y + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            if cnt > 100:
                print("unknown person")
                cv2.imwrite("unknown.jpg", im)
                cnt = 0

    cv2.imshow('facerecognition', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
