# Legacy face recording and detection
## Sub-features
Webcam frame capture, sample storage and KNN face classification.
## How to get to it (user POV)
face_detection/record_face.py and detect_face.py expect camera index1, cascade XML and local trained face_01.npy/face_02.npy. They use Python2 print syntax and inconsistent indentation, so Python3 startup is not supported as-is.
## Driving it with drive.py
Not executed. The safe image drive deliberately does not acquire a camera, collect faces or write biometric training samples. Needs separate modernization, explicit camera/privacy scope, actual device/fixture prerequisites and acceptance recipe.
## Gotchas
Source labels[40] assignment is outside the40row array; KNN ignores its targets argument and reads global labels; missing training arrays and cleanup/error loops need review. These are source findings, not proven/fixed camera behavior. No face recognition or recording acceptance is claimed.
