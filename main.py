import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, 
    QVBoxLayout, QWidget, QListWidget, QMessageBox
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Web Browser")
        self.widget = QWidget(self)

        # Web view
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.google.com/"))
        self.webview.urlChanged.connect(self.url_changed)

        # Navigation buttons
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.webview.back)
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.webview.forward)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.webview.reload)

        # URL address bar
        self.url_text = QLineEdit()

        # Button to load URL
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.url_set)

        # Button to add bookmarks
        self.bookmark_button = QPushButton("Add Bookmark")
        self.bookmark_button.clicked.connect(self.add_bookmark)

        # Bookmark list
        self.bookmark_list = QListWidget()
        self.bookmark_list.itemClicked.connect(self.load_bookmark)

        # Top layout (Navigation bar)
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.refresh_button)
        self.toplayout.addWidget(self.url_text)
        self.toplayout.addWidget(self.go_button)
        self.toplayout.addWidget(self.bookmark_button)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.webview)
        self.layout.addWidget(self.bookmark_list)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Bookmarks storage
        self.bookmarks = []

    def url_changed(self, url):
        """Refresh the address bar"""
        self.url_text.setText(url.toString())

    def url_set(self):
        """Load the new URL"""
        self.webview.setUrl(QUrl(self.url_text.text()))

    def add_bookmark(self):
        """Add the current URL to bookmarks"""
        url = self.url_text.text().strip()
        if url and url not in self.bookmarks:
            self.bookmarks.append(url)
            self.bookmark_list.addItem(url)
        else:
            QMessageBox.warning(self, "Bookmark Error", "URL is empty or already bookmarked!")

    def load_bookmark(self, item):
        """Load the clicked bookmark"""
        self.webview.setUrl(QUrl(item.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())
