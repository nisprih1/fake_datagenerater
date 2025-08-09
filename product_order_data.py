import pandas as pd
import random
import time

def generate_order_items(orders_file='orders.csv',
                         products_file='products.csv',
                         output_file='order_items.csv'):
    start_time = time.time()

    # Load orders and products
    orders_df = pd.read_csv(orders_file, usecols=['order_id'])
    products_df = pd.read_csv(products_file)
    product_list = products_df.to_dict(orient='records')
    print(f"Loaded {len(orders_df)} orders and {len(product_list)} products.")

    all_items = []

    for _, row in orders_df.iterrows():
        order_id = row['order_id']
        num_items = random.randint(1, 3)
        selected_products = random.sample(product_list, num_items)

        for product in selected_products:
            quantity = random.randint(1, 5)
            price = product['price']
            total = round(price * quantity, 2)

            all_items.append({
                'order_id': order_id,
                'product_id': product['product_id'],
                'quantity': quantity,
                'price_per_unit': price,
                'total_price': total
            })

    df_items = pd.DataFrame(all_items)
    df_items.to_csv(output_file, index=False)
    print(f"\n Generated {len(df_items)} order items in '{output_file}'")
    print(f" Time taken: {round(time.time() - start_time, 2)} seconds.")

if __name__ == "__main__":
    generate_order_items()
