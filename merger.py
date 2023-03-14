from datetime import datetime, timedelta

def generate_bitcoin_urls(start_date, end_date):
    """
    Generates a list of download URLs for Bitcoin transaction TSV files
    from Blockchair between two specified dates.
    
    Args:
    - start_date (str): Start date in YYYY-MM-DD format.
    - end_date (str): End date in YYYY-MM-DD format.
    
    Returns:
    - A list of download URLs as strings.
    """
    base_url = "https://gz.blockchair.com/bitcoin/transactions/blockchair_bitcoin_transactions_{}.tsv.gz"

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    urls = []

    while current_date <= end_date:
        url = base_url.format(current_date.strftime("%Y%m%d")) # Format the URL with the current date
        urls.append(url) # Add the URL to the list
        current_date += timedelta(days=1) # Move on to the next date
    
    return urls
def merger(start_date, end_date):
  df = pd.DataFrame()
  csv_urls=generate_bitcoin_urls(start_date, end_date)
  # loop through the list of URLs and append the dataframes
  dfs = []

  for url in csv_urls:
      temp_df = pd.read_csv(url,sep='\t', compression='gzip')
      dfs.append(temp_df)
  df = pd.concat(dfs, ignore_index=True)
  return df

#start_date = "2012-01-01"
#end_date = "2012-01-02"
#urls = generate_bitcoin_urls(start_date, end_date)
#merger(start_date, end_date)
