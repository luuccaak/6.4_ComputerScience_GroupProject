# 6.4_ComputerScience_GroupProject
Group No. 6.4

Streamlit Group Project for Fundamentals in Computer Science

Purpose

The Watch Investment App is designed to guide users in selecting, analyzing, and investing in luxury watches. It provides personalized recommendations based on user profiles, real-time currency conversion, detailed watch insights, and an investment calculator for projecting returns over time. This application is ideal for users interested in blending personal luxury with smart investment strategies.

Features

User Questionnaire: Collects income, investment amount, age, and risk tolerance to recommend watches tailored to individual profiles.

Watch Recommendations: Displays personalized watch recommendations with brand details, pricing, and currency conversion options.

Detailed Watch Insights: Offers in-depth information about the selected watch, including price trends and historical data.

Investment Calculator: Simulates potential investment returns over different time horizons and scenarios.

Real-Time Currency Conversion: Converts prices to the user’s preferred currency using live exchange rates.

Installation Instructions

Prerequisites

Python 3.8 or higher

Virtual environment (optional but recommended)

Steps

Clone the repository:

git clone <repository-url>
cd <repository-folder>

Install dependencies:
Ensure pip is installed and run the following command:

pip install -r requirements.txt

Prepare datasets:

Place watchdata5.csv in the project root directory. Ensure this file contains the required watch information.

Run the application:
Execute the main file Watch.py using Streamlit:

streamlit run Watch.py

Access the app:
Open your browser and go to http://localhost:8501.

Walkthrough

Start at the Questionnaire:

Navigate to the initial page to provide income, investment amount, age, and risk tolerance.

Submit the form to receive personalized watch recommendations.

View Recommendations:

Browse watches tailored to your profile.

Use currency conversion to see prices in your preferred currency.

Select a watch for more details.

Explore Watch Details:

View in-depth data, including price history and brand details.

Analyze historical price trends with interactive charts.

Investment Calculation:

Simulate potential returns by adjusting investment amount, time horizon, and risk scenarios.

View projected returns and platform fees.

Explanation of the Code

Core Files

Watch.py:

Entry point for the application.

Manages navigation between pages (Questionnaire, Recommendations, Details, Investment Calculator).

Loads watchdata5.csv for watch information.

page1_questionnaire.py:

Implements the questionnaire functionality.

Utilizes K-Nearest Neighbors (KNN) for watch recommendations.

Preprocesses user input and dataset for machine learning predictions.

page2_recommendations.py:

Displays personalized recommendations.

Integrates live currency conversion through api.py.

Facilitates exploration of additional watches.

page3_watch_detail.py:

Provides detailed insights into the selected watch.

Visualizes price history using Matplotlib.

page4_investment_calculator.py:

Simulates investment scenarios based on the selected watch.

Computes returns using time horizon, ROI scenarios, and platform fees.

api.py:

Handles API calls for fetching live exchange rates.

Caches results to optimize performance.

watchdata5.csv:

Dataset containing watch details (brand, price, historical data).

Required for recommendations and detailed insights.

External Dependencies

Streamlit: Builds an interactive UI for the app.

Scikit-learn: Implements machine learning models for recommendations.

Matplotlib: Creates visualizations for price history.

Pandas: Processes CSV data and user inputs.

Requests: Fetches live exchange rates from the API.

Data Flow

Input:

User data from sliders and dropdowns (income, age, risk tolerance).

Watch data from watchdata5.csv.

Processing:

Machine learning for personalized recommendations.

Currency conversion using live exchange rates.

Output:

Display recommendations, detailed watch information, and investment projections.

Sources and References

Streamlit Documentation: https://docs.streamlit.io

Scikit-learn Documentation: https://scikit-learn.org

Matplotlib Documentation: https://matplotlib.org

Free Currency API: https://freecurrencyapi.com

ChatGPT: Code optimization and assistance.

Future Enhancements

Expand watch dataset with more brands and historical data.

Integrate advanced machine learning models for enhanced recommendations.

Add user authentication for personalized data persistence.

Implement advanced visualizations for investment analysis.

Provide multilingual support for a global audience
