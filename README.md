<p>This is a simple script to download edx.org video files.</p>
# instalation
<code>
git clone https://github.com/isankadn/edx-video-download.git
</code>

<p>Install necessary packages by running </p>
<code>
  pip install -r requirements.txt
</code>
 
<p>
First, log in to studio.edx.org  and go to video uploads and download the video list CSV.
Then copy the path of the downloaded CSV file.</p> 
example: <code>/Users/isanka/dev/edv-video-download/009x_video_urls.csv</code>
Run the script by 
<code>python edx_video_backup.py</code>
