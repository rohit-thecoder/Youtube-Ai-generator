# 🎬 AI Based YouTube Video Idea Generator

An **AI-powered YouTube Video Idea Generator** that researches current trends, analyzes popular YouTube videos, and generates engaging video ideas using Mistral AI.

## 🚀 Features

- 🔥 Google Trends research using SerpApi
- ▶️ Popular YouTube video research using YouTube Data API v3
- 🤖 AI-generated video ideas using Mistral AI + LangChain
- 🎯 Target audience and region selection
- 🖼️ YouTube thumbnails and embedded video playback
- ⏳ Premium loading state during research
- 🎨 Modern Streamlit UI
- ⚡ FastAPI backend
- 🌐 Ready for Render + Streamlit Community Cloud deployment

## 🏗️ Architecture

```text
                         USER
                           │
                           ▼
                ┌─────────────────────┐
                │ Streamlit Frontend  │
                │  streamlit_app.py   │
                └──────────┬──────────┘
                           │
                           │ HTTP Request
                           ▼
                ┌─────────────────────┐
                │    FastAPI Backend  │
                │       main.py       │
                └──────────┬──────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        ┌──────────┐ ┌───────────┐ ┌──────────┐
        │ SerpApi  │ │ YouTube   │ │ Mistral  │
        │  Trends  │ │ Data API  │ │   AI     │
        └──────────┘ └───────────┘ └──────────┘
                           │
                           ▼
                    Research Results
                           │
                           ▼
                AI Generated Video Ideas
```

## 📁 Project Structure

```text
youtube-video-idea-generator/
│
├── backend/
│   ├── main.py
│   ├── google_trends.py
│   ├── youtube_trends.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

### Frontend
- Streamlit
- Python
- Requests
- HTML/CSS

### Backend
- FastAPI
- Uvicorn
- Python
- Requests

### AI
- LangChain
- Mistral AI
- `ChatMistralAI`

### APIs
- SerpApi Google Trends
- YouTube Data API v3

## 🔑 API Keys

The project requires:

| Service | Environment Variable | Purpose |
|---|---|---|
| SerpApi | `SERPAPI_KEY` | Google Trends research |
| YouTube Data API | `YOUTUBE_API_KEY` | YouTube video research |
| Mistral AI | `MISTRAL_API_KEY` | AI idea generation |

Create `.env` for local development:

```env
SERPAPI_KEY=your_serpapi_key
YOUTUBE_API_KEY=your_youtube_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

> ⚠️ Never commit `.env` or API keys to GitHub.

## 💻 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/rohit-thecoder/Youtube-Ai-generator.git
cd youtube-video-idea-generator
```

### 2. Create virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## ⚙️ Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
fastapi
uvicorn[standard]
python-dotenv
requests
langchain
langchain-mistralai
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
streamlit
requests
```

Start Streamlit:

```bash
streamlit run streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

## 🔗 Backend API

### Generate Video Ideas

```http
GET /generate_ideas/
```

Parameters:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `topic` | string | Required | Topic to research |
| `audience` | string | `Beginners` | Target audience |
| `region` | string | `US` | YouTube region |

Example:

```text
http://127.0.0.1:8000/generate_ideas/?topic=Artificial%20Intelligence&audience=Beginners&region=US
```

Example response:

```json
{
  "trending_keywords": [],
  "trending_videos": [],
  "ideas": "AI generated video ideas..."
}
```

## 🔄 Application Workflow

```text
1. User enters a topic
          ↓
2. Streamlit sends request to FastAPI
          ↓
3. FastAPI requests Google Trends data
          ↓
4. FastAPI retrieves popular YouTube videos
          ↓
5. Research data is sent to Mistral AI
          ↓
6. Mistral generates 5 video ideas
          ↓
7. FastAPI returns JSON
          ↓
8. Streamlit displays:
      ├── Trending Keywords
      ├── YouTube Videos
      ├── Thumbnails
      ├── Video Player
      └── AI Generated Ideas
```

## 🤖 AI Idea Generation

The AI uses:

```text
Topic
  +
Trending Keywords
  +
Popular YouTube Videos
  +
Target Audience
       ↓
   Mistral AI
       ↓
5 YouTube Video Ideas
```

Generated ideas can include:

- Title
- Hook
- Concept
- Why it works
- Suggested format

## 🌐 Deployment

Recommended production architecture:

```text
Streamlit Community Cloud
          │
          │ HTTPS
          ▼
        Render
          │
          ├── SerpApi
          ├── YouTube API
          └── Mistral AI
```

### Backend on Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Add these environment variables:

```text
SERPAPI_KEY
YOUTUBE_API_KEY
MISTRAL_API_KEY
```

After deployment, Render provides a URL such as:

```text
https://your-backend.onrender.com
```

Test:

```text
https://your-backend.onrender.com/docs
```

### Frontend on Streamlit Community Cloud

Set:

```text
BACKEND_URL=https://your-backend.onrender.com
```

Use this in the frontend:

```python
import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)
```

This keeps local and production environments compatible.

## 🔐 Security

Recommended `.gitignore`:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

Never expose API keys in source code or commit them to GitHub.

## 🧪 Testing

Backend:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Frontend:

```bash
streamlit run streamlit_app.py
```

Test flow:

```text
Enter Topic
      ↓
Select Audience
      ↓
Select Region
      ↓
Generate Video Research
      ↓
Loading State
      ↓
Trending Queries
      ↓
YouTube Videos
      ↓
AI Generated Ideas
```

## 📌 Example Use Cases

Useful for:

- YouTube creators
- Content strategists
- Digital marketers
- Social media managers
- Video production teams
- AI content creators

Example topics:

```text
Artificial Intelligence
Generative AI
Machine Learning
Web Development
Gaming
Technology
Fitness
Finance
Education
Travel
```

## 🚀 Future Improvements

- 🔥 Real-time Google Trends dashboard
- 📊 YouTube video analytics
- 📈 Search trend graphs
- 🎯 Advanced audience targeting
- 🧠 Agentic research workflow
- 🔍 Competitor channel analysis
- 💡 Thumbnail title suggestions
- 📝 AI-generated video scripts
- 🎨 AI thumbnail generation
- 📅 YouTube content calendar
- 📊 SEO score for generated ideas
- 💬 Follow-up chat with the research agent
- 💾 Save generated ideas
- 🔐 User authentication
- 🗄️ Research history database

## 👨‍💻 Author

**Rohit Kumar**

B.Tech CSE Student  
Machine Learning & Generative AI Learner

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

## 📄 License

This project is intended for educational and personal development purposes.
#   Y o u t u b e - A i - g e n e r a t o r 
 
 