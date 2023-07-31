import argparse
from pytube import YouTube

# By Fernando Da Silva - July 31st, 2023

def download_youtube_video(url, output_path=None):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)

        # Get the highest resolution stream available (for MP4 format)
        video_stream = yt.streams.filter(file_extension='mp4').first()

        if not video_stream:
            print("No MP4 format available for this video.")
            return

        # Set the output path and filename
        output_filename = video_stream.default_filename
        output_file = output_filename if not output_path else f"{output_path}/{output_filename}"

        # Download the video
        print(f"Downloading video: {output_filename}...")
        video_stream.download(output_path=output_path)
        print("Download complete!")

    except Exception as e:
        print("Error occurred while downloading:", str(e))

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Download a YouTube video as MP4.")
    parser.add_argument("youtube_url", help="URL of the YouTube video to download")
    parser.add_argument("-o", "--output", help="Output path to save the downloaded video")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the download function with the provided URL and output path
    download_youtube_video(args.youtube_url, args.output)
