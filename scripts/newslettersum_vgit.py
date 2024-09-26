#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import imaplib
import email
from email import policy
import quopri
from bs4 import BeautifulSoup
from openai import OpenAI
from datetime import datetime
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email and Telegram Credentials (stored in .env)
HOST = os.getenv('EMAIL_HOST')
USERNAME = os.getenv('EMAIL_USERNAME')
PASSWORD = os.getenv('EMAIL_PASSWORD')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY  # Setting OpenAI API key

def fetch_latest_email_text(username, password, folder_name):
    try:
        mail = imaplib.IMAP4_SSL(HOST)
        mail.login(username, password)
        status, messages = mail.select(f'"{folder_name}"')
        if status == 'OK':
            typ, msgs = mail.search(None, 'UNSEEN')
            if msgs[0]:
                latest_email_id = msgs[0].split()[-1]
                typ, data = mail.fetch(latest_email_id, '(BODY[])')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1], policy=policy.default)
                        subject = str(email.header.make_header(email.header.decode_header(msg['subject'])))
                        date = datetime.strptime(msg['date'], '%a, %d %b %Y %H:%M:%S %z')
                        formatted_date = date.strftime('%Y-%m-%d')

                        # Create directory to store emails
                        try:
                            os.makedirs(f'./BLOOMBERGNEWS/TXT/{formatted_date}')
                        except FileExistsError:
                            pass  # Directory already exists

                        file_path = f'./BLOOMBERGNEWS/TXT/{subject}_{formatted_date}.txt'

                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    email_text = part.get_payload(decode=True).decode('utf-8', errors='replace')
                        else:
                            email_text = msg.get_payload(decode=True).decode('utf-8', errors='replace')

                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(email_text)

                        return file_path, subject
        print("No new unseen emails.")
        return None, None

    except Exception as e:
        print(f"Error fetching email: {e}")
        return None, None

def summarize_text(file_path, subject):
    # Load the email content
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Prepare prompt for OpenAI
    prompt = (
        f"USE YOUR OWN PROMPT.\n\n{text}"
    )

    # Use GPT to generate summary
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    summary_content = response.choices[0].text.strip()

    # Create directories for storing summaries
    formatted_date = datetime.now().strftime('%Y-%m-%d')
    try:
        os.makedirs(f"./BLOOMBERGNEWS/SUMUP/{formatted_date}")
    except FileExistsError:
        pass  # Directory already exists

    summary_file_name = f"./BLOOMBERGNEWS/SUMUP/{formatted_date}/{subject}_sumup.txt"

    with open(summary_file_name, 'w', encoding='utf-8') as f:
        f.write(summary_content)

    return summary_file_name, summary_content

def get_summary():
    file_path, subject = fetch_latest_email_text(USERNAME, PASSWORD, 'BLOOMBERG')
    if file_path:
        summary_file, message_to_send = summarize_text(file_path, subject)
        return message_to_send
    else:
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # Optional, for formatting
    }
    
    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        print(f"Message sent successfully to Telegram chat ID {TELEGRAM_CHAT_ID}")
    else:
        print(f"Failed to send message via Telegram. Error: {response.text}")

# Main execution
if __name__ == "__main__":
    while True:
        summary = get_summary()  # Fetch the summary from your existing code logic
        if summary:
            send_telegram_message(summary)
        else:
            print("No new emails found to summarize.")
        break
