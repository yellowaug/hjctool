from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
import sys

# 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
# # app = QApplication(sys.argv)
# # # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
# # w = QWidget()
# # w.resize(500,500)
# # w.move(300,300)
# # w.setWindowTitle("test")
# # w.show()
# # sys.exit(app.exec_())
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法
    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",10))
        # ms="test<b>QWidget</b>test"
        # self.setToolTip(ms)
        #创建按钮的方法
        btn=QPushButton("quit",self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        ms = "test<b>Quit method</b>test"
        btn.setToolTip(ms)
        #按钮尺寸
        btn.resize(btn.sizeHint())
        #按钮位置
        btn.move(50,50)
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('test')
        # 设置窗口的图标，引用当前目录下的web.png图片
        # self.setWindowIcon(QIcon('web.png'))
        # 显示窗口
        self.show()
    def closeEvent(self, btn):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            btn.accept()
        else:
            btn.ignore()

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())