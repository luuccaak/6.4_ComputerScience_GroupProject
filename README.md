# 6.4_ComputerScience_GroupProject
Group No. 6.4

Streamlit Group Project for Fundamentals in Computer Science

# Watch Investment App

## Purpose
The **Watch Investment App** is designed to guide users in selecting, analyzing, and investing in luxury watches. It provides:

- Personalized recommendations based on user profiles.
- Real-time currency conversion.
- Detailed watch insights.
- An investment calculator for projecting returns over time.

This application is ideal for users interested in blending personal luxury with smart investment strategies.

---

## Features

1. **User Questionnaire**: Collects income, investment amount, age, and risk tolerance to recommend watches tailored to individual profiles.
2. **Watch Recommendations**: Displays personalized watch recommendations with brand details, pricing, and currency conversion options.
3. **Detailed Watch Insights**: Offers in-depth information about the selected watch, including price trends and historical data.
4. **Investment Calculator**: Simulates potential investment returns over different time horizons and scenarios.
5. **Real-Time Currency Conversion**: Converts prices to the user’s preferred currency using live exchange rates.

---

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**:
   Ensure `pip` is installed and run the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare datasets**:
   Place `watchdata5.csv` in the project root directory. Ensure this file contains the required watch information.

4. **Run the application**:
   Execute the main file `Watch.py` using Streamlit:
   ```bash
   streamlit run Watch.py
   ```

5. **Access the app**:
   Open your browser and go to `http://localhost:8501`.

---

## Walkthrough

1. **Start at the Questionnaire**:
   - Navigate to the initial page to provide income, investment amount, age, and risk tolerance.
   - Submit the form to receive personalized watch recommendations.

2. **View Recommendations**:
   - Browse watches tailored to your profile.
   - Use currency conversion to see prices in your preferred currency.
   - Select a watch for more details.

3. **Explore Watch Details**:
   - View in-depth data, including price history and brand details.
   - Analyze historical price trends with interactive charts.

4. **Investment Calculation**:
   - Simulate potential returns by adjusting investment amount, time horizon, and risk scenarios.
   - View projected returns and platform fees.

---

## Explanation of the Code

### Core Files

1. **`Watch.py`**:
   - Entry point for the application.
   - Manages navigation between pages (Questionnaire, Recommendations, Details, Investment Calculator).
   - Loads `watchdata5.csv` for watch information.

2. **`page1_questionnaire.py`**:
   - Implements the questionnaire functionality.
   - Utilizes K-Nearest Neighbors (KNN) for watch recommendations.
   - Preprocesses user input and dataset for machine learning predictions.

3. **`page2_recommendations.py`**:
   - Displays personalized recommendations.
   - Integrates live currency conversion through `api.py`.
   - Facilitates exploration of additional watches.

4. **`page3_watch_detail.py`**:
   - Provides detailed insights into the selected watch.
   - Visualizes price history using Matplotlib.

5. **`page4_investment_calculator.py`**:
   - Simulates investment scenarios based on the selected watch.
   - Computes returns using time horizon, ROI scenarios, and platform fees.

6. **`api.py`**:
   - Handles API calls for fetching live exchange rates.
   - Caches results to optimize performance.

7. **`watchdata5.csv`**:
   - Dataset containing watch details (brand, price, historical data).
   - Required for recommendations and detailed insights.

### External Dependencies

- **Streamlit**: Builds an interactive UI for the app.
- **Scikit-learn**: Implements machine learning models for recommendations.
- **Matplotlib**: Creates visualizations for price history.
- **Pandas**: Processes CSV data and user inputs.
- **Requests**: Fetches live exchange rates from the API.

---

## Data Flow

1. **Input**:
   - User data from sliders and dropdowns (income, age, risk tolerance).
   - Watch data from `watchdata5.csv`.
2. **Processing**:
   - Machine learning for personalized recommendations.
   - Currency conversion using live exchange rates.
3. **Output**:
   - Display recommendations, detailed watch information, and investment projections.

---

## Sources and References

- **Streamlit Documentation**: [https://docs.streamlit.io](https://docs.streamlit.io)
- **Scikit-learn Documentation**: [https://scikit-learn.org](https://scikit-learn.org)
- **Matplotlib Documentation**: [https://matplotlib.org](https://matplotlib.org)
- **Free Currency API**: [https://freecurrencyapi.com](https://freecurrencyapi.com)
- **ChatGPT**: Code optimization and assistance.

---

## Future Enhancements

- Expand watch dataset with more brands and historical data.
- Integrate advanced machine learning models for enhanced recommendations.
- Add user authentication for personalized data persistence.
- Implement advanced visualizations for investment analysis.
- Provide multilingual support for a global audience.

