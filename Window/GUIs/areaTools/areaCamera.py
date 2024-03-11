import cv2
import numpy as np
from GUIs.tools import color


def autumn(img, points):

    pts = np.array([[int(pt.x()), int(pt.y())] for pt in points])
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.fillPoly(mask, [pts], (255, 255, 255))
    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    cv2.fillPoly(mask, [pts], 255)

    result_masked = cv2.bitwise_and(img, img, mask=mask)
    result_gray = cv2.cvtColor(result_masked, cv2.COLOR_BGR2GRAY)
    result_colored = cv2.applyColorMap(result_gray, cv2.COLORMAP_AUTUMN)

    return result_colored



def bone(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_BONE)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def jet(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_JET)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def winter(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_WINTER)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def rainbow(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_RAINBOW)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def ocean(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_OCEAN)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def summer(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_SUMMER)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def spring(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_SPRING)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def cool(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_COOL)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def hsv(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_HSV)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def pink(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_PINK)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def hot(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    result = cv2.applyColorMap(result_gray, cv2.COLORMAP_HOT)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def gray(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
    result = np.uint8(np.clip((1.2 * result_gray + 0), 0, 255))
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def sketch(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    num_down = 1
    num_bilateral = 3

    for _ in range(num_down):
        result = cv2.pyrDown(result)

    for _ in range(num_bilateral):
        result = cv2.bilateralFilter(result, d=3, sigmaColor=5, sigmaSpace=5)

    for _ in range(num_down):
        result = cv2.pyrUp(result)

    result_gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)

    result = cv2.medianBlur(result_gray, 3)

    result = cv2.adaptiveThreshold(result, 256,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY,
                                   blockSize=5,
                                   C=2)

    result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def cartoon(img, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    result = color.convertchannel(img)
    result_gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
    result_blur = cv2.medianBlur(result_gray, 5)

    result_edge = cv2.adaptiveThreshold(result_blur, 128,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY,
                                        blockSize=9,
                                        C=8)
    result_edge = cv2.cvtColor(result_edge, cv2.COLOR_GRAY2RGB)
    result = cv2.bitwise_and(result, result_edge)

    result = np.uint8(np.clip((2.0 * result + 16), 0, 255))
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img
