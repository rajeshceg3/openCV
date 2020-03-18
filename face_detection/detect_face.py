import numpy as np
import cv2

# Initialize video and classifier
cam = cv2.VideoCapture(1)
face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

# Convert numpy matrices to vectors
face1 = np.load('face_01.npy').reshape((20, 50*50*3))  
face2=  np.load('face_02.npy').reshape((20, 50*50*3))    

print face1.shape, face2.shape
entries = {
    0: 'Person',
    1: 'Nil',
}

# Store labels in an array, Distribute among Person and Nil
labels = np.zeros((40, 1))
labels[:20, :] = 0.0    
labels[40, :] = 1.0 

# Merge both arrays
data = np.concatenate([face1, face2]) # (40, 7500)
print data.shape, labels.shape        # (40, 1)

# K Nearest Neighbors algorithm
def distance(x1, x2):
    return np.sqrt(((x1-x2)**2).sum())

def knn(x, train, targets, k=5):
    m = train.shape[0]
    dis = []
    for index in range(m):
        dis.append(distance(x, train[index])) # Store distance in a list
    dis = np.asarray(dis)
    index = np.argsort(dis)
    s_labels = labels[index][:k]
    counts = np.unique(s_labels, return_counts=True)
    return counts[0][np.argmax(counts[1])]

while True:
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)
	# Iterate through faces array
        for (x, y, w, h) in faces: 
	    # Preprocess image
            face_point = frame[y:y+h, x:x+w, :]
            fc = cv2.resize(face_point, (50, 50))
	    # Run knn algorithm
            result = knn(fc.flatten(), data, labels)
            # convert this label to int and get the corresponding name
            text = entries[int(result)]

            # display the name
            cv2.putText(frame, text, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('Identified face', frame)

        if cv2.waitKey(1) == 27:
            break
    else:
        print 'Camera not working'

cv2.destroyAllWindows()
