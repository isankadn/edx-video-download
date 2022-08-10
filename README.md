<p>This is a simple script to download edx.org video files.</p>
# instalation

<p>This needs Python 3.</p>
<p>
<code>
git clone https://github.com/isankadn/edx-video-download.git
</code>
</p>

<p>Install necessary packages by running </p>
<p>
<code>
  pip install -r requirements.txt
</code>
</p>
<p>
First, log in to studio.edx.org  and go to video uploads and download the video list CSV.
Then copy the path of the downloaded CSV file.</p> 

<p>example:</p> 
<p>
<code>/Users/isanka/dev/edv-video-download/009x_video_urls.csv</code>
</p>
<p>Run the script by;</p>
<p>
<code>python edx_video_backup.py</code>
</p>
