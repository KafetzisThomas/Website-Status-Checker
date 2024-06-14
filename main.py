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


def check_website_status(url):
    response = requests.get(url)
    status_code = response.status_code
    message = statuses[response.status_code]
    print(f"\nUrl: {url}\nMessage: {message}\nStatus code: {status_code}")


if __name__ == "__main__":
    input_url = sys.argv[1]
    check_website_status(input_url)
