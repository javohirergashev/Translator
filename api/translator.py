import requests
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
base_link = os.environ.get("BASE_MYMEMORY_LINK")


def handler(request):
    body = request.get_json()

    try:
        q = body["q"]
        langpair = body["langpair"]
    except KeyError:
        return error_msg("Empty input")

    if not isinstance(q, str) or not isinstance(langpair, str):
        return error_msg("Invalid input or langpair type")

    if not q.strip() or not langpair:
        return error_msg("Missing input or langpair")

    if not re.match(r"^[a-zA-Z]{2}\|[a-zA-Z]{2}$", langpair.strip()):
        return error_msg("Wrong langpair format")

    try:
        data = translate(q.strip(), langpair.strip())
        t_text = data["responseData"]["translatedText"].strip()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"t-text": t_text})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }


def translate(q, langpair):
    params = {
        "q": q,
        "langpair": langpair,
    }

    try:
        data = requests.get(base_link, params=params, timeout=10).json()

        if not (200 <= data.get("responseStatus", 0) < 300):
            raise Exception(data.get("responseDetails", "Unknown Error"))

        return data

    except requests.RequestException as e:
        raise HTTPException(
            status_code=502, detail=f"Upstream error: {str(e)}")


def error_msg(msg):
    return {
        "statusCode": 400,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"error": msg})
    }
