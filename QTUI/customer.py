import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드
        loadUi('customer.ui', self)

        # 버튼 클릭 이벤트 처리
        self.pushButton_4.clicked.connect(self.onpushButton_4Click)

    def onpushButton_4Click(self):
        # 버튼 클릭 시 동작
        # text = self.lineEdit.text()  # QLineEdit에서 텍스트 가져오기
        # self.label.setText(f'입력한 텍스트: {text}')  # QLabel에 텍스트 설정
        print('clicked pushButton_4')

if __name__ == '__main__':
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # MyDialog 인스턴스 생성
    dialog = MyDialog()

    # 다이얼로그 실행
    dialog.exec_()

    # 이벤트 루프 진입
    sys.exit(app.exec_())
