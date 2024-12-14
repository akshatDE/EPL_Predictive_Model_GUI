import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

class FootballPlayerPredictor:
    def __init__(self, csv_path='data/epl_data_with_market_value.csv'):
        """
        Initialize the predictor with data loading and preprocessing
        """
        # Load data
        self.df = pd.read_csv(csv_path)
        
        # Preprocessing
        self.preprocess_data()
        
        # Train selected models
        self.train_models()
    
    def preprocess_data(self):
        """
        Preprocess the data for model training
        """
        # Remove duplicate rows
        self.df.drop_duplicates(inplace=True)
        
        # Select features and target variables
        self.features = ['Age', 'Height', 'Weight', 'Minutes Played', 'Goals Scored', 'Assists']
        
        # Define prediction targets
        self.targets = {
            'Goals Prediction': 'Goals Scored',
            'Assists Prediction': 'Assists',
            'Market Value Prediction': 'Market Value (Millions $)'
        }
        
        # Prepare feature matrix and target dictionaries
        self.X = self.df[self.features]
        self.y = {target_name: self.df[target_col] 
                  for target_name, target_col in self.targets.items()}
    
    def train_models(self):
        """
        Train regression models for selected predictions
        """
        # Store models and scalers
        self.models = {}
        self.scalers = {}
        self.error_metrics = {}  # To store model error (MSE and standard error)

        # Train a model for each target
        for target_name, target_col in self.targets.items():
            # Prepare data
            X = self.X
            y = self.y[target_name]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Train Random Forest Regressor with optimized parameters
            model = RandomForestRegressor(
                n_estimators=200,  # More trees for better performance
                max_depth=10,  # Limit depth to reduce overfitting
                random_state=42
            )
            model.fit(X_train_scaled, y_train)
            
            # Evaluate the model
            y_pred = model.predict(X_test_scaled)
            mse = mean_squared_error(y_test, y_pred)
            std_error = np.sqrt(mse)  # Calculate standard error
            
            # Store error metrics
            self.error_metrics[target_name] = {
                'Mean Squared Error': round(mse, 2),
                'Standard Error': round(std_error, 2)
            }
            
            # Store model and scaler
            self.models[target_name] = {
                'model': model,
                'scaler': scaler
            }
        
        print("Models trained successfully!")
    def predict(self, input_data):
        """
        Make predictions for a given set of input features
        
        :param input_data: Dict with keys ['Age', 'Height', 'Weight', 'Minutes Played', 'Goals Scored', 'Assists']
        :return: Dict of predictions
        """
        # Validate input
        required_features = ['Age', 'Height', 'Weight', 'Minutes Played', 'Goals Scored', 'Assists']
        for feature in required_features:
            if feature not in input_data:
                raise ValueError(f"Missing required feature: {feature}")
        
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Store predictions
        predictions = {}
        
        # Make predictions for selected models
        for target_name, model_data in self.models.items():
            # Scale input
            input_scaled = model_data['scaler'].transform(input_df[self.features])
            
            # Predict
            prediction = model_data['model'].predict(input_scaled)[0]
            
            # Format predictions
            if target_name == 'Market Value Prediction':
                predictions[target_name] = f"${round(prediction, 2)} Million"
            else:
                predictions[target_name] = round(prediction, 2)
        
        return predictions

def interactive_prediction():
    """
    Interactive interface for making predictions
    """
    predictor = FootballPlayerPredictor()
    
    print("\n--- EPL Player Performance Predictor ---")
    print("Enter player characteristics for prediction:")
    
    # Get user input
    age = float(input("Age (years): "))
    height = float(input("Height (cm): "))
    weight = float(input("Weight (kg): "))
    minutes_played = float(input("Minutes Played: "))
    goals_scored = float(input("Goals Scored: "))
    assists = float(input("Assists: "))
    
    # Prepare input
    input_data = {
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Minutes Played': minutes_played,
        'Goals Scored': goals_scored,
        'Assists': assists
    }
    
    # Make predictions
    try:
        predictions = predictor.predict(input_data)
        
        # Display results
        print("\n--- Prediction Results ---")
        for pred_name, pred_value in predictions.items():
            print(f"{pred_name}: {pred_value}")
    
    except ValueError as e:
        print(f"Error: {e}")

# Example usage and interactive mode
if __name__ == '__main__':
    interactive_prediction()