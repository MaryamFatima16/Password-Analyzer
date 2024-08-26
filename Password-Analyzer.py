import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


def analyze_password(password):
    """
    Analyzes the strength of the given password and provides recommendations.

    Parameters:
    password (str): The password to be analyzed.

    Returns:
    tuple: A tuple containing:
        - strength (str): The strength of the password ("Strong", "Moderate", or "Weak").
        - recommendations (list): A list of recommendations to improve the password.
    """
    score = 0
    recommendations = []

    # Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Password should be at least 8 characters long.")

    # Check if the password contains at least one uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        recommendations.append("Include at least one uppercase letter.")

    # Check if the password contains at least one lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        recommendations.append("Include at least one lowercase letter.")

    # Check if the password contains at least one number
    if re.search(r'[0-9]', password):
        score += 1
    else:
        recommendations.append("Include at least one number.")

    # Check if the password contains at least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        recommendations.append("Include at least one special character (e.g., !, @, #).")

    # Determine the strength of the password based on the score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, recommendations


class PasswordAnalyzer(QWidget):
    def __init__(self):
        """
        Initializes the PasswordAnalyzer widget and sets up the UI.
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Sets up the user interface of the PasswordAnalyzer widget.
        """
        self.setWindowTitle('Password Analyzer')  # Set the window title
        self.resize(450, 300)  # Set the window size to 450x300 pixels

        # Set the font for the entire widget
        font = QFont("Arial", 11)
        self.setFont(font)

        # Set the color palette for the UI elements
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(45, 45, 48))  # Background color of the window
        palette.setColor(QPalette.WindowText, Qt.white)  # Color of the window text
        palette.setColor(QPalette.Base, QColor(30, 30, 30))  # Background color of input fields
        palette.setColor(QPalette.AlternateBase, QColor(45, 45, 48))  # Color for alternate backgrounds
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))  # Background color of tooltips
        palette.setColor(QPalette.ToolTipText, Qt.black)  # Text color of tooltips
        palette.setColor(QPalette.Text, Qt.white)  # Color of text in widgets
        palette.setColor(QPalette.Button, QColor(70, 70, 70))  # Background color of buttons
        palette.setColor(QPalette.ButtonText, Qt.white)  # Text color of buttons
        palette.setColor(QPalette.BrightText, Qt.red)  # Color of bright text (e.g., error messages)
        palette.setColor(QPalette.Highlight, QColor(100, 100, 150))  # Color of selected items
        palette.setColor(QPalette.HighlightedText, Qt.white)  # Color of text on selected items
        self.setPalette(palette)

        # Create and set up the main layout
        main_layout = QVBoxLayout()

        # Create a label for password input
        self.password_label = QLabel('Enter your password:')
        self.password_label.setStyleSheet("color: white;")  # Set label text color to white

        # Create a QLineEdit widget for password input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password characters
        self.password_input.setStyleSheet("color: black;")  # Set text color in the input field to black

        # Create an Analyze button and connect it to the analyze_password method
        self.analyze_button = QPushButton('Analyze')
        self.analyze_button.setStyleSheet(
            "background-color: #5A9; color: white; font-weight: bold;")  # Set button color and text
        self.analyze_button.clicked.connect(self.analyze_password)  # Connect button click to analyze_password method

        # Create labels to display the results and recommendations
        self.result_label = QLabel('')
        self.recommendations_label = QLabel('')

        # Add widgets to the main layout
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(self.analyze_button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.recommendations_label)

        # Set the main layout for the widget
        self.setLayout(main_layout)

    def analyze_password(self):
        """
        Analyzes the entered password and updates the result and recommendations labels.
        """
        password = self.password_input.text()  # Get the text from the password input field
        strength, recommendations = analyze_password(password)  # Analyze the password

        # Update the result and recommendations labels with the analysis results
        self.result_label.setText(f"Password Strength: {strength}")
        self.recommendations_label.setText("\n".join(recommendations))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication object

    analyzer = PasswordAnalyzer()  # Create an instance of the PasswordAnalyzer widget
    analyzer.show()  # Show the widget

    sys.exit(app.exec_())  # Start the event loop and exit the application when done
