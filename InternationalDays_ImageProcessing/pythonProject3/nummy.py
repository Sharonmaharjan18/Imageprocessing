try:
    import matplotlib as plt
except ImportError as e:
    print(f'Install Matplotlib using "pip install matplotlib" command’)')
else:
    print(f'Matplotlib installed version: {plt.__version__}’)')

try:
    import cv2
except ImportError as e:
    print(f'Install OpenCV using "pip install opencv-python“ command’)')
else:
    print(f'OpenCV installed version: {cv2.__version__}’)')