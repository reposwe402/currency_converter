from api import fetch_exchange_rates


def convert_currency(amount, from_currency, to_currency):
    """Converts the given amount from one currency to another using the latest exchange rates."""
    rates = fetch_exchange_rates()
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in rates or to_currency not in rates:
        raise KeyError("Invalid currency code")
    converted_amount = round(amount * rates[to_currency] / rates[from_currency], 2)
    return converted_amount
