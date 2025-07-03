# 🇪🇹 SiraFinder – Your AI-Powered Job Hunting Assistant

**SiraFinder** is an intelligent, Telegram-based job bot built for Ethiopia and beyond. It scrapes top job sites, personalizes alerts using AI, and empowers job seekers to find and apply for the right opportunities — faster and smarter.

> 🎯 "Sira" (ሥራ) means "job" in Amharic. SiraFinder = Your trusted job-finding companion.

---

## 🚀 Features

✅ **Smart Job Alerts**  
- Get daily or instant job notifications via Telegram  
- Filter by location, skills, experience level, or keywords  
- Support for remote, local, NGO, and government jobs

🤖 **AI-Powered Tools**  
- GPT-based **job description summarizer**  
- **Resume reviewer** for instant feedback  
- Auto-generate **custom cover letters** for applications  
- AI match score between your profile and job posts

🌐 **Multi-source Job Scraping**  
- Aggregates jobs from major platforms like **EthioJobs**, **Dereja**, **UN Jobs**, **RemoteOK**, etc.

💬 **Simple Chat Interface**  
- Use commands like `/start`, `/subscribe`, `/set`, and `/apply`  
- All inside Telegram – no sign-up required

---

## 📦 Tech Stack

| Layer         | Tech                                                                 |
|---------------|----------------------------------------------------------------------|
| Bot Platform  | [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) |
| Backend       | Python, FastAPI                                                      |
| Scraping      | BeautifulSoup, Requests, Playwright                                  |
| AI/ML         | OpenAI GPT-4 / Cohere / HuggingFace Transformers                     |
| DB            | MongoDB Atlas / Supabase / PostgreSQL                                |
| Deployment    | Railway / Render / Fly.io                                            |

---

## 📸 Screenshots (Coming Soon)

- Daily job digest message with AI summaries  
- Resume upload + feedback example  
- Cover letter generation result  
- User preference onboarding steps  

---
```

|── bot/                         # Telegram bot logic
│   ├── commands/               # Command handlers (e.g., /start, /set)
│   │   ├── start.py
│   │   ├── subscribe.py
│   │   └── resume_review.py
│   ├── messages/               # Bot responses & UI messages
│   │   └── messages.py
│   ├── inline/                 # Inline buttons/callback handlers
│   │   └── job_actions.py
│   ├── main.py                 # Entry point: bot setup and polling/webhook
│   └── dispatcher.py           # Register handlers and middlewares
│
├── scraper/                    # Job scraper modules
│   ├── base_scraper.py         # Abstract base class
│   ├── indeed_scraper.py       # Scrape Indeed
│   ├── remoteok_scraper.py     # Scrape RemoteOK
│   └── job_post_model.py       # Standard job posting data model
│
├── ai/                         # AI logic and integrations
│   ├── matcher.py              # Match jobs to user profile using embeddings
│   ├── summarizer.py           # Summarize job descriptions (GPT or LLM)
│   ├── resume_reviewer.py      # Review resumes and give feedback
│   └── cover_letter_gen.py     # Generate cover letters
│
├── models/                     # Data models and schemas
│   ├── user.py                 # User model: preferences, resume, etc.
│   └── job.py                  # Job model for DB/storage
│
├── services/                   # Core logic and business rules
│   ├── job_service.py          # Fetch, cache, rank jobs
│   ├── user_service.py         # Manage user prefs, state
│   └── ai_service.py           # Interface between AI & bot
│
├── database/                   # DB setup & CRUD
│   ├── db.py                   # Connect to MongoDB/Supabase/PostgreSQL
│   ├── crud_user.py
│   ├── crud_job.py
│   └── schema.sql              # Optional SQL schema if using RDBMS
│
├── scheduler/                  # Periodic tasks and cron jobs
│   └── job_dispatcher.py       # Send daily job alerts to users
│
├── config/                     # App configuration and secrets
│   ├── settings.py             # Env vars and global config
│   └── telegram_keys.env
│
├── tests/                      # Unit and integration tests
│   ├── test_scraper.py
│   ├── test_ai.py
│   └── test_bot_commands.py
│
├── requirements.txt            # Python dependencies
├── .env.example                # Template for environment variables
├── README.md                   # Project overview and setup
└── run.py                      # Main entry (start bot, schedule, etc.)

```
---

## 🔧 Installation & Development

```bash
git clone https://github.com/yourname/SiraFinder.git
cd SiraFinder
cp .env.example .env   # Fill in your keys
pip install -r requirements.txt
python run.py
```
