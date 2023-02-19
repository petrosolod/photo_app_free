import os
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PIL import Image 
from PIL.ImageFilter import DETAIL, BLUR

app = QApplication
