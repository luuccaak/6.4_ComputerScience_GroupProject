import requests
import streamlit as st

# API Configuration
API_KEY = "fca_live_CW46O05GyDUgIlulb3axvPjG8gPeOGjlUJosY7GO"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

def fetch_exchange_rates(base_currency="USD"):
    """
    Fetch exchange rates from the API.

    Args:
        base_currency (str): The base currency for exchange rates. Default is "USD".

    Returns:
        dict: A dictionary of exchange rates or None if an error occurs.
    """
    if "exchange_rates" in st.session_state and st.session_state["base_currency"] == base_currency:
        # Return cached rates if already fetched
        return st.session_state["exchange_rates"]
    
    params = {
        "apikey": API_KEY,
        "base_currency": base_currency
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json().get("data", {})
            # Cache the exchange rates in session state
            st.session_state["exchange_rates"] = data
            st.session_state["base_currency"] = base_currency
            return data
        else:
            st.error(f"Error fetching exchange rates: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching exchange rates: {e}")
        return None
