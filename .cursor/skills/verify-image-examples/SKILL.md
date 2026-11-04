---
name: verify-image-examples
description: Drive openCV's actual desktop image examples on an isolated display and verify image-processing outputs before editing the examples.
---
# Verify OpenCV image examples
## Surface and isolation
Eight independent Python desktop image examples plus two legacy webcam scripts. The safe drive uses only repository images and actual desktop windows. It never opens a camera or records a face. Desktop GUI proof is separate from camera/classification accuracy.
## Launch
Create a Python3 virtualenv and install this skill's requirements.txt (opencv-python, not the headless package). Linux needs Xvfb, xdotool and ImageMagick import plus OpenCV's GUI libraries. Run from repo root. The helper launches its own Xvfb display with an unused display number, then each real script as a separate process.
## Doctor
`python .cursor/skills/verify-image-examples/helpers/drive.py doctor --out .verification-evidence/doctor`
Checks actual cv2 import, helper command availability and all three input images decode. No camera/server is started.
## Drive
`python .cursor/skills/verify-image-examples/helpers/drive.py drive --out .verification-evidence/run`
Runs smoothing, crop, grayscale, resize, edges, rotation, shapes and dimensions/color scripts unchanged except the proven smoothing kernel correction. Waits for their real visible named windows, captures each window, sends a key to exit waitKey, and requires zero exit. Separately verifies real13x13Gaussian output has same shape and changed pixels. No GUI method is mocked.
## Evidence
Retained JSON includes process results/window titles and screenshots; actual desktop pixels must be inspected. Source face image is an illustration from the repo, not collected personal biometric input. PNG iCCP warning in coins.png and Xvfb focus warnings are retained, not hidden as successful warning-free execution. Rotation's fixed-size canvas intentionally clips corner content; no redesign claim.
## Cleanup
Terminates/reaps only its own child and display, including failures. Evidence survives cleanup. No camera, network, shared data or user desktop session is touched. Virtual display is an explicit stand-in for a physical display, not native device certification.
## Helpers
Executable helpers/drive.py provides doctor/drive and --out. See features/README.md for all mapped surfaces and exact unverified prerequisites. Install dependencies in a private virtualenv, not systemwide. Maintain the map as examples change.
