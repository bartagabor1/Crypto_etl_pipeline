# crypto_etl_pipeline (CoinGecko API)

This project demonstrates a simple ETL (Extract – Transform – Load) pipeline using Python.  
It pulls hourly cryptocurrency price data (Bitcoin) from the CoinGecko API, processes and cleans it using Pandas, and stores it in a local SQLite database.

---

## 📌 Project Structure
crypto_etl_pipeline/

├── crypto_etl.py # Main Python script (ETL logic)

├── crypto.db # Output SQLite database

├── requirements.txt # Python package dependencies

└── README.md # Project overview (this file)

---

## 🔧 Technologies Used

- **Python 3**
- `requests` – for calling the CoinGecko API
- `pandas` – for data transformation
- `sqlalchemy` – to save data to SQLite database
- `sqlite3` – as the database engine (no external setup needed)

- ---

## 📈 What It Does

### ✅ 1. **Extract**
Fetches hourly price data for Bitcoin over the last 7 days via the [CoinGecko API](https://www.coingecko.com/en/api/documentation).

### ✅ 2. **Transform**
- Converts UNIX timestamps to datetime
- Rounds price values
- Removes duplicates and invalid data

### ✅ 3. **Load**
Saves the cleaned data into a local SQLite database (`crypto.db`, table: `prices`).

### ✅ 4. **Analyze** *(optional)*
Performs a basic price summary:
- Average price
- Minimum and maximum values

---

## ▶️ How to Run

### Step 1 – Clone the repository

```bash
git clone https://github.com/yourusername/crypto_etl_pipeline.git
cd crypto_etl_pipeline

### Step 2 – Install dependencies
bash
Másolás
Szerkesztés
pip install -r requirements.txt
Step 3 – Run the ETL script
bash
Másolás
Szerkesztés
python crypto_etl.py
After execution, you’ll find a crypto.db SQLite file with the prices table inside.

🗃 Example Output
timestamp	price (USD)
2025-07-01 12:00:00	62034.12
2025-07-01 13:00:00	62120.87
...	...

📊 Next Steps
Replace bitcoin with other coins (e.g. ethereum)

Extend to multiple coins at once

Build a dashboard using Power BI or Plotly

Connect to a MySQL database instead of SQLite

💡 Why This Project?
This beginner-friendly ETL pipeline is a great foundation for aspiring data engineers or analysts.
It combines real-world data, automation, and clean data storage — all in under 100 lines of Python.

✅ Author
Created by [Your Name]
💼 Fiverr profile: fiverr.com/yourusername
📬 Contact: your@email.com

yaml
Másolás
Szerkesztés

---

## 📥 Következő lépések

1. Mentsd ezt `README.md` néven a projekt mappádba
2. Készíts `.gitignore` fájlt, hogy a `crypto.db` ne kerüljön föl (ha nem akarod)
3. Töltsd fel GitHub-ra:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - crypto ETL pipeline"
   git remote add origin https://github.com/yourusername/crypto_etl_pipeline.git
   git push -u origin main
