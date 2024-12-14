import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from scripts.predict import FootballPlayerPredictor  

class PredictionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EPL Player Performance Predictor")
        self.setGeometry(100, 100, 800, 400)

        # Initialize FootballPlayerPredictor
        self.predictor = FootballPlayerPredictor(csv_path='data/epl_data_with_market_value.csv')

        # Load DataFrame for displaying
        self.df = self.predictor.df

        # Create the input fields and table
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()  # Use horizontal layout to place the form and table side by side

        # Left side layout for input form
        form_layout = QFormLayout()
        self.age_input = QLineEdit(self)
        self.height_input = QLineEdit(self)
        self.weight_input = QLineEdit(self)
        self.minutes_played_input = QLineEdit(self)
        self.goals_scored_input = QLineEdit(self)
        self.assists_input = QLineEdit(self)

        form_layout.addRow("Age (years):", self.age_input)
        form_layout.addRow("Height (cm):", self.height_input)
        form_layout.addRow("Weight (kg):", self.weight_input)
        form_layout.addRow("Minutes Played:", self.minutes_played_input)
        form_layout.addRow("Goals Scored:", self.goals_scored_input)
        form_layout.addRow("Assists:", self.assists_input)

        # Button to trigger prediction with color styling
        self.predict_button = QPushButton("Predict", self)
        self.predict_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;  /* Green background */
                color: white;               /* White text */
                border-radius: 5px;         /* Rounded corners */
                font-size: 16px;            /* Larger text */
                padding: 10px 20px;         /* Padding around text */
            }
            QPushButton:hover {
                background-color: #45a049;  /* Darker green on hover */
            }
            """
        )
        self.predict_button.clicked.connect(self.make_prediction)

        # Labels for displaying results
        self.result_label = QLabel("Prediction Results will appear here.", self)

        # Add form layout and prediction button to the left side
        left_panel = QVBoxLayout()
        left_panel.addLayout(form_layout)
        left_panel.addWidget(self.predict_button)
        left_panel.addWidget(self.result_label)

        # Right side: Create a table to display the data (first 10 rows)
        self.table_widget = QTableWidget(self)
        self.load_table_data()

        # Add left and right panels to the main horizontal layout
        layout.addLayout(left_panel, 1)  # Left side takes 1/2 of the space
        layout.addWidget(self.table_widget, 2)  # Right side takes 2/3 of the space

        self.setLayout(layout)

    def load_table_data(self):
        """Load the first 10 rows of the DataFrame into the table."""
        # Set the row and column count based on the DataFrame
        self.table_widget.setRowCount(min(10, len(self.df)))  # Only display the first 10 rows for simplicity
        self.table_widget.setColumnCount(len(self.df.columns))  # Columns based on DataFrame
        
        # Set the table headers
        self.table_widget.setHorizontalHeaderLabels(self.df.columns)

        # Populate the table with data from the DataFrame
        for row_idx, row in self.df.head(10).iterrows():
            for col_idx, value in enumerate(row):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def make_prediction(self):
        # Get input values
        try:
            input_data = {
                'Age': float(self.age_input.text()),
                'Height': float(self.height_input.text()),
                'Weight': float(self.weight_input.text()),
                'Minutes Played': float(self.minutes_played_input.text()),
                'Goals Scored': float(self.goals_scored_input.text()),
                'Assists': float(self.assists_input.text())
            }

            # Make prediction using the model
            predictions = self.predictor.predict(input_data)

            # Display results
            result_text = "\n".join([f"{pred_name}: {pred_value}" for pred_name, pred_value in predictions.items()])
            self.result_label.setText(result_text)

        except ValueError as e:
            self.result_label.setText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PredictionApp()
    window.show()
    sys.exit(app.exec_())