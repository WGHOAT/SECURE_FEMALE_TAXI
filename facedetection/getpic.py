def capture_face(name):
    haar = 'haarcascade_frontalface_default.xml'
    ds = 'datasets'
    sd = 'champ'
    path = os.path.join(ds, sd)
    path_to_save_newface = os.path.join('/home/rohith/Documents/vscode/facedetection/getpic', name)

    if not os.path.exists(path_to_save_newface):
        os.makedirs(path_to_save_newface)

    (width, height) = (130, 100)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar)
    
    if face_cascade.empty():
        print("Error loading Haar cascade.")
        return

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        return

    count = 1

    while count <= 30:
        ret, im = cam.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite(os.path.join(path_to_save_newface, f'{count}.png'), face_resize)
            count += 1

        cv2.imshow('opencv', im)
        key = cv2.waitKey(10)
        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
