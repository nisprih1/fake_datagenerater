from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(123)
random.seed(123)

def generate_products(n=1000, output_file="products.csv"):
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys', 'Sports', 'Grocery']
    products = []

    for i in range(1, n + 1):
        products.append({
            'product_id': i,
            'product_name': fake.word().capitalize() + " " + random.choice(['Pro', 'Plus', 'Max', 'Lite', 'X']),
            'category': random.choice(categories),
            'price': round(random.uniform(50, 5000), 2)
        })

    df = pd.DataFrame(products)
    df.to_csv(output_file, index=False)
    print(f" Generated {n} products in '{output_file}'")

if __name__ == "__main__":
    generate_products()