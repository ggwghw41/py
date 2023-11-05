from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import*
from PyQt6.uic import loadUi
import sys
import MySQLdb as sql
import bancafe
#cửa sổ login
class login_w(QMainWindow):
    def __init__(self):
        super(login_w,self).__init__()
        uic.loadUi('login.ui',self)
        self.dang_nhap.clicked.connect(self.dang_nhap1)
        self.tao_tk.clicked.connect(self.tao_tk1)
    def tao_tk1(self):
        widget.setCurrentIndex(1)

    def dang_nhap1(self):
        user=self.tai_khoan.text()
        password=self.mat_khau.text()
        db=sql.connect('localhost','root','','login_app')
        query=db.cursor()
        query.execute("select * from tai_khoan where  admin='"+user+"' and pass='"+password+"'")
        kt=query.fetchone()
        if kt:
            QMessageBox.information(self,"Đăng nhập","Đăng nhập thành công")
            widget.setCurrentIndex(2)
        else:
            QMessageBox.information(self,"Đăng nhập","Sai rồi bạn êi -_-")
#cửa số tạo tài khoản
class tao_tai_khoan1(QMainWindow):
    def __init__(self):
        super(tao_tai_khoan1,self).__init__()
        uic.loadUi('tao_tai_khoan.ui',self)
        self.tao_tai_khoan.clicked.connect(self.tao)
        self.quay_lai.clicked.connect(self.exit)
    def tao(self):
        user=self.tao_tk.text()
        password=self.tao_mk.text()
        db=sql.connect('localhost','root','','login_app')

        query=db.cursor()
        query.execute("select * from tai_khoan where  admin='"+user+"' and pass='"+password+"'")

        kt=query.fetchone()
        if kt:
            QMessageBox.information(self,"TẠO TÀI KHOẢN","Nhập lại đêii cha nội,tài khoản này có đăng kí rồi -_-")
        else:
            query.execute("insert into tai_khoan value('"+user+"','"+password+"')")
            db.commit()
            QMessageBox.information(self,"TẠO TÀI KHOẢN","TẠO TÀI KHOẢN")
            widget.setCurrentIndex(0)
    def exit(self):
            widget.setCurrentIndex(0)
class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        uic.loadUi('bancafe.ui',self)

#xử lý

ung_dung=QApplication(sys.argv)
appp=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
login_from=login_w()
taotk=tao_tai_khoan1()
ap=main()
widget.addWidget(login_from)
widget.addWidget(taotk)
widget.addWidget(ap)
widget.setCurrentIndex(0)
widget.setFixedHeight(543)
widget.setFixedWidth(800)
widget.show()
ung_dung.exec()
