# app design
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView

from PyQt6.QtCore import QDate, Qt

from database import fetch_expenses, add_expenses, delete_expenses

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__() #initialise QWidget
        self.settings()
        self.appUI()
        self.load_tableData()

    def settings(self):
        self.setGeometry(750, 300, 550, 500)
        self.setWindowTitle("Budget Tracker")

    # Design
    def appUI(self):
        # create all objects 
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.dropdown = QComboBox() # choose a category of expense
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        self.table = QTableWidget(0,5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])

        # to extend the window
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_dropdown()

        # connect buttons
        self.btn_add.clicked.connect(self.add_expense)
        self.btn_delete.clicked.connect(self.delete_expense)   

        # self.apply_styles()     

        # add widgets to a layout (column or row)
        self.setup_layout()

    def setup_layout(self):
        master = QVBoxLayout()
        row0 = QHBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        # row0
        row0.addWidget(QLabel("Date"))
        row0.addWidget(self.date_box)
        row0.addWidget(QLabel("Category"))
        row0.addWidget(self.dropdown)

        # row1
        row1.addWidget(QLabel("Amount"))
        row1.addWidget(self.amount)
        row1.addWidget(QLabel("Description"))
        row1.addWidget(self.description)

        row2.addWidget(self.btn_add)
        row2.addWidget(self.btn_delete)

        master.addLayout(row0)
        master.addLayout(row1)
        master.addLayout(row2)
        master.addWidget(self.table)

        self.setLayout(master)

# add some css
    # def apply_styles(self):
    #      # can target each object individually Qpushbutton ..
    #      self.setStyleSheet("""
    #                         QWidget{
    #                             background-color: pink;
    #                             font-family: Arial;
    #                         }

    #                         QLabel{
    #                             color: blue;
    #                             padding: 5px;
    #                         }

    #                         QLineEdit, QComboBox, QDateEdit{
    #                             background-color: #fff;
    #                             border-radius: 15px;
    #                             padding: 5px; 
    #                         }

    #                         QLineEdit:hover, QComboBox:hover, QDateEdit:hover{
    #                             border: 1px solid green;
    #                         }

    #                         QLineEdit:focus, QComboBox:focus, QDateEdit:focus{
    #                             border: 1px solid green;
    #                             background-color: white;
    #                         }

    #                         QTableWidget {
    #                             background-color: #fff;
    #                             alternate-background-color: purple;
    #                             gridline-color: grey;
    #                             selection-background-color: green;
    #                             selection-color: white;
    #                             border 1px solid red;
    #                         }


    #                         """)

    def populate_dropdown(self):
        categories = ["Food", "Rent", "Bills", "Shopping"]
        self.dropdown.addItems(categories)

    def load_tableData(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)

        for row_id, expense in enumerate(expenses):
            self.table.insertRow(row_id)
            for col_id, data in enumerate(expense):
                self.table.setItem(row_id, col_id, QTableWidgetItem(str(data)))

    def clear_inputs(self):
            self.date_box.setDate(QDate.currentDate())
            self.dropdown.setCurrentIndex(0)
            self.amount.clear()
            self.description.clear()

# collect the info we need
    def add_expense(self):

        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text() 
        description = self.description.text()

        #checks
        if not amount or not description:
            QMessageBox.warning(self, "Input Error", "Amount and description cant be empty")
            return
        
        if add_expenses(date, category, amount, description):
            self.load_tableData() # reload

            # clear inputs
            self.clear_inputs()

        else:
                QMessageBox.critical(self,"Error","Failed to add expense")

    def delete_expense(self):
        # select by clocking a row and delete it
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "oops","you need to select a row to delete")
            return 
        
        expense_id = int(self.table.item(selected_row, 0).text()) # first column
        confirm = QMessageBox.question(self, "Confirm", "Are you sure you want to delete ?", QMessageBox.StandardButton.Yes  | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expenses(expense_id):
             self.load_tableData()
        
