import cv2 as cv
import numpy as np

from PyQt5.QtGui import (
    QPixmap, 
    QFont,
    QImage
)
from PyQt5.QtWidgets import (QMainWindow, 
    QWidget, 
    QLineEdit, 
    QPushButton, 
    QGridLayout, 
    QVBoxLayout, 
    QHBoxLayout,
    QPlainTextEdit, 
    QTextEdit, 
    QFormLayout, 
    QGroupBox, 
    QLabel, 
    QFileDialog,
)

from PyQt5.QtCore import Qt
from styles import STYLES

from model import Model
from styles import STYLES



class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = Model('model/resnet.h5')
        self.msrcr_model = Model('model/resnet_msrcr.h5')
        self.data_img = None

        self.setFixedSize(400, 600)
        self.setWindowTitle('Glaucoma Classifier')
        self.setStyleSheet('''
                           background-color: #ffffff;
                           color: #312F2F;
                           ''')

        self._gnrLayout = QVBoxLayout()
        self._cntWidget = QWidget()
        
        self.setCentralWidget(self._cntWidget)
        
        self._cntWidget.setLayout(self._gnrLayout)
        
        self.create_widget()

    def create_widget(self):
        # <input_label>
        self.input_label = QLabel()

        self.input_image = QPixmap('img/input.jpg')
        self.input_image = self.input_image.scaled(400, 200, Qt.KeepAspectRatio)

        self.input_label.setPixmap(self.input_image)
        self.input_label.setAlignment(Qt.AlignCenter)
        
        self._gnrLayout.addWidget(self.input_label)

        # <browse_button>
        self.browse_button = QPushButton('Browse Data')
        self.browse_button.setFixedHeight(40)
        self.browse_button.setStyleSheet(STYLES['browse_button'])

        self._gnrLayout.addWidget(self.browse_button, alignment=Qt.AlignBottom)
        self.browse_button.clicked.connect(self.browse_func)

        # msrcr & msrcp layout
        self._msrLayout = QHBoxLayout()

        # <msrcr_button>
        self.msrcr_button = QPushButton('MSRCR + ResNet')
        self.msrcr_button.setFixedHeight(40)
        self.msrcr_button.setStyleSheet(STYLES['msrcr_button'])

        self._msrLayout.addWidget(self.msrcr_button)
        self.msrcr_button.clicked.connect(self.msrcr_func)

        # # <msrcp_button>
        # self.msrcp_button = QPushButton('MSRCP')
        # self.msrcp_button.setFixedHeight(40)
        # self.msrcp_button.setStyleSheet(STYLES['msrcp_button'])

        # self._msrLayout.addWidget(self.msrcp_button)
        # self.msrcp_button.clicked.connect(self.msrcp_func)

        # <predict_button>
        self.predict_button = QPushButton('ResNet')
        self.predict_button.setFixedHeight(40)
        self.predict_button.setStyleSheet(STYLES['predict_button'])

        self._msrLayout.addWidget(self.predict_button)
        self.predict_button.clicked.connect(self.predict_func)

        self._gnrLayout.addLayout(self._msrLayout)

        # <clf_label>
        self.clf_label = QLabel()

        # <clf_image>
        self.clf_image = QPixmap('img/classification.png')
        self.clf_image = self.clf_image.scaled(400, 200, Qt.KeepAspectRatio)
        # <normal_image>
        self.normal_image = QPixmap('img/normal.png')
        self.normal_image = self.normal_image.scaled(400, 200, Qt.KeepAspectRatio)
        # <cataract_image>
        self.cataract_image = QPixmap('img/cataract.png')
        self.cataract_image = self.cataract_image.scaled(400, 200, Qt.KeepAspectRatio)
        # <diabetic_image>
        self.diabetic_image = QPixmap('img/diabetic.png')
        self.diabetic_image = self.diabetic_image.scaled(400, 200, Qt.KeepAspectRatio)
        # <glaucoma_image>
        self.glaucoma_image = QPixmap('img/glaucoma.png')
        self.glaucoma_image = self.glaucoma_image.scaled(400, 200, Qt.KeepAspectRatio)

        self.clf_label.setPixmap(self.clf_image)
        self.clf_label.setAlignment(Qt.AlignCenter)
        
        self._gnrLayout.addWidget(self.clf_label)

    def browse_func(self):
        self.clf_label.setPixmap(self.clf_image)

        self.data_path = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg *.png *.jpeg)')[0]
        
        pixmap = QPixmap(self.data_path)
        pixmap = pixmap.scaled(224, 224, Qt.KeepAspectRatio)
        self.input_label.setPixmap(pixmap)

        self.data_img = cv.imread(self.data_path)
        self.data_img = cv.resize(self.data_img, (224, 224))

    def msrcr_func(self):
        self.data_img = self.model.msrcr(self.data_img)

        pixmap = QPixmap.fromImage(QImage(self.data_img.data, self.data_img.shape[1], self.data_img.shape[0], QImage.Format_RGB888))
        self.input_label.setPixmap(pixmap)

        img = np.expand_dims(self.data_img, axis=0)
        
        prediction = round(self.msrcr_model.predict(img)[0][0])

        if prediction == 1:
            self.clf_label.setPixmap(self.normal_image)
        else:
            self.clf_label.setPixmap(self.glaucoma_image)

    # tidak dipakai
    def msrcp_func(self):
        self.data_img = self.model.msrcp(self.data_img)

        pixmap = QPixmap.fromImage(QImage(self.data_img.data, self.data_img.shape[1], self.data_img.shape[0], QImage.Format_RGB888))
        self.input_label.setPixmap(pixmap)

    def predict_func(self):
        img = np.expand_dims(self.data_img, axis=0)
        
        prediction = round(self.model.predict(img)[0][0])

        if prediction == 1:
            self.clf_label.setPixmap(self.normal_image)
        else:
            self.clf_label.setPixmap(self.glaucoma_image)





