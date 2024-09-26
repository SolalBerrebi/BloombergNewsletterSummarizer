
# Bloomberg Market News Summarizer 📈💼
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot-blue)](https://core.telegram.org/bots)
[![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-brightgreen)](https://openai.com)

A robust newsletter summarizer for Bloomberg emails using OpenAI GPT-4, with automated delivery via Telegram. Tailored for finance professionals and students at the Master's level.

## Introduction
This project automates the process of summarizing Bloomberg newsletters using OpenAI's GPT-4 model and delivers these summaries to users via a Telegram bot. The system is designed for market finance professionals and students, providing clear, concise insights into financial news with an academic tone, suitable for Master's level learners.

## Key Features
- **Automated Email Retrieval**: Fetches unseen emails from Bloomberg using IMAP.
- **Advanced Summarization**: Uses GPT-4 to generate concise, clear summaries tailored to finance students.
- **Telegram Integration**: Sends the generated summaries via Telegram for easy access.
- **Glossary Support**: Provides English-French translations of finance-specific terminology.
- **Market Concept Explanation**: Explains key finance concepts with examples at the end of each summary.

## Technical Overview
This project integrates multiple technologies to create a seamless workflow:
- **Email Retrieval**: Fetches Bloomberg newsletters using IMAP.
- **Natural Language Processing**: GPT-4 model by OpenAI is used to summarize content in a structured, finance-focused manner.
- **Messaging**: Summaries are delivered using Telegram's Bot API.

## Installation & Setup
Follow these steps to run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/BloombergNewsletterSummarizer.git
   cd BloombergNewsletterSummarizer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (email credentials, Telegram bot token, and OpenAI API key):
   
   Create a `.env` file in the root directory to securely manage your credentials:
   ```bash
   touch .env

4. **Run the script:** Start fetching emails, generating summaries, and sending them to Telegram:
   ```bash
   python newslettersum_v1.py
   ```
   This will continuously check for unseen Bloomberg emails, summarize them, and send them to the specified Telegram chat.

## Project Structure

BloombergNewsletterSummarizer/
│
├── /scripts/                   # All the core Python scripts
│   ├── newslettersum_v1.py      # Main script for email summarization and Telegram messaging
│   └── getchannelIDTelegram.py  # Script for fetching the Telegram channel ID
│
├── .env                        # Environment variables (email credentials, bot token, API key)
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Project documentation
└── LICENSE                     # License for the project


## Key Technologies

- **OpenAI GPT-4:** This state-of-the-art language model enables the generation of high-quality summaries, making the complex finance language accessible to both professionals and students.
- **IMAP for Email Handling:** Securely connects to Bloomberg email servers to retrieve market news content in real time.
- **Telegram Bot API:** Seamlessly sends the summarized content to Telegram channels or user chats, ensuring that finance professionals can receive updates directly on their mobile devices.
- **Python:** The entire project is built using Python for its versatility and ease of integration with various APIs.

## Use Case Scenarios

- **Market Analysts:** Receive concise daily summaries of the latest Bloomberg reports directly via Telegram, with a focus on actionable insights.
- **Finance Students:** Stay up to date on market news while also enhancing finance vocabulary with the glossary feature, which includes English-French translations.


