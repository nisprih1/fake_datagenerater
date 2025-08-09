# Fake Data Generator

A Python-based tool for generating large-scale synthetic datasets for testing, development, and analytics purposes.  
This project is ideal for data engineers, analysts, and developers who need realistic sample data without exposing sensitive information.

---

##  Features
- Generate **user**, **order**, and **product** datasets.
- Support for **large datasets** (millions of rows).
- Configurable data fields (names, dates, amounts, categories, etc.).
- Output in **CSV** or **Parquet** format.
- Customizable for specific business needs.

---

## Installation
```bash
git clone https://github.com/nisprih1/fake_datagenerater.git
cd fake_datagenerater
pip install -r requirements.txt
```

---

## Usage
Run the main script to generate datasets:
```bash
python generate_data.py --rows 5000000 --output users.csv
```

Example with orders:
```bash
python generate_data.py --rows 20000000 --output orders.csv
```

---

##  Configuration
You can modify the configuration in `config.json`:
```json
{
  "rows": 1000000,
  "format": "csv",
  "seed": 42
}
```

---

##  Example Output
- `users.csv` → User details (ID, name, email, location)
- `orders.csv` → Order details (order_id, user_id, amount, status, date)
- `products.csv` → Product catalog (product_id, name, category, price)
- `order_items.csv` → Product and order information (product_id, order_id, price_per_unit, total_amount, quantity)
---
