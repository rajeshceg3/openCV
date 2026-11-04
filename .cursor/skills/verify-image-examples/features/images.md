# Static image transformations
## Sub-features
Smoothing, crop, grayscale, resize, edge detection, rotation, rectangle overlay and pixel/dimension readout.
## How to get to it (user POV)
Run a root Python example from repo root with OpenCV GUI and the tracked input PNGs. Observe the named window and press a key to exit.
## Driving it with drive.py
Drive all eight actual scripts on an owned virtual display, capture each resulting window and require normal key-exit. Smoothing output is also checked mathematically. dimensions_color prints the actual image dimensions and BGR pixel.
## Gotchas
Original smoothImage used even12x12kernel, which OpenCV rejects. Corrected13x13kernel is exercised. Current image transforms depend on root working directory. Rotation intentionally keeps original dimensions, so corners clip. Crop is only80x100pixels and centered in a wider OpenCV window. PNG profile warning remains for coins.png. No claim every transformation is artistically optimal.
