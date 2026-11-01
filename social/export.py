"""Write CAPTIONS.md (copy-paste ready) and calendar.csv from posts.py.

Usage: python3 social/export.py [YYYY-MM-DD start date, default 2026-11-02]
"""
import csv
import datetime as dt
import re
import sys
from pathlib import Path

from posts import POSTS
from publish_instagram import full_caption, image_name

ROOT = Path(__file__).resolve().parent
start = dt.date.fromisoformat(sys.argv[1] if len(sys.argv) > 1 else "2026-11-02")


def plain(html):
    return re.sub(r"<[^>]+>", " ", html).replace("&#8209;", "-").replace("  ", " ").strip()


md = ["# CleanAir: 30 Instagram posts\n",
      f"Day 1 = {start:%A %d %B %Y}. Images are in `social/posts/`. Each caption below includes the call to action and hashtags.\n"]
rows = []
for p in POSTS:
    date = start + dt.timedelta(days=p["day"] - 1)
    cap = full_caption(p)
    md += [f"\n---\n\n## Day {p['day']:02d} · {date:%a %d %b} · {p['pillar']} · {p['audience']}\n",
           f"**Image:** `posts/{image_name(p)}`  \n**On-image headline:** {plain(p.get('title', 'Myth vs fact: ' + p.get('myth', '')))}\n",
           "```text\n" + cap + "\n```\n"]
    rows.append([p["day"], date.isoformat(), date.strftime("%A"), p["pillar"], p["audience"],
                 plain(p.get("title", "Myth vs fact: " + p.get("myth", ""))), image_name(p), cap])

(ROOT / "CAPTIONS.md").write_text("".join(md), encoding="utf-8")
with open(ROOT / "calendar.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["day", "date", "weekday", "pillar", "audience", "headline", "image", "caption"])
    w.writerows(rows)
print("wrote CAPTIONS.md and calendar.csv")
