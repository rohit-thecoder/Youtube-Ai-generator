import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY is missing!")


def get_youtube_trending_videos(topic="AI", region="US"):

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": topic,
        "type": "video",
        "regionCode": region,
        "order": "viewCount",
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }

    try:

        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        videos = []

        for item in data.get("items", []):

            video_id = item["id"]["videoId"]

            videos.append({
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })

        return videos

    except Exception as e:

        print(f"YouTube API Error: {e}")

        return []