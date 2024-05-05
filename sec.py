from sec_api import QueryApi
import pandas as pd
import os
import requests

API_KEY = '53dd7d57fd9d62f68d231732991775a4d0c590c78fdf5e4a4d6faf69bea2a472'
PDF_GENERATOR_API = 'https://api.sec-api.io/filing-reader'

queryApi = QueryApi(api_key=API_KEY)

def standardize_filing_url(url):
    return url.replace('ix?doc=/', '')

def get_10K_metadata(start_year=2023, end_year=2024):
    frames = []

    for year in range(start_year, end_year + 1):
        form_type_filter = 'formType:"10-K" AND NOT formType:("10-K/A", NT)'
        ticker_filter = 'ticker:"GOOG"'
        lucene_query = f'{form_type_filter} AND {ticker_filter} AND filedAt:[{year}-01-01 TO {year}-12-31]'

        query_from = 0
        query_size = 200

        while True:
            query = {
                "query": lucene_query,
                "from": query_from,
                "size": query_size,
                "sort": [{"filedAt": {"order": "desc"}}]
            }

            response = queryApi.get_filings(query)
            filings = response['filings']

            if len(filings) == 0:
                break
            else:
                query_from += query_size

            metadata = list(map(lambda f: {'ticker': f['ticker'],
                                           'cik': f['cik'],
                                           'formType': f['formType'],
                                           'filedAt': f['filedAt'],
                                           'filingUrl': f['linkToFilingDetails']
                                           }, filings))

            df = pd.DataFrame.from_records(metadata)
            df['filingUrl'] = df['filingUrl'].apply(standardize_filing_url)
            frames.append(df)

    result = pd.concat(frames)
    print(f'✅ Download completed. Metadata downloaded for {len(result)} filings.')
    return result

metadata_10K = get_10K_metadata()

def download_pdf(metadata):
    ticker = metadata['ticker']
    filing_url = metadata['filingUrl']
    try:
        new_folder = './filings/' + ticker
        date = metadata['filedAt'][:10]
        file_name = date + '_' + metadata['formType'] + '_' + filing_url.split('/')[-1] + '.pdf'
        
        if not os.path.isdir(new_folder):
            os.makedirs(new_folder)

        api_url = f"{PDF_GENERATOR_API}?token={API_KEY}&type=pdf&url={filing_url}"
        response = requests.get(api_url, stream=True)
        response.raise_for_status()

        with open(os.path.join(new_folder, file_name), "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except Exception as e:
        print(f"❌ {ticker}: download failed: {filing_url}. Error: {str(e)}")

google_filings = metadata_10K[metadata_10K['ticker'] == 'GOOG']
google_filings.apply(download_pdf, axis=1)

print('✅ Download completed')
