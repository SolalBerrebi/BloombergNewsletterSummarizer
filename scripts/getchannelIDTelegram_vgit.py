#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:42:56 2024

@author: solalberrebi
"""

import requests

# Replace with your bot's token
TOKEN = 'your_token'

# URL to get updates from the bot
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

# Make the request
response = requests.get(url)

# Print the response
print(response.json())
