from controller import Controller
from PyQt5.QtWidgets import QApplication


def main() -> None:
    """Create and show the main application window."""
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
