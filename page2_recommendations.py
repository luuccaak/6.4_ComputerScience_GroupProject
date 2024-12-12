import streamlit as st
from api import fetch_exchange_rates  # Import the centralized API logic

# Fetch exchange rates
exchange_rates = fetch_exchange_rates()
if not exchange_rates:
    st.stop()  # Stop if exchange rates are not fetched

# Currency Selection
st.subheader("Currency Selection")
selected_currency = st.selectbox("Select your currency:", ["USD"] + list(exchange_rates.keys()))

# Function to display watch recommendations
def recommend_watches():
    st.title("Recommendations")

    # Ensure the CSV dataset containing watch data is loaded
    if 'watches_data' not in st.session_state:
        st.error("Watch data not loaded. Please complete the questionnaire on Page 1.")
        return

    # Access the data stored in the session state
    df = st.session_state['watches_data']

    # Currency selection for dynamic pricing
    st.subheader("Currency Selection")
    if 'selected_currency' not in st.session_state:
        st.session_state['selected_currency'] = "USD"  # Default currency is USD
    selected_currency = st.selectbox(
        "Select your currency:",
        ["USD", "EUR", "CHF", "GBP", "JPY", "AUD"],
        index=["USD", "EUR", "CHF", "GBP", "JPY", "AUD"].index(st.session_state['selected_currency'])
    )
    st.session_state['selected_currency'] = selected_currency  # Store the selected currency in session state

    # Get exchange rate for the selected currency
    exchange_rate = exchange_rates.get(selected_currency, 1.0)

    # Ensure a recommended watch exists in the session state
    if 'recommended_watch' not in st.session_state:
        st.error("No recommendation available. Please complete the questionnaire on Page 1.")
        return

    # Display the recommended watch
    st.subheader("Based on your profile, we recommend:")
    recommended_watch_name = st.session_state['recommended_watch']
    recommended_watch = df[df['recommended_watch'] == recommended_watch_name].iloc[0]

    st.image(recommended_watch['link'], width=300)
    st.write(f"### {recommended_watch['recommended_watch']}")
    st.write(f"*Brand*: {recommended_watch['brand']}")
    st.write(f"**Price (USD):** {recommended_watch['Price']:,} USD")
    if selected_currency != "USD":
        converted_price = recommended_watch['Price'] * exchange_rate
        st.write(f"**Price ({selected_currency}):** {converted_price:,.0f} {selected_currency}")

    if st.button(f"Details for {recommended_watch['recommended_watch']}"):
        st.session_state['selected_watch'] = recommended_watch.to_dict()
        st.session_state['page'] = 'Watch Details'
        st.write("Redirecting to Watch Details...")
        st.rerun()

    st.write("---")

    # Explore all watches
    st.subheader("Explore All Watches")
    for _, watch in df.iterrows():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(watch['link'], width=100)
        with col2:
            st.write(f"### {watch['recommended_watch']}")
            st.write(f"*Brand*: {watch['brand']}")
            st.write(f"**Price (USD):** {watch['Price']:,} USD")
            if selected_currency != "USD":
                converted_price = watch['Price'] * exchange_rate
                st.write(f"**Price ({selected_currency}):** {converted_price:,.2f} {selected_currency}")
            if st.button(f"Details for {watch['recommended_watch']}", key=f"details_{watch['recommended_watch']}"):
                st.session_state['selected_watch'] = watch.to_dict()
                st.session_state['page'] = 'Watch Details'
                st.rerun()
        st.write("---")



#	•	Sources:
#	•	Original Code: The logic for generating watch recommendations is a custom implementation.
#	•	Streamlit Documentation: UI elements and user interaction patterns were adapted from the Streamlit documentation: https://docs.streamlit.io/get-started/fundamentals/main-concepts
#	•	StackOverflow: Problem-solving strategies for filtering data and presenting recommendations were inspired by related Q&A discussions on StackOverflow: https://stackoverflow.com/questions/38072334/how-to-start-machine-learning-with-python-programming
#       KNN source: https://scikit-learn.org/1.5/modules/neighbors.html
#	•	ChatGPT: ChatGPT was used to enhance readability, optimize code structure, and suggest additional functionality.
