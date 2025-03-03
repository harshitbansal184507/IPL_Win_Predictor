# IPL Win Predictor

[Live Application](https://iplwinpredictor-2024.streamlit.app/)  
[Kaggle Notebook](https://www.kaggle.com/code/harshitbansal122/ipl-win-predictor-2024)

## Overview
IPL Win Predictor is a Streamlit-based application that predicts the winning probability of an IPL match in real time based on the current match scenario. The prediction model is built using machine learning techniques and is integrated into the application to provide dynamic insights.

## Features
- Select the **batting** and **bowling** teams from dropdown menus.
- Choose the **city** where the match is being played.
- Input the **target score**, **current score**, **overs bowled**, and **wickets fallen**.
- Get real-time predictions for the **winning probabilities** of both teams.

## Installation

### Prerequisites
Ensure you have Python installed on your system.

### Steps to Set Up Locally
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/harshitbansal184507/IPL_Win_Predictor.git
   ```
2. **Navigate to the project directory:**  
   ```bash
   cd IPL_Win_Predictor
   ```
3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
To start the Streamlit app, run the following command:
```bash
streamlit run app.py
```
Once the app is running, open your browser and go to [http://localhost:8501](http://localhost:8501) to use the application.

## Model Information
- The predictive models are stored in `pipe.pkl` and `pipe5.pkl`.
- These models were trained using a Jupyter Notebook (`ipl_win_probability_predictor.ipynb`) available in the repository.
- The models use historical match data to compute probabilities based on live match inputs.

## Example Usage
1. Select **batting** and **bowling** teams from the dropdown menu.
2. Choose the **city** where the match is being played.
3. Enter the **target score**, **current score**, **overs bowled**, and **wickets fallen**.
4. Click on the **Predict** button.
5. The app will display the **winning probabilities** for both teams.

## Contributions
Feel free to contribute by submitting issues, feature requests, or pull requests to improve the application.


Developed by **Harshit Bansal**
