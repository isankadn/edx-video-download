
"""
@Author: Isanka Wijerathne
@Date: 2022 August 10

Install necessary packages by running pip install -r requirements.txt
This is a simple script to download edx.org video files.
First, log in to studio.edx.org  and go to video uploads and download the video list CSV.
Then copy the path of the downloaded CSV file. example: /Users/isanka/dev/edv-video-download/009x_video_urls.csv
Run the script by "python edx_video_backup.py"

"""
    
import pandas as pd
import wget


DOWNLOAD_LOCATION = "./downloads"

csv_path = input("What is the video url CSV path? Ex: '/home/isanka/009x_video_urls.csv' ").strip()

fields = ['Name', 'Status', 'desktop_mp4 URL',]
df = pd.read_csv(csv_path, skipinitialspace=True, usecols=fields)

df = df.reset_index()
c = 0
for index, row in df.iterrows():
    url = row["desktop_mp4 URL"]
    if row['Status'] == "Ready":   
        wget.download(url, out = DOWNLOAD_LOCATION)
        c += 1
        
print(str(c) + " video files downloaded!")
    

  
   