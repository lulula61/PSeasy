import cv2
import numpy as np
import matplotlib.pyplot as plt
import random


def convertchannel(img):
    if img.shape[2] == 4:
        result = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    elif img.shape[2] == 1:
        result = cv2.cvtColor(img, cv2.COLOR_GREY2BGR)
    else:
        result = img
    return result


# def show_img_plt(img_array, title=[]):
#     size = len(img_array)
#     plt.figure()
#     for i in range(1, size + 1):
#         plt.subplot(1, size, i)
#         if len(img_array[i - 1].shape) == 2:
#             plt.imshow(img_array[i - 1], cmap='gray')
#         else:
#             img_array[i -
#                       1] = cv2.cvtColor(img_array[i - 1].copy(), cv2.COLOR_BGR2RGB)
#             plt.imshow(img_array[i - 1])
#         if len(title):
#             plt.title(title[i - 1])
#     plt.show()


# def img_show(img):
#     cv2.imshow("Son4ta", img)
#     cv2.waitKey()


# def Laplace(img):
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
#     temp = np.array(img)
#     H, W = img.shape
#     kernel_size = len(kernel)
#     margin = int(kernel_size / 2)
#     result = np.zeros(img.shape)
#     img = cv2.copyMakeBorder(img, margin, margin, margin,
#                              margin, borderType=cv2.BORDER_REPLICATE)
#     img = np.array(img)
#     for i in range(margin, H + margin):
#         for j in range(margin, W + margin):
#             pix = np.sum(kernel * img[i - margin: i +
#                                       margin + 1, j - margin: j + margin + 1])
#             result[i - margin, j - margin] = pix

#     return result


# def sharpen(img):
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
#     temp = np.array(img)
#     H, W = img.shape
#     kernel_size = len(kernel)
#     margin = int(kernel_size / 2)
#     result = np.zeros(img.shape)
#     img = cv2.copyMakeBorder(img, margin, margin, margin,
#                              margin, borderType=cv2.BORDER_REPLICATE)
#     img = np.array(img)
#     for i in range(margin, H + margin):
#         for j in range(margin, W + margin):
#             pix = np.sum(kernel * img[i - margin: i +
#                                       margin + 1, j - margin: j + margin + 1])
#             result[i - margin, j - margin] = pix

#     result = temp - result
#     result[result < 0] = 0
#     result[result > 255] = 255
#     return result


# def salt_and_pepper_noise(img, proportion=0.05):
#     noise_img = img
#     height, width = noise_img.shape[0], noise_img.shape[1]
#     num = int(height * width * proportion)  # 多少个像素点添加椒盐噪声
#     for i in range(num):
#         w = random.randint(0, width - 1)
#         h = random.randint(0, height - 1)
#         if random.randint(0, 1) == 0:
#             noise_img[h, w] = 0
#         else:
#             noise_img[h, w] = 255
#     return noise_img


# def Sobel(img, threshold=0):
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     H, W = img.shape
#     x_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
#     y_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
#     kernel_size = len(x_kernel)
#     margin = int(kernel_size / 2)
#     x_result = np.zeros(img.shape)
#     y_result = np.zeros(img.shape)
#     img = cv2.copyMakeBorder(img, margin, margin, margin,
#                              margin, borderType=cv2.BORDER_REPLICATE)
#     for i in range(margin, H + margin):
#         for j in range(margin, W + margin):
#             x_pix = sum(
#                 sum(x_kernel * img[i - margin: i + margin + 1, j - margin: j + margin + 1]))
#             y_pix = sum(
#                 sum(y_kernel * img[i - margin: i + margin + 1, j - margin: j + margin + 1]))
#             if x_pix > threshold:
#                 x_result[i - margin, j - margin] = x_pix
#             if y_pix > threshold:
#                 y_result[i - margin, j - margin] = y_pix
#     # return [img, x_result, y_result, x_result + y_result]
#     return x_result + y_result


# def median_filter(img, kernel_size):
#     H, W, C = img.shape
#     margin = int(kernel_size / 2)
#     result = img.copy()
#     img = cv2.copyMakeBorder(img, margin, margin, margin,
#                              margin, borderType=cv2.BORDER_REPLICATE)
#     for i in range(margin, H + margin):
#         for j in range(margin, W + margin):
#             for c in range(C):
#                 result[i - margin, j - margin, c] = np.median(
#                     img[i - margin: i + margin + 1, j - margin: j + margin + 1, c])
#     return result


# def max_min_filter(img, kernel_size):
#     H, W, C = img.shape
#     margin = int(kernel_size / 2)
#     max_result = img.copy()
#     min_result = img.copy()
#     img = cv2.copyMakeBorder(img, margin, margin, margin,
#                              margin, borderType=cv2.BORDER_REPLICATE)
#     for i in range(margin, H + margin):
#         for j in range(margin, W + margin):
#             for c in range(C):
#                 max_result[i - margin, j - margin, c] = np.max(
#                     img[i - margin: i + margin + 1, j - margin: j + margin + 1, c])
#                 min_result[i - margin, j - margin, c] = np.min(
#                     img[i - margin: i + margin + 1, j - margin: j + margin + 1, c])
#     return [max_result, min_result]


def middle_filter(img, kernel_size, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    H, W, C = img.shape
    kernel = np.ones([kernel_size, kernel_size])
    margin = int(kernel_size / 2)
    result = img.copy()
    img = cv2.copyMakeBorder(img, margin, margin, margin,
                             margin, borderType=cv2.BORDER_REPLICATE)

    for i in range(margin, H + margin):
        for j in range(margin, W + margin):
            for c in range(C):
                result[i - margin, j - margin, c] = sum(
                    sum(kernel * img[i - margin: i + margin + 1, j - margin: j + margin + 1, c])) // (kernel_size ** 2)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def binary_filter(img, kernel_size=3, x_start=None, y_start=None, x_end=None, y_end=None):
    sigma1 = 150
    sigma2 = 150
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    img_tmp = convertchannel(img)
    result = cv2.bilateralFilter(img_tmp, kernel_size, sigma1, sigma2)
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = result
    else:
        Img = result
    return Img


def max_filter(img, kernel_size, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    img_tmp = convertchannel(img)
    H, W, C = img_tmp.shape
    margin = int(kernel_size / 2)
    max_result = img_tmp.copy()
    img = cv2.copyMakeBorder(img_tmp, margin, margin,
                             margin, margin, borderType=cv2.BORDER_REPLICATE)
    for i in range(margin, H + margin):
        for j in range(margin, W + margin):
            for c in range(C):
                max_result[i - margin, j - margin, c] = np.max(
                    img_tmp[i - margin: i + margin + 1, j - margin: j + margin + 1, c])
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = max_result
    else:
        Img = max_result
    return Img


def min_filter(img, kernel_size, x_start=None, y_start=None, x_end=None, y_end=None):
    Img = img
    if x_start != None:
        img = img[int(y_start):int(y_end), int(x_start):int(x_end)]
    img_tmp = convertchannel(img)
    H, W, C = img_tmp.shape
    margin = int(kernel_size / 2)
    min_result = img_tmp.copy()
    img_tmp = cv2.copyMakeBorder(
        img_tmp, margin, margin, margin, margin, borderType=cv2.BORDER_REPLICATE)
    for i in range(margin, H + margin):
        for j in range(margin, W + margin):
            for c in range(C):
                min_result[i - margin, j - margin, c] = np.min(
                    img_tmp[i - margin: i + margin + 1, j - margin: j + margin + 1, c])
    if x_start != None:
        Img[int(y_start):int(y_end), int(x_start):int(x_end)] = min_result
    else:
        Img = min_result
    return Img


"""
if __name__ == '__main__':
    main()
"""
