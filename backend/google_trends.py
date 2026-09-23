import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise ValueError("SERPAPI_KEY is missing!")


def get_trending_keywords(topic="artificial intelligence"):

    url = "https://serpapi.com/search"

    base_params = {
        "engine": "google_trends",
        "q": topic,
        "hl": "en",
        "geo": "US",
        "date": "today 12-m",
        "tz": "420",
        "api_key": SERPAPI_KEY
    }

    try:

        
        # 1. TRY RELATED QUERIES
        

        query_params = {
            **base_params,
            "data_type": "RELATED_QUERIES"
        }

        response = requests.get(
            url,
            params=query_params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print("SERP API Error:", data["error"])

        else:

            related_queries = data.get(
                "related_queries",
                {}
            )

            top_queries = related_queries.get(
                "top",
                []
            )

            rising_queries = related_queries.get(
                "rising",
                []
            )

            keywords = []

            # Top queries
            for item in top_queries:

                query = item.get("query")

                if query and query not in keywords:
                    keywords.append(query)

            # Rising queries
            for item in rising_queries:

                query = item.get("query")

                if query and query not in keywords:
                    keywords.append(query)

            if keywords:

                print(
                    f"Google Trends: {len(keywords)} "
                    "related queries found."
                )

                return keywords[:10]


        
        # 2. FALLBACK: RELATED TOPICS
        

        print(
            "No related queries found. "
            "Trying related topics..."
        )

        topic_params = {
            **base_params,
            "data_type": "RELATED_TOPICS"
        }

        response = requests.get(
            url,
            params=topic_params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            print(
                "SERP API Topic Error:",
                data["error"]
            )

        else:

            related_topics = data.get(
                "related_topics",
                {}
            )

            top_topics = related_topics.get(
                "top",
                []
            )

            rising_topics = related_topics.get(
                "rising",
                []
            )

            keywords = []

            # Top topics
            for item in top_topics:

                topic_data = item.get(
                    "topic",
                    {}
                )

                title = topic_data.get(
                    "title"
                )

                if title and title not in keywords:
                    keywords.append(title)

            # Rising topics
            for item in rising_topics:

                topic_data = item.get(
                    "topic",
                    {}
                )

                title = topic_data.get(
                    "title"
                )

                if title and title not in keywords:
                    keywords.append(title)

            if keywords:

                print(
                    f"Google Trends: {len(keywords)} "
                    "related topics found."
                )

                return keywords[:10]


        
        # 3. FINAL FALLBACK
        

        print(
            "No related queries/topics found. "
            "Using original topic."
        )

        return [topic]


    except requests.exceptions.RequestException as e:

        print(
            f"SERP API Request Error: {e}"
        )

        # Don't return an empty list.
        # Give the AI the original topic as context.

        return [topic]


    except Exception as e:

        print(
            f"Google Trends Error: {e}"
        )

        return [topic]