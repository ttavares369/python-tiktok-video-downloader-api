import requests
import json

def get_video_link(video_url, rapidapi_key):
    # Get your FREE API key here: https://rapidapi.com/titavares33/api/social-media-video-downloader-no-watermark
    api_url = "https://social-media-video-downloader-no-watermark.p.rapidapi.com/api/v1/video"
    
    headers = {
        "x-rapidapi-host": "social-media-video-downloader-no-watermark.p.rapidapi.com",
        "x-rapidapi-key": rapidapi_key,
        "Content-Type": "application/json"
    }
    
    payload = {"url": video_url}
    
    print(f"Extracting video from: {video_url}")
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Success!")
        print(f"Title: {data.get('title')}")
        print(f"Download Link: {data.get('video_url')}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

# --- Usage Example ---
API_KEY = "YOUR_RAPIDAPI_KEY" # Replace with your RapidAPI key
TARGET_VIDEO = "https://www.tiktok.com/@tiktok/video/7106594312292453675"

get_video_link(TARGET_VIDEO, API_KEY)
