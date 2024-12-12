import streamlit as st
import requests

# Function to fetch exchange rates
API_KEY = "fca_live_CW46O05GyDUgIlulb3axvPjG8gPeOGjlUJosY7GO"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

# This function interacts with the Free Currency API to fetch live exchange rates for the base currency.
def fetch_exchange_rates(base_currency="USD"):
    """Fetch exchange rates from the API."""
    params = {
        "apikey": API_KEY,  # Provides API authentication
        "base_currency": base_currency  # Base currency to convert from
    }
    response = requests.get(BASE_URL, params=params)  # Makes the API request
    if response.status_code == 200:  # If the API call succeeds
        data = response.json()  # Convert the response to JSON format
        return data.get("data", {})  # Extracts the actual exchange rate data
    else:  # If the API call fails
        st.error(f"Error fetching exchange rates: {response.status_code}")  # Displays the error in the Streamlit app
        return None  # Stops further calculations if the API call fails

# Fetch the exchange rates at the start of the app to ensure data availability
exchange_rates = fetch_exchange_rates()
if not exchange_rates:  # If exchange rates could not be fetched, the app stops
    st.stop()

# This function provides an investment calculator based on the selected watch's price and user inputs.
def investment_calculator():
    st.title("Investment Calculator")  # Title for the investment calculator page

    # Ensure a watch is selected in session state
    if 'selected_watch' not in st.session_state or st.session_state['selected_watch'] is None:
        st.warning("No watch selected. Please go back and select a watch.")  # Warn if no watch is selected
        st.stop()  # Stop further execution

    # Get details of the selected watch
    watch = st.session_state['selected_watch']  # Load the selected watch's details

    # Fetch exchange rates again to ensure up-to-date conversion
    if 'selected_currency' not in st.session_state:
        st.session_state['selected_currency'] = "USD"  # Default to USD if no currency selected
    selected_currency = st.session_state['selected_currency']  # Retrieve the selected currency
    exchange_rates = fetch_exchange_rates("USD")  # Fetch rates with USD as the base currency
    exchange_rate = exchange_rates.get(selected_currency, 1.0)  # Get the rate for the selected currency, defaulting to 1.0

    # Define the maximum investment based on the price of the watch
    max_investment = watch['Price']# The watch's price sets the upper limit for investment

    # Display details about the selected watch
    st.subheader(f"Investment Options for {watch['recommended_watch']}")  # Subheader for investment options
    st.write(f"**Brand:** {watch['brand']}")  # Display the brand of the watch
    st.write(f"**Price (USD):** {watch['Price']:,} USD")  # Show the price in USD
    if selected_currency != "USD":  # If a currency other than USD is selected
        converted_price = watch['Price'] * exchange_rate  # Convert the price
        st.write(f"**Price ({selected_currency}):** {converted_price:,.0f} {selected_currency}")  # Display the converted price

   # Collect user inputs for investment calculation
    investment_amount = st.slider(
        f"Select your investment amount (USD)",
        min_value=100,  # Minimum investment is 100 in the selected currency
        max_value=int(max_investment),  # Maximum investment is the watch's price
        value=int(watch['Price']),  # Default value is the watch's converted price
        step=100  # Allow users to adjust in steps of 100
    )

    time_horizon = st.slider(
        "Select time horizon (years):", min_value=1, max_value=20, value=5
    )  # Time horizon for investment in years

    scenario = st.radio(
        "Select ROI scenario:",
        ["Defensive scenario (2%)", "Expected scenario (4%)", "Ambitious scenario (8%)"]
    )  # Choose between conservative, expected, or ambitious ROI scenarios

    rate_of_return = {  # Map scenarios to specific ROI percentages
        "Defensive scenario (2%)": 0.02,
        "Expected scenario (4%)": 0.04,
        "Ambitious scenario (8%)": 0.08
    }[scenario]

    # Perform investment calculations
    expected_value = investment_amount * (1 + rate_of_return) ** time_horizon  # Future value calculation
    platform_fees = 0.02 * investment_amount  # fees calculation
    net_return = expected_value - investment_amount - platform_fees  # Net return calculation
    net_return_percentage = (net_return / investment_amount) * 100  # Calculate return as a percentage

    # Display calculated results
    st.markdown("### Investment Results")  # Subheader for results
    st.write(f"- **Investment amount:** {investment_amount:,.2f} USD")  # Show investment amount
    st.write(f"**Expected value after {time_horizon} years:** {expected_value:,.0f} USD")  # Display expected future value
    st.write(f"- **ROI scenario:** {scenario}")  # Display selected ROI scenario
    st.write(f"**Net return:** {net_return:,.2f} USD ({net_return_percentage:.2f}%)")  # Show net return and percentage
    st.write(f"**Platform fees:** {platform_fees:,.2f} USD")  # Display platform fees
    
    


    # Add navigation buttons
    col1, col2 = st.columns(2)  # Create two columns for buttons
    with col1:
        if st.button("Back to Watch Details"):  # Button to navigate back
            st.session_state['page'] = 'Watch Details'  # Change page to Watch Details
            st.rerun()  # Refresh the app




# 	•	Sources:
# 	•	Original Code: The investment calculator logic is custom-built to suit the requirements of the app based on the theory from following website: https://www.w3schools.com/python/python_functions.asp
# 	•	Python Documentation: Mathematical functions and data manipulation methods were guided by Python’s official documentation: https://docs.python.org/3/library/functions.html
# 	•	StackOverflow: Solutions to common issues, such as handling decimal precision and real-time data updates, were adapted from discussions on StackOverflow: https://stackoverflow.com/questions/52517487/python-investment-calculator
# 	•	ChatGPT: ChatGPT provided suggestions for optimizing calculations and improving the user experience.
