import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QTextEdit, QGridLayout, QPushButton

class InventoryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

    def init_ui(self):
        self.setWindowTitle('입고 정보')
        
        # 아이템명 레이블과 입력 위젯
        item_name_label = QLabel('아이템명:')
        self.item_name_input = QLineEdit()
        
        # 아이템 종류 레이블과 콤보 박스
        item_type_label = QLabel('아이템 종류:')
        self.item_type_combobox = QComboBox()
        self.item_type_combobox.addItems(['의류', '전자제품', '도서'])
        
        # 입고 수량 레이블과 입력 위젯
        quantity_label = QLabel('입고 수량:')
        self.quantity_input = QLineEdit()
        
        # 입고 내용 레이블과 입력 위젯
        description_label = QLabel('입고 내용:')
        self.description_input = QTextEdit()
        
        # 저장 버튼
        save_button = QPushButton('저장')
        save_button.clicked.connect(self.save_data)
        
        # 그리드 레이아웃 설정
        layout = QGridLayout()
        layout.addWidget(item_name_label, 0, 0)
        layout.addWidget(self.item_name_input, 0, 1)
        layout.addWidget(item_type_label, 1, 0)
        layout.addWidget(self.item_type_combobox, 1, 1)
        layout.addWidget(quantity_label, 2, 0)
        layout.addWidget(self.quantity_input, 2, 1)
        layout.addWidget(description_label, 3, 0)
        layout.addWidget(self.description_input, 3, 1)
        layout.addWidget(save_button, 4, 0, 1, 2)
        
        self.setLayout(layout)
        self.show()

    def save_data(self):
        item_name = self.item_name_input.text()
        item_type = self.item_type_combobox.currentText()
        quantity = self.quantity_input.text()
        description = self.description_input.toPlainText()
        # 여기에서 입력된 정보를 저장하거나 처리하는 로직을 구현합니다.
        # 예를 들면, 데이터베이스에 저장하거나 파일에 쓰는 등의 작업을 수행할 수 있습니다.
        print(f'아이템명: {item_name}')
        print(f'아이템 종류: {item_type}')
        print(f'입고 수량: {quantity}')
        print(f'입고 내용: {description}')
        self.close()