import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, qApp, QGridLayout, QLabel, QLineEdit
class Sqlmana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('欢迎使用数据管理工具') #状态栏返回消息
        self.memu_list()
        self.ed_win()
        self.setGeometry(300,300,350,300)
        self.setWindowTitle("数据管理工具")
        self.show()
    def memu_list(self): #菜单栏，退出功能
        # 菜单栏文件信息
        exitact=QAction('&退出',self)
        cpmanegeact=QAction('&电脑信息管理',self)
        acmanageact=QAction('&账号管理',self)
        kvmact=QAction('&kvm管理',self)
        ###############################################
        # 设置快捷键
        exitact.setShortcut('Ctrl+Q')
        cpmanegeact.setShortcut('Ctrl+1')
        acmanageact.setShortcut('Ctrl+2')
        kvmact.setShortcut('Ctrl+2')
        ###############################################
        # 菜单栏文件描述
        exitact.setStatusTip('退出应用程序')
        cpmanegeact.setStatusTip('使用电脑信息管理工具')
        acmanageact.setStatusTip('使用账号管理工具')
        kvmact.setStatusTip('使用kvm管理工具')
        exitact.triggered.connect(qApp.quit)
        cpmanegeact.triggered.connect(self.cpmaact) #连接功能
        self.statusBar()
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&常用工具') #新建一个一级菜单栏名称
        fileMenu.addAction(cpmanegeact)
        fileMenu.addAction(acmanageact)
        fileMenu.addAction(kvmact)
        fileMenu.addAction(exitact)

    def ed_win(self):
        text_ed=QTextEdit()
        self.setCentralWidget(text_ed)
    def cpmaact(self):
        QLabel('111')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Sqlmana()
    sys.exit(app.exec_())
