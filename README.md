# IPL_Win_Predictor 

Live at - https://iplwinpredictor-2024.streamlit.app/
kaggle notebook link - https://www.kaggle.com/code/harshitbansal122/ipl-win-predictor-2024

This project is a Streamlit application that predicts the winning probability of an IPL match based on the current match situation. The model is built using machine learning techniques and is integrated into the Streamlit app to provide real-time predictions.

##Features
Select the batting and bowling teams.
Choose the city where the match is being played.
Input the target score, current score, overs bowled, and wickets fallen.
Get the predicted winning probability for the batting and bowling teams.
#Installation
#Clone the repository:
bash
git clone https://github.com/harshitbansal184507/IPL_Win_Predictor.git
Change to the project directory:
bash
cd IPL_Win_Predictor
Install the required dependencies:
bash
pip install -r requirements.txt
Usage
Run the Streamlit app:
bash
streamlit run app.py
Open your web browser and go to http://localhost:8501 to view the app.
Model Information
The models used for prediction are stored in the files pipe.pkl and pipe5.pkl. These models were trained using a colab notebook (ipl_win_probability_predictor.ipynb) available in the repository.

Example
Select the batting and bowling teams from the dropdown menus.
Choose the city where the match is being played.
Input the target score, current score, overs bowled, and wickets fallen.
Click the "Predict" button to get the winning probabilities for the batting and bowling teams.
