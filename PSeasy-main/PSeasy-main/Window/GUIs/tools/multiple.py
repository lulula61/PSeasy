from PIL import Image
import os

from PyQt5.QtWidgets import QFileDialog


def batch_process_images(input_dir, output_dir):
    # 获取所有图片文件名
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.png')]

    # 逐个处理图片
    for file_name in image_files:
        # 打开图片文件
        image = Image.open(os.path.join(input_dir, file_name))

        # 进行图片处理
        image = image.resize((500, 500))
        image = image.convert('L')

        # 保存处理后的图片
        output_file_name = os.path.join(output_dir, os.path.splitext(file_name)[0] + '_processed.jpg')
        image.save(output_file_name)

if __name__ == '__main__':
    input_dir = 'C:\\Users\\29296\\Pictures'
    output_dir = 'C:\\Users\\29296\\Pictures\\temp'
    # input_dir, _ = QFileDialog.getExistingDirectory(self, '选择打开文件夹', './')
    # output_dir, _ = QFileDialog.getExistingDirectory(self, '选择保存文件夹', './')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    batch_process_images(input_dir, output_dir)
