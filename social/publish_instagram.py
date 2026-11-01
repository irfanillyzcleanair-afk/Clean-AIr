"""Publish one day's CleanAir post to Instagram through the official Instagram Graph API.

Environment variables
  IG_USER_ID       Instagram professional (Business/Creator) account ID
  IG_ACCESS_TOKEN  Long-lived access token with instagram_content_publish permission
  IG_START_DATE    Date of Day 1 in YYYY-MM-DD (Dubai time). Day = days since start + 1
  IG_DAY           Optional: force a specific day (1-30) instead of using the start date
  IMAGE_BASE_URL   Public URL of the social/posts folder (the GitHub workflow sets this)
  GRAPH_HOST       graph.facebook.com (default, Facebook-login tokens) or graph.instagram.com
  CAPTION_LANG     both (default: English then Arabic), en or ar
  IG_POST_STORY    1 (default) also posts the matching Story image; 0 to skip
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
from captions_ar import AR, CTA_AR, TAGS_AR  # noqa: E402

API_VERSION = "v21.0"
DUBAI = dt.timezone(dt.timedelta(hours=4))


def full_caption(post, lang="en"):
    tags, seen = [], set()
    groups = list(post["tags"]) + ([TAGS_AR] if lang in ("ar", "both") else [])
    for group in groups:
        for t in group.split():
            if t.lower() not in seen:
                seen.add(t.lower())
                tags.append(t)
    hashtags = " ".join(tags[:30])
    if lang == "ar":
        return AR[post["day"]] + CTA_AR + "\n\n" + hashtags
    if lang == "both":
        return post["caption"] + CTA_LINE + "\n\n— العربية —\n\n" + AR[post["day"]] + "\n\n" + hashtags
    return post["caption"] + CTA_LINE + "\n\n" + hashtags


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
    caption = full_caption(post, os.environ.get("CAPTION_LANG", "both"))
    if len(caption) > 2200:
        sys.exit(f"Caption for day {day} is {len(caption)} characters; Instagram allows 2,200.")
    print(f"Day {day}: {image_url}\n---\n{caption}\n---")
    if os.environ.get("DRY_RUN") == "1":
        return

    publish(image_url, caption)
    if os.environ.get("IG_POST_STORY", "1") == "1":
        publish(f"{base.rsplit('/', 1)[0]}/stories/story-{day:02d}.jpg", None, story=True)


def publish(image_url, caption, story=False):
    user, token = os.environ["IG_USER_ID"], os.environ["IG_ACCESS_TOKEN"]
    graph = f"https://{os.environ.get('GRAPH_HOST', 'graph.facebook.com')}/{API_VERSION}"
    params = {"image_url": image_url, "access_token": token}
    if story:
        params["media_type"] = "STORIES"
    else:
        params["caption"] = caption
    container = call("POST", f"{graph}/{user}/media", params)["id"]
    for _ in range(30):  # wait until Instagram has fetched and processed the image
        status = call("GET", f"{graph}/{container}", {"fields": "status_code", "access_token": token})
        if status.get("status_code") == "FINISHED":
            break
        if status.get("status_code") == "ERROR":
            sys.exit(f"Instagram could not process the image: {status}")
        time.sleep(5)
    media = call("POST", f"{graph}/{user}/media_publish", {"creation_id": container, "access_token": token})
    print("Published", "story" if story else "post", "- Instagram media id:", media.get("id"))

if __name__ == "__main__":
    main()
