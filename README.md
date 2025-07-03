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

## 🔧 Installation & Development

```bash
git clone https://github.com/yourname/SiraFinder.git
cd SiraFinder
cp .env.example .env   # Fill in your keys
pip install -r requirements.txt
python run.py
