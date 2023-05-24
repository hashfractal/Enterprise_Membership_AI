import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
from mysql import *

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('customer.ui', self)
        self.myDB = mySqlDB()
        self.already = False
        print(self.myDB)
        # 버튼 클릭 이벤트 처리
        self.pushButton_1.clicked.connect(self.onInsertClick) 
        self.pushButton_2.clicked.connect(self.onUpdateClick)
        self.pushButton_3.clicked.connect(self.onDeleteClick)
        self.pushButton_4.clicked.connect(self.onSearchClick)
    def clearLineEdit(self):
        self.lineEdit_1.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.already = False
    def onInsertClick(self):        
        if (not self.already):
            print('Insert customer')
            self.myDB.insert(self.lineEdit_1.text(),self.lineEdit_2.text(), \
                                    self.lineEdit_3.text(),self.lineEdit_4.text())            
        else :
            QMessageBox.information(self,'Insert','새로운 코드를 사용하세요')
    def onUpdateClick(self):        
        if (self.already):
            print('Update customer')
            result= self.myDB.update(self.lineEdit_1.text(),self.lineEdit_2.text(), \
                                    self.lineEdit_3.text(),self.lineEdit_4.text())
            if result:
                QMessageBox.information(self,'Update','정상적으로 업뎃 되었습니다.')
                self.already = False
        else :
            QMessageBox.information(self,'Update','먼저 조회 하세요')

    def onDeleteClick(self):        
        print('Delete customer')
        if (self.already):
            self.myDB.delete(self.lineEdit_1.text())
        else :
            QMessageBox.information(self,'Delete','먼저 조회 하세요')

    def onSearchClick(self):
        # Search Data 조회버튼 
        result = self.myDB.customSearch(self.lineEdit_5.text())
        
        if result :
            self.lineEdit_1.setText(result['code'])
            self.lineEdit_2.setText(result['name'])
            self.lineEdit_3.setText(result['tel'])
            self.lineEdit_4.setText(result['addr'])
            self.already = True
        else :
            # 찾는 데이터가 없을때 신규. 
            # 신규 번호는 Auto Increse를 사용 할 수도 있지만 수동 구현
            QMessageBox.information(self,'신규등록','신규 입력시 코드를 입력후 재 검색하세요')
            # 또는 code 필드의 값중에서 가장 큰 값을 조회해서 varChar를 int로 바꾸고 
            # +1을 한 다음 0으로 4자리를 채운 문자열을 만들어 사용할수도 있습니다. 
        return

if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # MyDialog 인스턴스 생성
    dialog = MyDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
