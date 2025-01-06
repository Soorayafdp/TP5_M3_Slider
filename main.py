import sys
from PyQt5.QtWidgets import QApplication, QWidget
from interface_gain import Ui_Form  # Import de l'interface générée par pyuic5


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # Connecter le slider au lcdNumber
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())  # Afficher la valeur initiale
        self.ui.horizontalSlider.valueChanged.connect(self.update_lcd)


    def update_lcd(self, value):
        """
        Méthode appelée lorsque la valeur du slider change.
        Elle met à jour le lcdNumber avec la nouvelle valeur.
        """
        self.ui.lcdNumber.display(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
