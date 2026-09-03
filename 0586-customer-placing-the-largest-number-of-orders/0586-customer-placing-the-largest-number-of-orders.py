import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number').size()

    maxi = result.max()

    result = result[result == maxi].reset_index(name='order_number')

    return result[['customer_number']]