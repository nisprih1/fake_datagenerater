import pandas as pd
from faker import Faker
import random
import time

fake = Faker()
Faker.seed(101)
random.seed(101)


def generate_orders_csv(user_file='5M_user_data.csv', output_file='orders.csv', total_orders=100000):
    start_time = time.time()

    #Load user IDs from existing file
    user_ids = pd.read_csv(user_file, usecols=['id'])['id'].tolist()
    print(f"Loaded {len(user_ids)} user IDs.")

    orders = []

    for order_id in range(1, total_orders + 1):
        order = {
            'order_id': order_id,
            'user_id': random.choice(user_ids),
            'order_date': fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d'),
            'total_amount': round(random.uniform(100, 10000), 2),
            'status': random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
        }
        orders.append(order)

    df = pd.DataFrame(orders)
    df.to_csv(output_file, index=False)

    print(f"\n Done: {total_orders} orders saved to '{output_file}' in {round(time.time() - start_time, 2)} seconds.")


if __name__ == "__main__":
    generate_orders_csv()