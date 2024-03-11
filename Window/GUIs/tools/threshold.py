from PIL import Image
import numpy as np
import cv2
from PyQt5.QtWidgets import QInputDialog, QMessageBox


def Threshold(img,threshold,x1,y1,x2,y2,points):

    result = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY),
                                        threshold, 255, cv2.THRESH_BINARY_INV)[1]
    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    return result

