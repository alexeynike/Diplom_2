import json
import logging
from json import JSONDecodeError


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def logging_request(url, method, data, headers):
    text = (f"PERFOMING REQUEST:\n"
            f"REQUEST URL: {method} {url}\n"
            f"HEADERS: {headers}\n"
            f"REQUEST DATA: {data}\n")
    logging.info(text)


def logging_response(response):
    try:
        data = json.dumps(response.json(), ensure_ascii=False)
    except JSONDecodeError:
        data = response.text
    text = (f"\nGOT RESPONSE:\n"
            f"RESPONSE STATUS CODE: {response.status_code}\n"
            f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n"
            f"RESPONSE CONTENT: {data}\n")
    logging.info(text)