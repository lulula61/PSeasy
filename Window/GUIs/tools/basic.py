from PIL import Image
import numpy as np
import cv2


def img_horizontal_reverse(img, x_start=None, y_start=None, x_end=None, y_end=None, polygon = None):
    temp = img.copy()
    wide = len(img[0])
    high = len(img)
    for i in range(len(img)):
        for j in range(wide):
            temp[i][wide - 1 - j] = img[i][j]
    return temp


def Rotate(img, angle=0, x_start=None, y_start=None, x_end=None, y_end=None):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    # 获得旋转矩阵并对图像进行旋转操作
    m = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(img, m, (w, h))
    return rotated_image


def Crop(img, x_start=None, y_start=None, x_end=None, y_end=None, polygon = None):
    if(x_start != None):
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    return img


if __name__ == '__main__':
    pth = "C:\\Users\\zly17\Pictures\\123.png"
    img = Image.open(pth)
    img = Crop(img, 20, 30, 100, 200)
    img.show()
