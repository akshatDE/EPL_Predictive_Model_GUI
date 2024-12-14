import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout
from PyQt5.QtCore import Qt
from predict import FootballPlayerPredictor  # Assuming the class is in 'football_predictor.py'

class PredictionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EPL Player Performance Predictor")
        self.setGeometry(100, 100, 400, 300)

        # Initialize FootballPlayerPredictor
        self.predictor = FootballPlayerPredictor(csv_path='data/epl_data_with_market_value.csv')

        # Create the input fields
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Form Layout for user inputs
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

        # Button to trigger prediction
        self.predict_button = QPushButton("Predict", self)
        self.predict_button.clicked.connect(self.make_prediction)

        # Labels for displaying results
        self.result_label = QLabel("Prediction Results will appear here.", self)

        layout.addLayout(form_layout)
        layout.addWidget(self.predict_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

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