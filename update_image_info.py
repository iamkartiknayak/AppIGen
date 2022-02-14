import os
from PIL import Image
from PyQt6.QtGui import QPixmap


def add_info(self, image_path):
    self.line_edit_image_path.setText(image_path)
    self.label_image_display.setPixmap(
        QPixmap(image_path).scaledToWidth(200))
    self.line_edit_image_path.setCursorPosition(0)
    self.label_status.setText('Waiting for project folder...')
    image = Image.open(image_path)
    image_name = image_path.split('/')[-1].split('.')[0]
    image_size, size_unit = get_image_size(image_path)
    image_type = image.format
    image_resolution = image.size
    image.close()
    image_info = f'{image_name}\n\n{image_size} {size_unit}\n\n{image_type}\n\n{image_resolution[0]} x {image_resolution[1]}'
    self.label_img_info.setText(image_info)


def get_image_size(image_path):
    image_size_in_kb = round(os.path.getsize(image_path) / 1000, 2)
    if image_size_in_kb > 1024:
        image_size_in_mb = round(image_size_in_kb / 1000, 2)
        return image_size_in_mb, "MB"
    return image_size_in_kb, "KB"
