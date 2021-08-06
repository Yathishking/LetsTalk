class ThemeEngine:
    def __init__(self, parent):
        self.parent = parent
        pass

    def initTheme(self):
        self.parent.setStyleSheet("""
            color: whitesmoke;
            background: #212121;
        """)

    def removeTheme(self):
        pass

    def changeTheme(self):
        pass
