# 📦 Import libraries
import requests                 # For API requests
import pandas as pd            # For data processing
from sqlalchemy import create_engine  # For database interaction
from datetime import datetime

# 🟩 1. EXTRACT: Fetch cryptocurrency price data from CoinGecko API
def extract_crypto_data(coin='bitcoin', currency='usd'):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {
        'vs_currency': currency,
        'days': '7',       # Last 7 days
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ API error:", response.status_code)
        print("⚠️ Response text:", response.text)
        return pd.DataFrame()  # üres DataFrame-et ad vissza

    data = response.json()

    if 'prices' not in data:
        print("❌ 'prices' key not found in response.")
        print("📦 Full response:", data)
        return pd.DataFrame()

    # Convert to DataFrame
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df


# 🟨 2. TRANSFORM: Clean and format the data
def transform_data(df):
    df = df.copy()
    df['price'] = df['price'].round(2)
    df = df.drop_duplicates()
    df = df[df['price'] > 0]
    return df


# 🟦 3. LOAD: Save the cleaned data into a local SQLite database
def load_to_sqlite(df, db_name='crypto.db', table_name='prices'):
    engine = create_engine(f"sqlite:///{db_name}")
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


# 🧪 Optional: Perform basic data analysis
def basic_analysis(df):
    print("🔹 Average price:", df['price'].mean())
    print("🔹 Highest price:", df['price'].max())
    print("🔹 Lowest price:", df['price'].min())


# 🚀 Main execution sequence
if __name__ == "__main__":
    print("🔍 Fetching data from API...")
    df_raw = extract_crypto_data()

    print("🧹 Cleaning data...")
    df_clean = transform_data(df_raw)

    print("💾 Saving to database (crypto.db)...")
    load_to_sqlite(df_clean)

    print("📊 Basic analysis:")
    basic_analysis(df_clean)

    print("✅ ETL pipeline completed successfully!")
