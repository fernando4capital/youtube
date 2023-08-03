# youtube
Youtube tools

1) download.py
   
    To download a YouTube video as an MP4 file in Python, you can use the pytube library.
    Before running the script, make sure you have installed the pytube library by running

 pip install pytube

    After that to download a file:

 python your_script_name.py "https://www.youtube.com/watch?v=your_youtube_video_id" -o /path/to/output/directory

    Replace your_script_name.py with the actual name of your Python script file, and https://www.youtube.com/watch?v=your_youtube_video_id with the YouTube URL you want to download. 

    You can include the -o option with a path if you want to specify a custom download location.

     If no output path is provided, the video will be downloaded in the current directory.
