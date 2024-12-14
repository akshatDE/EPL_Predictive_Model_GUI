import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Extracting Data 
def extract_data():
    """
    This function extracts the data from the API and returns the cleaned data in the form of a list
    For EPL Seasons 2020,2021,2022 these are passed as arguments to the function
    """
    headers = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": api_key
    }
    years = [2020, 2021, 2022]
    cleaned_data = []
    for year in years:
        url = f"https://v3.football.api-sports.io/players/topscorers?season={year}&league=39"
        response = requests.request("GET", url, headers=headers)
        data_json = response.json()
        for i in range(0, 20):
            player_names = data_json['response'][i]['player']['name']
            age = data_json['response'][i]['player']['age']
            height =data_json['response'][i]['player']['height']
            weight =data_json['response'][i]['player']['weight']
            team_name=data_json['response'][i]['statistics'][0]['team']['name']
            goals_scored=data_json['response'][i]['statistics'][0]['goals']['total']
            assists=data_json['response'][i]['statistics'][0]['goals']['assists']
            shots_on_target=data_json['response'][i]['statistics'][0]['shots']['on']
            key_passes=data_json['response'][i]['statistics'][0]['passes']['key']
            minutes_played=data_json['response'][i]['statistics'][0]['games']['minutes']

            data_dict = {
            'Player Name': player_names,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Team Name': team_name,
            'Goals Scored': goals_scored,
            'Assists': assists,
            'Shots on Target': shots_on_target,
            'Pass Accuracy': key_passes,
            'Minutes Played': minutes_played
            }
            cleaned_data.append(data_dict)
    return cleaned_data

# Transforming Data
def transform_data():
    """
    This function transforms the data by converting the list of dictionaries to a dataframe

    Also it checks for the data types of the columns and converts them to the required data types

    Null values are also handled in this function
    """
    req_data = extract_data()
    print("Number of records extracted:", len(req_data))
    
    df = pd.DataFrame(req_data)
    # Checking for the data types of the columns
    df.drop_duplicates(inplace=True)

    df['Age'] = df['Age'].astype(int)
    df['Height'] = df['Height'].apply(lambda x: x.split('cm')[0]).astype(int)
    df['Weight'] = df['Weight'].apply(lambda x: x.split('kg')[0]).astype(int)

    # Assits column has one NAN value for a particular player
    # Replacing the NAN value with 0
    df['Assists'].fillna(0, inplace=True)

    # Again checking for the data types of the columns
    # Checking for the data types of the columns
    df.info()

    return df

# Loading Data to CSV file /EPS_Predictive_Model_GUI/data/epl_data.csv
def load_data_to_csv():
    """
    This function loads the cleaned data to a csv file
    """
    df = transform_data()
    df.to_csv('data/epl_data.csv', index=False)
    print('Data Loaded to CSV')

# Running the ETL pipeline
if __name__ == '__main__':
    """
    This is the main function which calls all the functions in the ETL pipeline

    As of now, the API key is hardcoded in the script.

    In future user has to pass the API key as an argument to the function

    User can get the API key by signing up on the website

    Website for API key: https://www.api-football.com/

    The API key is stored in the .env file and user have to first add the API key to the .env file

    Then load the API key using the load_dotenv() function
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")

    # Calling the function for data loading to a csv file
    print(transform_data())
    load_data_to_csv()


