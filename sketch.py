import cv2
import numpy as np
def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

vc = cv2.VideoCapture(0)
while True:
    ret, frame = vc.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == ord('p'):
        break

vc.release()
cv2.destroyAllWindows()