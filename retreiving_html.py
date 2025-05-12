import os
import pandas as pd
import requests
import time
from fake_useragent import UserAgent

# Specify directory
directory_name = "HTML Files"


# Specify path
path = f'{directory_name}'

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if (not isExist):
    # Create the directory if folder doesn't exists
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Creating pandas dataframe for the mental_wellness_articles csv file
df = pd.read_csv('mental_wellness_articles.csv')
data = []
for _, row in df.iterrows():
    topic = row[0]
    urls = [url for url in row[1:] if url != '']
    data.append({"Topic": topic, "URLs": urls})

result_df = pd.DataFrame(data)

# print(result_df)
# desired_row = result_df[result_df['Topic'] == "Anxiety"].iloc[0]
# print(desired_row[1])

# Creating folders for individual topics
topics = result_df['Topic']


# Creating session for copying data from web to html files

session = requests.Session()

headers = {
    'User-Agent': UserAgent().random,
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com'
}

proxy_list = [
    "137.184.174.32:4857",
    "143.42.66.91:80",
    "34.143.143.61:7777",
    "3.110.60.103:80",
    "99.79.124.70:80"
]

proxies = {
    'http': f'http://{proxy_list[2]}',
    'https': f'http://{proxy_list[2]}'
}

time.sleep(2)  # Respectful delay

for topic in topics:
    # Create folder for each topic
    # Specify directory
    directory_name = topic

    # Specify path
    path = f'HTML Files/{directory_name}'

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if (not isExist):
        # Create the directory if folder doesn't exists
        try:
            os.mkdir(path)
            print(f"Directory '{directory_name}' created successfully.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{directory_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Get the row for the current topic
    desired_row = result_df[result_df['Topic'] == topic].iloc[0]
    urls = desired_row[1]
    i = 0
    for url in urls:

        if pd.isna(url):  # Skip if URL is NaN/empty
            continue

        # Extract domain name for filename
        clean_url = url.replace(
            'https://', '').replace('http://', '').replace('www.', '')
        domain = clean_url.split('.')[0]

        try:
            filePath = f"HTML Files/{topic}/{i+1:02d}_{domain}.html"
            isFileExist = os.path.isfile(filePath)

            if (not isFileExist):
                time.sleep(2)  # Respectful delay
                r = session.get(url, proxies=proxies,
                                headers=headers, verify=False)
                r.raise_for_status()  # Raise exception for bad status codes
                # Save file with sequential numbering and domain name
                with open(filePath, 'w', encoding='utf-8') as f:
                    f.write(r.text)

            i = i+1

        except Exception as e:
            print(f"Failed to fetch {url}: {str(e)}")
