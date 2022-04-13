import cv2

# Read image using imread function
image = cv2.imread("color.png", cv2.IMREAD_COLOR)

B, G, R = cv2.split(image)

# To get the status of writing the image, save the value into a variable
statusB = cv2.imwrite('colorB.png',B)
if statusB == True:
  print(f'Written B image status: {statusB}')
else:
  print(f'Image B not saved')

statusG = cv2.imwrite('colorB.png',G)
if statusG == True:
  print(f'Written G image status: {statusG}')
else:
  print(f'Image G not saved')

statusR = cv2.imwrite('colorB.png', R)
if statusR == True:
    print(f'Written R image status: {statusR}')
else:
    print(f'Image R not saved')