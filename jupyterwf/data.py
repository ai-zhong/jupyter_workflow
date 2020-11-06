from urllib.request import urlretrieve
import pandas as pd
import os


FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """
    Download and cache the fremont data
    
    Parameters
    ----------
    filename : string (default 'Fremont.csv', optional)
        location to save the data
    url : string (default inplace, optional)
        web location of the data
    force_download : bool (default False)
        if True, force redownload the data

    Returns
    --------
    data : pandas.DataFrame
        The fremont bridge bike count data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'Fremont.csv')
    
    # parse_dates took long here since we didn't specify datetime format
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except:
        data.index = pd.to_datetime(data.index)
    data.columns=['Total', 'East', 'West']
    
    return data
