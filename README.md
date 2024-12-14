<h1>EPL_Predictive_Model_GUI</h1>
<p><strong>Predictive Model for EPL Player Performance with GUI</strong></p>

<h3>Group Project Description:</h3>
<p>This project was completed as part of our Business Programming (BP) class. The goal was to build a predictive model that estimates the performance of top English Premier League (EPL) players based on various input features, including goals, assists, and market value. The project leverages data from the 2020, 2021, and 2022 EPL seasons and uses machine learning for prediction.</p>

<h3>Key Features:</h3>
<ul>
  <li><strong>Data Collection</strong>: Data includes top 20 players from each season (2020, 2021, 2022) in the English Premier League.</li>
  <li><strong>Prediction Model</strong>: A multiple regression model that predicts player performance metrics (Goals, Assists, and Market Value).</li>
  <li><strong>GUI</strong>: A PyQt-based graphical user interface (GUI) allows users to input player data and get predictions in real time.</li>
  <li><strong>Currency Formatting</strong>: Market value predictions are displayed with the dollar symbol, rounded to two decimal places.</li>
</ul>

<h3>Technologies Used:</h3>
<ul>
  <li><strong>Python</strong>: pandas, scikit-learn, PyQt, dotenv</li>
  <li><strong>GitHub</strong>: Version control and project management</li>
</ul>

<h3>Roles:</h3>
<ul>
  <li><strong>Akshat Sharma</strong>: Responsible for data engineering tasks, including data preprocessing and building the PyQt-based GUI.</li>
  <li><strong>Atul Kumar Pandey</strong>: Responsible for machine learning model development, including feature engineering and model training.</li>
</ul>

<h3>Project Structure:</h3>
<pre>
EPL_Predictive_Model_GUI/
├── data/           # Store datasets here
├── scripts/        # Python scripts (ML, GUI) here
│   ├── ETL.py      # ETL script for data extraction, transformation, and loading
│   ├── GUI.py      # GUI script for user interface using PyQt
│   └── predict.py  # Prediction logic using the trained model
├── testing/        # Testing code
├── README.md       # Project overview
</pre>

<h3>How to Run:</h3>
<ol>
  <li><strong>Clone the repository</strong>:<br>
    <code>git clone https://github.com/yourusername/EPL_Predictive_Model_GUI.git</code></li>
  <li><strong>Install the required dependencies</strong>:<br>
    Navigate to the project directory and run the following command:
    <code>pip install -r requirements.txt</code></li>
  <li><strong>Set up environment variables</strong>:<br>
    Make sure to create a <code>.env</code> file in the root of the project.<br>
    Add the API key to the <code>.env</code> file as follows:
    <pre>
    API_KEY=your_api_key_here
    </pre>
  </li>
  <li><strong>Run the application</strong>:<br>
    Execute the following command to start the GUI and make predictions:
    <code>python main.py</code></li>
</ol>

<h3>ETL Process:</h3>
<p>The <code>ETL.py</code> script is responsible for the data extraction, transformation, and loading process. It requires an API key for accessing the necessary data. You must add your API key to the <code>.env</code> file for the script to work properly.</p>

<h3>Prediction Process:</h3>
<p>The <code>predict.py</code> script contains the logic for making predictions based on user inputs using the trained machine learning model. The script takes the player data as input, processes it, and provides predictions for goals, assists, and market value.</p>

<h3>Requirements (<code>requirements.txt</code>):</h3>
<p>Here is the <code>requirements.txt</code> file for your project:</p>
<pre>
pandas==1.5.3
scikit-learn==1.2.0
PyQt5==5.15.9
python-dotenv==1.0.0
numpy==1.23.5
</pre>
