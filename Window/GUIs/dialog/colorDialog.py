from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication



class colorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.x_edit = QLineEdit()
        self.y_edit = QLineEdit()
        self.z_edit = QLineEdit()
        self.confirm_button = QPushButton('确认')
        self.confirm_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('channel_r, 范围是 0-200 :'))
        layout.addWidget(self.x_edit)
        layout.addWidget(QLabel('channel_g, 范围是 0-200 :'))
        layout.addWidget(self.y_edit)
        layout.addWidget(QLabel('channel_b, 范围是 0-200 :'))
        layout.addWidget(self.z_edit)
        layout.addWidget(self.confirm_button)
        self.setLayout(layout)

    def get_params(self):
        x = float(self.x_edit.text())
        y = float(self.y_edit.text())
        z = float(self.z_edit.text())
        return x, y, z