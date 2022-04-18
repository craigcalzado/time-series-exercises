import pandas as pd
from sklearn.model_selection import train_test_split


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
    df['Wind'].fillna(0, inplace=True)
    df['Solar'].fillna(0, inplace=True)
    df['Wind+Solar'] = df['Wind'] + df['Solar']
    return df
#-------------------------------------------------------------------------------
def split_dataframe(df):
   train, test = train_test_split(df, test_size=0.2, random_state=789, stratify=df['index'])
   train, validate = train_test_split(train, test_size=0.3, random_state=789, stratify=train['index'])
   return train, validate, test 