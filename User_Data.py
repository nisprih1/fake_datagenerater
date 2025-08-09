from faker import Faker
import pandas as pd
import random
import time

fake = Faker('en_IN')
Faker.seed(42)
random.seed(42)

def user(user_id):
    return {
        'id': user_id,
        'name' : fake.name(),
        'email' : fake.email(),
        'gender' : random.choice(['Male','Female']),
        'dob' : fake.date_of_birth(minimum_age=18,maximum_age=90).strftime('%Y-%m-%d'),
        'country' : fake.country(),
        'is_active' : random.choice([True,False])
    }

def generate_user_save_csv(total_record = 5000000,batch_size =100000, output_file="5M_user_data.csv"):
    start_time = time.time()
    with open(output_file, "w", encoding="utf-8") as f:
        columns = ['id','name','email','gender','dob','country','is_active']
        f.write(','.join(columns) + "\n")

        for i in range(0,total_record,batch_size):
            batch= [user(user_id) for user_id in range(i+1,i+batch_size+1)]
            df = pd.DataFrame(batch)
            df.to_csv(f,header=False,index=False)
            print(f" Saved {i+batch_size}")

        print(f"Done Total Time : {round(time.time() - start_time, 2)} seconds")


if __name__ == "__main__":
    generate_user_save_csv()