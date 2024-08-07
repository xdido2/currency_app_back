import pandas as pd

# Define the data
data = {
    "currency_code": ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR", "MXN", "BRL", "SEK", "NZD", "SGD", "HUF", "KRW", "TRY", "ZAR", "PHP", "MYR", "PLN"],
    "currency_name": ["US Dollar", "Euro", "British Pound", "Japanese Yen", "Australian Dollar", "Canadian Dollar", "Swiss Franc", "Chinese Yuan", "Indian Rupee", "Mexican Peso", "Brazilian Real", "Swedish Krona", "New Zealand Dollar", "Singapore Dollar", "Hungarian Forint", "South Korean Won", "Turkish Lira", "South African Rand", "Philippine Peso", "Malaysian Ringgit", "Polish Zloty"],
    "symbol": ["$", "€", "£", "¥", "A$", "C$", "CHF", "¥", "₹", "$", "R$", "kr", "$", "S$", "Ft", "₩", "₺", "R", "₱", "RM", "zł"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the file path
file_path = 'currencies.csv'

# Write DataFrame to CSV
df.to_csv(file_path, index=False)

print(f"CSV file '{file_path}' has been created successfully.")
