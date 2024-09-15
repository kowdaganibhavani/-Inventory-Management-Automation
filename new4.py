import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Sample inventory data
data = {
    'item': ['Widget A', 'Widget B', 'Widget C'],
    'current_stock': [100, 50, 10],
    'average_daily_sales': [5, 3, 8],
    'reorder_point': [20, 15, 5]  
}


invent = pd.DataFrame(data)


def predict(item_stock, daily_sales_rate, days_to_predict=7):
    return item_stock - daily_sales_rate * days_to_predict

def check(item_stock, reorder_point):
    return item_stock <= reorder_point

def update(invent):
    for index, row in invent.iterrows():
        predstock = predict(row['current_stock'], row['average_daily_sales'])
        
        print(f"Item: {row['item']}")
        print(f"Current Stock: {row['current_stock']}")
        print(f"Predicted Stock in 7 Days: {predstock}")
        
        if check(row['current_stock'], row['reorder_point']):
            print(f"Reorder {row['item']}")

update(invent)

plt.figure(figsize=(10, 6))
plt.bar(invent['item'], invent['current_stock'], color='skyblue')
plt.axhline(y=invent['reorder_point'].mean(), color='r', linestyle='--', label='Average Reorder Point')
plt.xlabel('Item')
plt.ylabel('Current Stock Level')
plt.title('Current Inventory Levels')
plt.legend()
plt.show()
