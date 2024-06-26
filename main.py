#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Website-Status-Checker (https://github.com/KafetzisThomas/Website-Status-Checker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import sys
import requests
from requests.exceptions import ConnectionError


# Map HTTP status codes to their corresponding descriptions
statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


def check_website_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        message = statuses[response.status_code]
        print(
            f"[*] Url: {input_url}\n[*] Message: {message}\n[*] Status code: {status_code}"
        )
    except ConnectionError:
        print(
            f"[*] Url: {url}\n[!] Error: Failed to establish a new connection. The server may not exist."
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] Usage: python3 main.py <URL>")
        sys.exit()

    input_url = sys.argv[1]
    if "http://www." not in input_url:
        input_url = f"http://www.{input_url}"

    check_website_status(input_url)
