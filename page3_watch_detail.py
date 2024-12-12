import streamlit as st
import matplotlib.pyplot as plt
import requests #The requests library allows your Python program to communicate with the API :



# Function to fetch exchange rates
API_KEY = "fca_live_CW46O05GyDUgIlulb3axvPjG8gPeOGjlUJosY7GO"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

# This function communicates with an external API to fetch live exchange rates for the selected base currency.
def fetch_exchange_rates(base_currency="USD"):
    """Fetch exchange rates from the API."""
    params = {
        "apikey": API_KEY,  # API key for authentication with the currency API
        "base_currency": base_currency  # Specifies the base currency (e.g., USD)
    }
    response = requests.get(BASE_URL, params=params)  # Sends the request to the API
    if response.status_code == 200:  # Checks if the API request was successful
        data = response.json()  # Parses the response into JSON format
        return data.get("data", {})  # Retrieves the dictionary of exchange rates
    else:  # Handles errors if the request fails
        st.error(f"Error fetching exchange rates: {response.status_code}")
        return None  # Returns None if there is an issue with the API request

# Fetch exchange rates to ensure data is available for currency conversion
exchange_rates = fetch_exchange_rates()
if not exchange_rates:  # If fetching fails, stop execution
    st.stop()

# This function displays the details of a selected watch, including price and its history.
def watch_detail():
    # Checks if a watch has been selected from the previous page
    if 'selected_watch' not in st.session_state or st.session_state['selected_watch'] is None:
        st.warning("No watch selected. Please go back and choose a watch.")  # Displays a warning if no watch is selected
        st.stop()  # Stops further execution

    # Loads details of the selected watch from the session state
    watch = st.session_state['selected_watch']

    # Ensure the currency selection is stored in session state
    if 'selected_currency' not in st.session_state:
        st.session_state['selected_currency'] = "USD"  # Defaults to USD
    selected_currency = st.session_state['selected_currency']  # Retrieves the selected currency
    exchange_rates = fetch_exchange_rates("USD")  # Fetches the exchange rates for USD as base
    exchange_rate = exchange_rates.get(selected_currency, 1.0)  # Retrieves the exchange rate for the selected currency

    # Displays the watch details with title and image
    st.title(f"Details for {watch['recommended_watch']}")  # Displays the title with the watch name
    st.image(watch["link"], width=300)  # Displays the watch image

    # Displays the brand and price information
    st.write(f"**Brand:** {watch['brand']}")  # Shows the brand of the watch
    st.write(f"**Price (USD):** {watch['Price']:,} USD")  # Shows the price in USD format
    if selected_currency != "USD":  # If a currency other than USD is selected, convert the price
        converted_price = watch['Price'] * exchange_rate  # Performs the currency conversion
        st.write(f"**Price ({selected_currency}):** {converted_price:,.0f} {selected_currency}")  # Displays the converted price

    # Displays the description of the watch, if available
    if 'description' in watch and watch['description']:  # Checks if the description exists
        st.write(f"**Description:** {watch['description']}")  # Displays the watch's description
    else:
        st.write("No description available for this watch.")  # Placeholder if no description is provided

    # Shows the price history of the watch, if available
    price_columns = ['2020', '2021', '2022', '2023', '2024']  # Columns representing historical prices
    price_history = [float(watch[year]) for year in price_columns if year in watch]  # Extracts price data for the years

    if price_history:  # If price history exists
        st.subheader("Price Fluctuations Over Time")  # Subheader for the price history section

        # Prepare years and prices for plotting
        years = list(map(int, price_columns))  # Converts column names to integers for plotting

        # Create a line plot of the price history
        plt.figure(figsize=(10, 4))  # Set the size of the plot
        plt.plot(
            years,
            price_history,
            marker='o',  # Marks data points with circles
            linestyle='-',  # Connects points with lines
            label="Price History"  # Adds a legend for the plot
        )
        plt.xticks(years)  # Ensures the x-axis shows only the specified years
        plt.xlabel("Year")  # Labels the x-axis as 'Year'
        plt.ylabel(f"Price ({selected_currency})")  # Labels the y-axis with the selected currency
        plt.title(f"Price Changes for {watch['recommended_watch']}")  # Adds a title to the plot
        plt.legend()  # Displays the legend
        st.pyplot(plt)  # Renders the plot in the Streamlit app
    else:  # If no price history exists, show an info message
        st.info("No price history available for this watch.")

    # Adds a button to navigate to the Investment Calculator page
    if st.button("Proceed to Investment Calculator"):
        st.session_state['page'] = 'Investment Calculator'  # Updates the page to Investment Calculator
        st.rerun()  # Refreshes the app to load the new page

    # Adds a button to return to the Recommendations page
    if st.button("Back to Recommendations"):
        st.session_state['page'] = 'Recommendations'  # Updates the page to Recommendations
        st.rerun()  # Refreshes the app to load the new page




	# •	Sources:
	# •	GitHub Repositories: Techniques for modularizing Streamlit apps and managing navigation between pages were inspired by projects shared on GitHub: https://github.com/python
	# •	Original Implementation: The specific logic for displaying watch details was independently developed for this project.
	# •	ChatGPT: ChatGPT was consulted for code refactoring and ensuring consistent page transitions across the application.
