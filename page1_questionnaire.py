import streamlit as st
import pandas as pd
import os 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from api import fetch_exchange_rates  # Import the centralized API logic

def questionnaire():
    # Load the first dataset for machine learning
    file_path = os.path.join("investment_data.csv")
    df_ml = pd.read_csv(file_path, delimiter=',')
    
    # Data preprocessing for machine learning
    for col in ['income', 'investment_amount']:
        if df_ml[col].dtype == 'object':
            df_ml[col] = df_ml[col].str.replace(',', '').astype(float)

    label_encoders = {
        'risk_tolerance': LabelEncoder(),
        'recommended_watch': LabelEncoder()
    }
    for col, encoder in label_encoders.items():
        df_ml[col] = encoder.fit_transform(df_ml[col])

    scaler = StandardScaler()
    numerical_features = ['income', 'investment_amount', 'age']
    df_ml[numerical_features] = scaler.fit_transform(df_ml[numerical_features])

    # Validate columns
    expected_columns = numerical_features + ['risk_tolerance', 'recommended_watch']
    missing_columns = [col for col in expected_columns if col not in df_ml.columns]
    if missing_columns:
        st.error(f"Missing columns in the dataset: {missing_columns}")
        st.stop()

    # Train KNN model
    X = df_ml[['income', 'investment_amount', 'age', 'risk_tolerance']]
    y = df_ml['recommended_watch']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    try:
        knn.fit(X_train, y_train)
    except ValueError as e:
        st.error(f"Error in training the model: {e}")
        st.stop()

    # Streamlit app UI for Page 1
    st.title("Investment Watch Recommendation")

    # Collect user inputs through sliders and a dropdown
    income = st.slider("Enter your income:", min_value=0, max_value=250000, step=1000)
    investment_amount = st.slider("Enter your investment amount:", min_value=0, max_value=2500, step=100)
    age = st.slider("Enter your age:", min_value=18, max_value=100, step=1)
    risk_tolerance = st.selectbox("Select your risk tolerance:", ["Low", "Moderate", "High"])

    # Convert the risk tolerance input (text) into a numeric value
    risk_encoded = label_encoders['risk_tolerance'].transform([risk_tolerance])[0]

    # Fetch exchange rates (this is where we utilize the centralized API)
    exchange_rates = fetch_exchange_rates()
    if not exchange_rates:
        st.warning("Unable to fetch exchange rates. Currency conversion may not work on later pages.")

    # Button for prediction
    if st.button("Recommend Watch"):
        try:
            # Prepare the user's input for prediction
            user_input = scaler.transform([[income, investment_amount, age]])[0]
            user_input = list(user_input) + [risk_encoded]

            # Predict the best watch for the user
            predicted_label = knn.predict([user_input])
            recommended_watch = label_encoders['recommended_watch'].inverse_transform(predicted_label)[0]

            # Save the recommended watch in the session state
            st.session_state['recommended_watch'] = recommended_watch
            st.success(f"Recommended Watch: {recommended_watch}")
            st.info("Proceed to Page 2 to see detailed recommendations.")
        except ValueError as e:
            st.error(f"Error in making prediction: {e}")
