import numpy as np
import cv2

# Capture from camera & intitialize cascade classifier
cam = cv2.VideoCapture(1)
face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
data = []
index = 0  

while True:
    # Fetch frame from camera
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Add fine tuning parameters for haar cascade 
        faces = face_cas.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
        # Extract face component
	    face_component = frame[y:y+h, x:x+w, :]
            fc = cv2.resize(face_component, (50, 50))
	    # Sample data every 10 frames
            if index%10 == 0 and len(data) < 20:
                data.append(fc)

            # Draw a rect around the detected face 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        index += 1 
        cv2.imshow('Image', frame)  

	# Break out of loop, when ESC key(id 27) is pressed
        if cv2.waitKey(1) == 27 or len(data) >= 20:
            break
    else:
        print "Camera not working"


cv2.destroyAllWindows()
data = np.asarray(data)

# Store data as np matrix
np.save('face_01', data)
