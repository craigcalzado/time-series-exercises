import pandas as pd


def trinity_prep(df):
    ''' This function takes in the trinity(sale, items, stores) dataframe and returns a dataframe with the following changes: 'sale_date' column is converted to datetime format, 'month' and 'day_of_week' columns are added, and 'sales_total' column is added. '''
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df.set_index('sale_date', inplace=True)
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name() 
    df['sales_total'] = df['sale_amount'] * df['item_price']
    return df
#-------------------------------------------------------------------------------
def opsd_prep(df):
    ''' This function takes in the opsd_germany_daily dataframe and returns a dataframe with the following changes: 
    'Date' column is converted to datetime format, 'month' and 'year' columns are added, and 'Wind+Solar' column is added.
    '''
    df.reset_index(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    df['Wind+Solar'] = df['Wind'] + df['Solar']
    return df