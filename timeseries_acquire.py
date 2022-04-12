import pandas as pd
import requests
import os

# --------------------------------------------------------------------------------------------------------------
def acquire_df(item):
    ''' This function takes a string and returns a dataframe with a .cvs. From https://api.data.codeup.com '''
    # identify the base url
    base_line = 'https://api.data.codeup.com'
    # identify the primary endpoint
    api = '/api/v1/'
    # create the url
    url = base_line + api
    response = requests.get(url + item)
    data = response.json()
    # create a .csv file to store the data
    csv_name = (item + '.csv')
    # check if the .csv file exists
    if os.path.isfile(csv_name):
        print('File already exists')
        return pd.read_csv(item+'.csv', index_col=0)
    else:
        # create a variable to hold the list of data
        list = data['payload'][item]
        # check if url still has data to be acquired and add to list
        while data['payload']['next_page'] != None:
            response = requests.get(base_line + data['payload']['next_page'])
            data = response.json()
            list.extend(data['payload'][item])
        # turn list into a dataframe
        df = pd.DataFrame(list)
        # write dataframe to .csv file
        df.to_csv(item+'.csv')
    return df
#-------------------------------------------------------------------------------
def combine_data(df_sales, df_items, df_stores):
    '''` This function takes three dataframes and combines them into one dataframe. Cleaning it up aswell. '''
    df_sales.rename(columns={'item': 'item_id'}, inplace=True)
    df_sales_items = df_sales.merge(df_items, on='item_id')
    df_sales_items.rename(columns={'store': 'store_id'}, inplace=True)
    df_sales_items.drop(columns=['item_id'], inplace=True)
    df_trinity = df_sales_items.merge(df_stores, on='store_id')
    df_trinity.drop(columns=['store_id'], inplace=True)
    df_trinity.set_index('sale_id', inplace=True)
    return df_trinity
#-------------------------------------------------------------------------------
def acquire_opsd_germany_daily():
    ''' This function acquires the data from the https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv website and returns a dataframe. '''
    opsd_germany_daily = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv', index_col=0)
    opsd_germany_daily.to_csv('opsd_germany_daily.csv')
    return opsd_germany_daily