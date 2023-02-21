import os
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PIL import Image 
from PIL.ImageFilter import DETAIL, BLUR


class ImageProcessor:
    def __init__(self): 
        pass

    def load_image(self, filename):
        pass

    def save_image(self): 
        pass

    def bl_wt(self): 
        pass

    def to_left(self): 
        pass

    def to_right(self):
        pass

    def flip(self): 
        pass

    def go_blur(self):
        pass


def filter_images(files, extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result 


def choose_workdir():
    global workdir 
    workdir = QFileDialog.getExistingDirectory

def show_name_list():
    extentions = ['.jpg', '.jpeg', '.bmp', '.gif', '.png' ]
    choose_workdir()
    filenames = filter_images(os.listdir(workdir), extentions)

    
def show_info():
    my_info = QMessageBox()
    my_info.setText('Demo photo \nVer 1.0')



app = QApplication
window = QWidget()
window.resize(1200, 850)
window.setWindowTitle('Photo Redactor (v.0.0.1)')

btn_dir = QPushButton('Directory')
lb_image = QLabel('Image')
tbn_files =  QListWidget()

btn_left = QPushButton('Left')
btn_righ = QPushButton('Righ')

btn_flip = QPushButton('Flip')
btn_sharp = QPushButton('Sharp')
btn_bl_wt = QPushButton('Black and White')
btn_blure = QPushButton('Blure')
btn_conture = QPushButton('Conture')
btn_detail = QPushButton('Detalisation')

btn_info = QPushButton('INFO')

row = QHBoxLayout()
colmn1 = QVBoxLayout()
colmn2 = QVBoxLayout()

