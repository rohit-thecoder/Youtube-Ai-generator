from fastapi import FastAPI, Query
from google_trends import get_trending_keywords
from youtube_trends import get_youtube_trending_videos
from langchain_mistralai import ChatMistralAI
import os
from dotenv import load_dotenv


app = FastAPI()

@app.get("/generate_ideas/")

def generate_video_ideas(
    topic: str = Query(...,title="Topic"),
    audience: str =Query("Beginners", title="Target Audiance"),
    region: str = Query("US", title="Region")
):
    trending_keywords = get_trending_keywords(topic)

    if not trending_keywords:
        trending_keywords = [topic]

    trending_videos = get_youtube_trending_videos(topic, region) 

    if not trending_videos :
        [{"title": "No Trending video found","url": "#"}]   

    prompt = f"""
Generate 5 engaging YouTube video ideas on '{topic}'
for '{audience}' using the research below.

Trending keywords:
{', '.join(trending_keywords)}

Popular YouTube videos:
{', '.join([video["title"] for video in trending_videos])}

For each of the 5 ideas provide:

TITLE:
A compelling YouTube title.

HOOK:
A strong opening hook.

CONCEPT:
Explain what the video should cover.

WHY IT WORKS:
Explain why this topic is relevant.

FORMAT:
Suggest the video format.

IMPORTANT OUTPUT RULES:
- Do not use Markdown headings.
- Do not use ###.
- Do not use HTML.
- Do not add links.
- Keep the formatting clean and readable.
- Number the ideas from 1 to 5.
"""
    load_dotenv()

    llm = ChatMistralAI(
        model="codestral-2508",
        api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0
    )

    try:
        response = llm.invoke(prompt)

        ideas = response.content.strip()

    except Exception as e:
        ideas = f"Mistral API Error: {str(e)}"


    return {
        "trending_keywords": trending_keywords,
        "trending_videos": trending_videos,
        "ideas": ideas
    }       