"""Publish one day's CleanAir post to Instagram through the official Instagram Graph API.

Environment variables
  IG_USER_ID       Instagram professional (Business/Creator) account ID
  IG_ACCESS_TOKEN  Long-lived access token with instagram_content_publish permission
  IG_START_DATE    Date of Day 1 in YYYY-MM-DD (Dubai time). Day = days since start + 1
  IG_DAY           Optional: force a specific day (1-30) instead of using the start date
  IMAGE_BASE_URL   Public URL of the social/posts folder (the GitHub workflow sets this)
  GRAPH_HOST       graph.facebook.com (default, Facebook-login tokens) or graph.instagram.com
  DRY_RUN=1        Print what would be posted without calling the API

Usage: python3 social/publish_instagram.py
"""
import datetime as dt
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from posts import POSTS, CTA_LINE  # noqa: E402

API_VERSION = "v21.0"
DUBAI = dt.timezone(dt.timedelta(hours=4))


def full_caption(post):
    tags, seen = [], set()
    for group in post["tags"]:
        for t in group.split():
            if t.lower() not in seen:
                seen.add(t.lower())
                tags.append(t)
    return post["caption"] + CTA_LINE + "\n\n" + " ".join(tags[:30])


def image_name(post):
    return f"day-{post['day']:02d}-{post['layout']}.jpg"


def which_day():
    if os.environ.get("IG_DAY"):
        return int(os.environ["IG_DAY"])
    start = os.environ.get("IG_START_DATE")
    if not start:
        sys.exit("IG_START_DATE is not set; nothing to post.")
    today = dt.datetime.now(DUBAI).date()
    return (today - dt.date.fromisoformat(start)).days + 1


def call(method, url, params):
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Instagram API error {e.code}: {e.read().decode()}")


def main():
    day = which_day()
    post = next((p for p in POSTS if p["day"] == day), None)
    if post is None:
        print(f"Day {day} is outside the 30-day plan; nothing to post.")
        return
    base = os.environ.get("IMAGE_BASE_URL", "").rstrip("/")
    image_url = f"{base}/{image_name(post)}"
    caption = full_caption(post)
    print(f"Day {day}: {image_url}\n---\n{caption}\n---")
    if os.environ.get("DRY_RUN") == "1":
        return

    user, token = os.environ["IG_USER_ID"], os.environ["IG_ACCESS_TOKEN"]
    graph = f"https://{os.environ.get('GRAPH_HOST', 'graph.facebook.com')}/{API_VERSION}"
    container = call("POST", f"{graph}/{user}/media",
                     {"image_url": image_url, "caption": caption, "access_token": token})["id"]
    for _ in range(30):  # wait until Instagram has fetched and processed the image
        status = call("GET", f"{graph}/{container}", {"fields": "status_code", "access_token": token})
        if status.get("status_code") == "FINISHED":
            break
        if status.get("status_code") == "ERROR":
            sys.exit(f"Instagram could not process the image: {status}")
        time.sleep(5)
    media = call("POST", f"{graph}/{user}/media_publish", {"creation_id": container, "access_token": token})
    print("Published Instagram media id:", media.get("id"))


if __name__ == "__main__":
    main()
