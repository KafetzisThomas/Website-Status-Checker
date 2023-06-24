#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Website Status Checker (https://github.com/KafetzisThomas/Website-Status-Checker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import requests

urls = [
  "https://www.google.com",
  "https://www.github.com",
  "https://www.yahoo.com", 
  "https://www.amazon.com"
]

statuses = {
  200: "Website Available",
  301: "Permanent Redirect",
  302: "Temporary Redirect",
  404: "Not Found",
  500: "Internal Server Error",
  503: "Service Unavailable"
}

print("\nURLs\t\t\t\tMessage\t\t\t\tStatus Code")

for url in urls:
  web_response = requests.get(url)
  print(f"{url}\t\t{statuses[web_response.status_code]}\t\t{web_response.status_code}")
