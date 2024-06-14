#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Website-Status-Checker (https://github.com/KafetzisThomas/Website-Status-Checker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import sys
import requests

# Map HTTP status codes to their corresponding descriptions
statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable",
}


url = sys.argv[1]

web_response = requests.get(f"http://www.{url}")

print(
    f"\nUrl: {url}\nMessage: {statuses[web_response.status_code]}\nStatus code: {web_response.status_code}"
)
