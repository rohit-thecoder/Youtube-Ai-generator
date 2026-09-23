import re
import requests
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CreatorAI",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CONFIG
# ============================================================

BACKEND_URL = "https://youtube-ai-generator.onrender.com/"


# ============================================================
# CUSTOM CSS
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --red: #ff0000;
    --red-dark: #d90000;
    --black: #111111;
    --dark: #181818;
    --white: #ffffff;
    --bg: #f6f6f6;
    --border: #e5e5e5;
    --muted: #777777;
}

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background: var(--bg);
}
/* ==========================================================
   STREAMLIT MARKDOWN TEXT FIX
   ========================================================== */

.stMarkdown,
.stMarkdown p,
.stMarkdown span,
.stMarkdown li,
.stMarkdown ul,
.stMarkdown ol {
    color: #222222 !important;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4,
.stMarkdown h5,
.stMarkdown h6 {
    color: #111111 !important;
    font-weight: 800 !important;
}

.stMarkdown strong,
.stMarkdown b {
    color: #111111 !important;
}

.stMarkdown a {
    color: #ff0000 !important;
    text-decoration: none !important;
}

.stMarkdown blockquote {
    color: #555555 !important;
    border-left: 3px solid #ff0000 !important;
    padding-left: 12px;
}

.stMarkdown code {
    color: #222222 !important;
    background: #f1f1f1 !important;
}
.ai-output {
    background: #ffffff;
    border: 1px solid #e2e2e2;
    border-radius: 18px;
    padding: 28px;
    margin-top: 15px;
    color: #222222;
    box-shadow: 0 5px 25px rgba(0,0,0,0.035);
}

.ai-output h1,
.ai-output h2,
.ai-output h3,
.ai-output h4 {
    color: #111111 !important;
}

.ai-output p,
.ai-output li {
    color: #4b4b4b !important;
}

.ai-output strong {
    color: #111111 !important;
}

.ai-output a {
    color: #ff0000 !important;
}

/* Main container */

.block-container {
    max-width: 1450px;
    padding-top: 35px;
    padding-bottom: 60px;
}

/* Hide Streamlit menu */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ==========================================================
   SIDEBAR
   ========================================================== */

section[data-testid="stSidebar"] {
    background: #111111;
    border-right: 1px solid #292929;
}

section[data-testid="stSidebar"] > div {
    background: #111111;
}

section[data-testid="stSidebar"] * {
    color: #eeeeee;
}

.sidebar-brand {
    padding: 8px 0 24px 0;
    border-bottom: 1px solid #2b2b2b;
    margin-bottom: 25px;
}

.brand-row {
    display: flex;
    align-items: center;
    gap: 10px;
}

.youtube-logo {
    width: 36px;
    height: 26px;
    border-radius: 8px;
    background: #ff0000;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 14px;
    font-weight: 800;
}

.brand-name {
    color: white;
    font-size: 21px;
    font-weight: 800;
}

.brand-description {
    color: #8e8e8e;
    font-size: 11px;
    line-height: 1.6;
    margin-top: 9px;
}

.sidebar-title {
    color: #777777;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    margin-top: 24px;
    margin-bottom: 12px;
}

.query-item {
    background: #1a1a1a;
    border: 1px solid #292929;
    border-radius: 9px;
    padding: 9px 11px;
    margin-bottom: 7px;
    font-size: 12px;
    color: #dddddd;
}

.query-number {
    color: #ff3b30;
    font-weight: 800;
    margin-right: 7px;
}

.service-box {
    margin-top: 25px;
    padding: 14px;
    border: 1px solid #292929;
    border-radius: 12px;
    background: #181818;
}

.service-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 11px;
}

.service-row:last-child {
    margin-bottom: 0;
}

.service-status {
    color: #4ade80;
    font-size: 10px;
    font-weight: 700;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero {
    background: #111111;
    border-radius: 24px;
    padding: 48px;
    position: relative;
    overflow: hidden;
    border: 1px solid #252525;
    margin-bottom: 30px;
}

.hero::after {
    content: "";
    position: absolute;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: rgba(255, 0, 0, 0.10);
    right: -160px;
    top: -200px;
    filter: blur(10px);
}

.hero-badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 100px;
    border: 1px solid #333333;
    background: #1c1c1c;
    color: #bbbbbb;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 17px;
}

.hero-title {
    color: white;
    font-size: clamp(34px, 5vw, 57px);
    line-height: 1.02;
    letter-spacing: -2.4px;
    font-weight: 800;
    margin: 0;
    max-width: 850px;
}

.hero-title span {
    color: #ff3333;
}

.hero-description {
    color: #a3a3a3;
    font-size: 14px;
    line-height: 1.7;
    max-width: 680px;
    margin-top: 18px;
}


/* ==========================================================
   SECTION TITLES
   ========================================================== */

.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #111111;
    letter-spacing: -0.5px;
    margin-top: 30px;
}

.section-subtitle {
    color: #808080;
    font-size: 12px;
    margin-top: 4px;
    margin-bottom: 17px;
}


/* ==========================================================
   INPUT AREA
   ========================================================== */

div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label {
    font-size: 12px !important;
    font-weight: 700 !important;
    color: #333333 !important;
}

div[data-testid="stTextInput"] input {
    background: white !important;
    color: #111111 !important;
    border: 1px solid #dddddd !important;
    border-radius: 10px !important;
    min-height: 44px !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #ff0000 !important;
    box-shadow: 0 0 0 1px #ff0000 !important;
}

div[data-testid="stSelectbox"] > div > div {
    background: white !important;
    color: #111111 !important;
    border-radius: 10px !important;
    border-color: #dddddd !important;
    min-height: 44px !important;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

.stButton > button {
    border-radius: 10px !important;
    min-height: 42px !important;
    font-weight: 700 !important;
    font-size: 12px !important;
    border: 1px solid #dddddd !important;
    background: white !important;
    color: #222222 !important;
    transition: 0.2s ease !important;
}

.stButton > button:hover {
    border-color: #ff0000 !important;
    color: #ff0000 !important;
}

.stButton > button[kind="primary"] {
    background: #ff0000 !important;
    color: white !important;
    border-color: #ff0000 !important;
}

.stButton > button[kind="primary"]:hover {
    background: #d90000 !important;
    border-color: #d90000 !important;
}


/* ==========================================================
   METRIC CARDS
   ========================================================== */

.metric-card {
    background: white;
    border: 1px solid #e4e4e4;
    border-radius: 16px;
    padding: 19px;
    min-height: 105px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.025);
}

.metric-number {
    font-size: 29px;
    font-weight: 800;
    color: #111111;
    letter-spacing: -1px;
}

.metric-number.red {
    color: #ff0000;
}

.metric-label {
    margin-top: 5px;
    color: #858585;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}


/* ==========================================================
   KEYWORDS
   ========================================================== */

.keyword {
    display: inline-block;
    background: white;
    border: 1px solid #e1e1e1;
    border-radius: 100px;
    padding: 9px 13px;
    margin: 0 6px 7px 0;
    font-size: 11px;
    font-weight: 700;
    color: #222222;
}

.keyword::before {
    content: "#";
    color: #ff0000;
    margin-right: 4px;
}


/* ==========================================================
   VIDEO INFORMATION
   ========================================================== */

.video-title {
    font-size: 14px;
    font-weight: 750;
    line-height: 1.45;
    color: #111111;
    margin-top: 9px;
    margin-bottom: 5px;
}

.video-meta {
    color: #888888;
    font-size: 10px;
    margin-bottom: 8px;
}

.video-index {
    color: #ff0000;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}


/* ==========================================================
   IDEA BOX
   ========================================================== */

.idea-wrapper {
    background: white;
    border: 1px solid #e2e2e2;
    border-radius: 18px;
    padding: 25px;
    margin-top: 15px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.03);
}

.idea-header {
    color: #ff0000;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.idea-title {
    color: #111111;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 10px;
}

.idea-text {
    color: #555555;
    font-size: 13px;
    line-height: 1.7;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;
    color: #999999;
    font-size: 10px;
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid #dddddd;
}


/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 900px) {

    .block-container {
        padding-left: 15px;
        padding-right: 15px;
    }

    .hero {
        padding: 30px 25px;
        border-radius: 18px;
    }

    .hero-title {
        font-size: 36px;
        letter-spacing: -1.5px;
    }

}

</style>
""")


# ============================================================
# SESSION STATE
# ============================================================

if "result" not in st.session_state:
    st.session_state.result = None

if "selected_video" not in st.session_state:
    st.session_state.selected_video = None


# ============================================================
# HELPERS
# ============================================================

def get_thumbnail(url: str):
    """Generate YouTube thumbnail from video URL."""

    if not url:
        return None

    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"youtube\.com/embed/([^?]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)

        if match:
            video_id = match.group(1)
            return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    return None


def call_backend(topic, audience, region):
    """Call FastAPI backend."""

    response = requests.get(
        f"{BACKEND_URL}/generate_ideas/",
        params={
            "topic": topic,
            "audience": audience,
            "region": region,
        },
        timeout=180,
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-brand">
        <div class="brand-row">
            <div class="youtube-logo">▶</div>
            <div class="brand-name">CreatorAI</div>
        </div>

        <div class="brand-description">
            YouTube intelligence for smarter content creation.
        </div>
    </div>
    """)

    st.html("""
    <div class="sidebar-title">
        Research Queries
    </div>
    """)

    if st.session_state.result:

        keywords = st.session_state.result.get(
            "trending_keywords",
            []
        )

        if keywords:

            for index, keyword in enumerate(keywords, 1):

                st.html(
                    f"""
                    <div class="query-item">
                        <span class="query-number">
                            {index:02d}
                        </span>
                        {keyword}
                    </div>
                    """
                )

        else:

            st.caption("No queries found.")

    else:

        st.caption(
            "Generate research to discover "
            "current search queries."
        )

    st.html("""
    <div class="sidebar-title">
        Connected Services
    </div>

    <div class="service-box">

        <div class="service-row">
            <span>Google Trends</span>
            <span class="service-status">● LIVE</span>
        </div>

        <div class="service-row">
            <span>YouTube Data API</span>
            <span class="service-status">● LIVE</span>
        </div>

        <div class="service-row">
            <span>Mistral AI</span>
            <span class="service-status">● LIVE</span>
        </div>

    </div>
    """)


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-badge">
        ✦ AI CONTENT INTELLIGENCE
    </div>

    <div class="hero-title">
        Turn Google trends into
        <span>better video ideas.</span>
    </div>

    <div class="hero-description">
        Discover what people are searching for, analyze popular
        YouTube content, and generate original video ideas using AI.
    </div>

</div>
""")


# ============================================================
# INPUT
# ============================================================

st.html("""
<div class="section-title">
    Start your research
</div>

<div class="section-subtitle">
    Tell CreatorAI what you want to create.
</div>
""")


col1, col2, col3 = st.columns([2.3, 1.1, 1.1])

with col1:

    topic = st.text_input(
        "Topic",
        value="Agentic AI",
        placeholder="e.g. Agentic AI, RAG, Machine Learning",
    )

with col2:

    audience = st.selectbox(
        "Target Audience",
        [
            "Beginners",
            "Intermediate",
            "Advanced",
            "Students",
            "Developers",
            "Business Professionals",
            "Content Creators",
        ],
    )

with col3:

    region_map = {
        "India": "IN",
        "United States": "US",
        "United Kingdom": "GB",
        "Canada": "CA",
        "Australia": "AU",
        "Germany": "DE",
    }

    region_name = st.selectbox(
        "Region",
        list(region_map.keys()),
    )

    region = region_map[region_name]


st.write("")

generate = st.button(
    "✨  Generate Video Research",
    type="primary",
    use_container_width=False,
)


# ============================================================
# GENERATE
# ============================================================

if generate:

    if not topic.strip():
        st.error("Please enter a topic.")

    else:

        # ----------------------------------------------------
        # PREMIUM LOADER
        # ----------------------------------------------------

        loader = st.empty()

        loader.html("""
        <div class="research-loader">

            <div class="loader-spinner"></div>

            <div class="loader-title">
                Researching your topic...
            </div>

            <div class="loader-subtitle">
                Finding trends • Analyzing YouTube • Generating AI ideas
            </div>

        </div>

        <style>

        .research-loader {
            margin-top: 24px;
            padding: 30px;
            border-radius: 18px;
            background: #ffffff;
            border: 1px solid #e5e5e5;
            text-align: center;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
        }

        .loader-spinner {
            width: 42px;
            height: 42px;

            margin: 0 auto 16px auto;

            border: 4px solid #eeeeee;
            border-top: 4px solid #ff0000;

            border-radius: 50%;

            animation: researchSpin 0.8s linear infinite;
        }

        .loader-title {
            font-size: 19px;
            font-weight: 700;
            color: #111111;
            margin-bottom: 6px;
        }

        .loader-subtitle {
            font-size: 13px;
            color: #777777;
        }

        @keyframes researchSpin {

            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }

        }

        </style>
        """)

        # ----------------------------------------------------
        # BACKEND REQUEST
        # ----------------------------------------------------

        try:

            data = call_backend(
                topic.strip(),
                audience,
                region,
            )

            st.session_state.result = data
            st.session_state.selected_video = None

            # Remove loader before displaying result
            loader.empty()

            st.rerun()

        except requests.exceptions.ConnectionError:

            loader.empty()

            st.error(
                "Cannot connect to FastAPI. "
                "Please make sure your backend is running on "
                "https://youtube-ai-generator.onrender.com/"
            )

        except requests.exceptions.Timeout:

            loader.empty()

            st.error(
                "The backend took too long to respond. "
                "Please try again."
            )

        except requests.exceptions.HTTPError as error:

            loader.empty()

            st.error(
                f"FastAPI returned an error: {error}"
            )

        except Exception as error:

            loader.empty()

            st.error(
                f"Unexpected error: {error}"
            )
# ============================================================
# RESULTS
# ============================================================

if st.session_state.result:

    data = st.session_state.result

    keywords = data.get(
        "trending_keywords",
        []
    )

    videos = data.get(
        "trending_videos",
        []
    )

    ideas = data.get(
        "ideas",
        ""
    )


    # ========================================================
    # METRICS
    # ========================================================

    st.html("""
    <div class="section-title">
        Research overview
    </div>

    <div class="section-subtitle">
        Live information collected for your selected topic.
    </div>
    """)

    m1, m2, m3 = st.columns(3)

    with m1:

        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-number red">
                    {len(keywords)}
                </div>

                <div class="metric-label">
                    Trending Queries
                </div>
            </div>
            """
        )

    with m2:

        st.html(
            f"""
            <div class="metric-card">
                <div class="metric-number">
                    {len(videos)}
                </div>

                <div class="metric-label">
                    Videos Analyzed
                </div>
            </div>
            """
        )

    with m3:

        st.html("""
        <div class="metric-card">
            <div class="metric-number">
                5
            </div>

            <div class="metric-label">
                AI Ideas Generated
            </div>
        </div>
        """)


    # ========================================================
    # TRENDING QUERIES
    # ========================================================

    st.html("""
    <div class="section-title">
        🔥 Trending searches
    </div>

    <div class="section-subtitle">
        Related searches discovered through Google Trends.
    </div>
    """)

    if keywords:

        keyword_html = ""

        for keyword in keywords:

            keyword_html += (
                f'<span class="keyword">{keyword}</span>'
            )

        st.html(keyword_html)

    else:

        st.info("No trending queries were found.")


    # ========================================================
    # YOUTUBE RESEARCH
    # ========================================================

    st.html("""
    <div class="section-title">
         YouTube research
    </div>

    <div class="section-subtitle">
        Popular videos related to your selected topic.
    </div>
    """)

    if videos:

        for start in range(0, len(videos), 3):

            row = videos[start:start + 3]

            columns = st.columns(3)

            for index, (column, video) in enumerate(
                zip(columns, row),
                start=start + 1
            ):

                title = video.get(
                    "title",
                    "Untitled Video"
                )

                url = video.get(
                    "url",
                    ""
                )

                thumbnail = video.get(
                    "thumbnail"
                )

                if not thumbnail:

                    thumbnail = get_thumbnail(url)

                with column:

                    if thumbnail:

                        st.image(
                            thumbnail,
                            use_container_width=True,
                        )

                    st.html(
                        f"""
                        <div class="video-index">
                            VIDEO {index:02d}
                        </div>

                        <div class="video-title">
                            {title}
                        </div>

                        <div class="video-meta">
                            YouTube research result
                        </div>
                        """
                    )

                    if st.button(
                        "▶  Watch Video",
                        key=f"video_{start}_{index}",
                        use_container_width=True,
                    ):

                        st.session_state.selected_video = {
                            "title": title,
                            "url": url,
                        }

                        st.rerun()

    else:

        st.info(
            "No YouTube videos were found."
        )


    # ========================================================
    # VIDEO PLAYER
    # ========================================================

    if st.session_state.selected_video:

        selected = st.session_state.selected_video

        st.html("""
        <div class="section-title">
            ▶ Now watching
        </div>

        <div class="section-subtitle">
            Watch the selected research video without leaving the dashboard.
        </div>
        """)

        st.video(
            selected["url"]
        )

        st.caption(
            selected["title"]
        )


    # ========================================================
    # AI GENERATED IDEAS
    # ========================================================

    st.html("""
    <div class="section-title">
        ✨ AI-generated video ideas
    </div>

    <div class="section-subtitle">
        Mistral analyzed the research and generated these content ideas.
    </div>
    """)

    if ideas:

        st.html("""
        <div class="ai-output">
        """)

        st.markdown(
            ideas,
            unsafe_allow_html=False
        )

        st.html("""
        </div>
        """)

    else:

        st.info(
            "No AI ideas were generated."
        )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">
    CreatorAI · Google Trends · YouTube Data API · Mistral AI
</div>
""")