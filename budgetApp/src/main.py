# brings everything together
import sys 
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import BudgetApp
from database import init_db

def main():
    app = QApplication(sys.argv)

    # init db
    if not init_db("expense.db"):
          QMessageBox.critical(None, "Error", "could not load database")
          sys.exit(1)

    window = BudgetApp() #refers the app
    window.show() # show the app

    sys.exit(app.exec())

if __name__ == "__main__":
        main()
