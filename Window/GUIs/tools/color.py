import cv2
import numpy as np
import copy


def convertchannel(img):
    if img.shape[2] == 4:
        result = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    elif img.shape[2] == 1:
        result = cv2.cvtColor(img, cv2.COLOR_GREY2BGR)
    else:
        result = img
    return result


def split_channel(img):
    img_tmp = convertchannel(img)
    img_b, img_g, img_r = cv2.split(img_tmp)
    return img_r, img_g, img_b


def change_color(img_c, channel, rgb):
    result = copy.deepcopy(img_c)
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            result[x][y] = int(rgb[channel] * result[x][y])
            if result[x][y] > 255:
                result[x][y] = 255
    return result


def join_channel(chr, chg, chb):
    result = cv2.merge((chb, chg, chr))
    return result


def change_color_all(img, channel_r=100, channel_g=100, channel_b=100, x_start=None, y_start=None, x_end=None, y_end=None):
    if(x_start != None):
        roi = img[int(y_start):int(y_end), int(x_start):int(x_end)]
        rgb = [channel_r/100, channel_g/100, channel_b/100]
        img_r, img_g, img_b = split_channel(roi)
        img_r = change_color(img_r, 0, rgb)
        img_g = change_color(img_g, 1, rgb)
        img_b = change_color(img_b, 2, rgb)
        roi_result = join_channel(img_r, img_g, img_b)
        img[int(y_start):int(y_end), int(x_start):int(x_end)] = roi_result
        return img
    else:
        rgb = [channel_r / 100, channel_g / 100, channel_b / 100]
        img_r, img_g, img_b = split_channel(img)
        img_r = change_color(img_r, 0, rgb)
        img_g = change_color(img_g, 1, rgb)
        img_b = change_color(img_b, 2, rgb)
        result = join_channel(img_r, img_g, img_b)
        return result


def add_contrast1(img, channel_r=100, channel_g=100, channel_b=100, x_start=None, y_start=None, x_end=None, y_end=None):
    if x_start != None:
        roi = img[int(y_start):int(y_end), int(x_start):int(x_end)]
        img_tmp = convertchannel(roi)
        hist, _ = np.histogram(img_tmp.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        roi_result = cdf[img_tmp]
        img[int(y_start):int(y_end), int(x_start):int(x_end)] = roi_result
        return img
    else:
        img_tmp = convertchannel(img)
        hist, _ = np.histogram(img_tmp.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        result = cdf[img_tmp]
        return result


def add_contrast2(img, channel_r=100, channel_g=100, channel_b=100, x_start=None, y_start=None, x_end=None, y_end=None):
    if x_start != None:
        roi = img[int(y_start):int(y_end), int(x_start):int(x_end)]
        img_tmp = convertchannel(roi)
        img_r, img_g, img_b = split_channel(img_tmp)
        img_r = cv2.equalizeHist(img_r)
        img_g = cv2.equalizeHist(img_g)
        img_b = cv2.equalizeHist(img_b)
        roi_result = join_channel(img_r, img_g, img_b)
        img[int(y_start):int(y_end), int(x_start):int(x_end)] = roi_result
        return img
    else:
        img_tmp = convertchannel(img)
        img_r, img_g, img_b = split_channel(img_tmp)
        img_r = cv2.equalizeHist(img_r)
        img_g = cv2.equalizeHist(img_g)
        img_b = cv2.equalizeHist(img_b)
        result = join_channel(img_r, img_g, img_b)
        return result


def add_contrast3(img, channel_r=100, channel_g=100, channel_b=100, x_start=None, y_start=None, x_end=None, y_end=None):
    if x_start != None:
        roi = img[int(y_start):int(y_end), int(x_start):int(x_end)]
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img_tmp = convertchannel(roi)
        img_r, img_g, img_b = split_channel(img_tmp)
        img_r = clahe.apply(img_r)
        img_g = clahe.apply(img_g)
        img_b = clahe.apply(img_b)
        roi_result = join_channel(img_r, img_g, img_b)
        img[int(y_start):int(y_end), int(x_start):int(x_end)] = roi_result
        return img
    else:
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img_tmp = convertchannel(img)
        img_r, img_g, img_b = split_channel(img_tmp)
        img_r = clahe.apply(img_r)
        img_g = clahe.apply(img_g)
        img_b = clahe.apply(img_b)
        result = join_channel(img_r, img_g, img_b)
        return result


if __name__ == '__main__':
    pth = 'E:\Me\College\大三下\软件工程原理\大作业\imgs\woman_0.jpg'
    img = cv2.imdecode(np.fromfile(pth, dtype=np.uint8), -1)
    cv2.imshow("origin", img)
    print(img.shape)
    img2 = add_contrast1(img)

    cv2.imshow("woman", img2)
    cv2.waitKey()
