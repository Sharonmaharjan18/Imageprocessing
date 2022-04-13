try:
  import numpy as np
except ImportError:
  print(f'Install numpy using "pip install numpy" command')
else:
  print(f'Numpy installed version: {np.__version__}')

try:
  import matplotlib as plt
except ImportError:
  print(f'Install Matplotlib using "pip install matplotlib" command')
else:
  print(f'Matplotlib installed version: {plt.__version__}')

try:
  import cv2
except ImportError:
  print(f'Install OpenCV using "pip install opencv-python" command')
else:
  print(f'OpenCV installed version: {cv2.__version__}')









