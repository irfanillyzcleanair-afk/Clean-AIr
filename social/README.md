# CleanAir social media kit

| Path | What it is |
| --- | --- |
| `posts/` | 30 finished Instagram posts, 1080 × 1350 (4:5 portrait), JPG |
| `CAPTIONS.md` | Copy-paste captions with call to action and hashtags, one per day |
| `calendar.csv` | The same plan as a spreadsheet (open in Excel / Google Sheets) |
| `MARKETING_PLAN.md` | How to reach offices, villas and government, with ads, LinkedIn and tenders |
| `posts.py` | Source text for every post: edit here, then re-render |
| `render.py`, `shot.cjs` | Re-render the designs (`python3 social/render.py`, needs Node + Playwright) |
| `export.py` | Rebuild `CAPTIONS.md` and `calendar.csv` (`python3 social/export.py 2026-11-02`) |
| `publish_instagram.py` | Posts one day's image and caption through the Instagram Graph API |

## Posting by hand

Open `CAPTIONS.md`, save the day's image from `posts/` to your phone, and paste the caption into Instagram.

## Automatic daily posting

The workflow `.github/workflows/instagram-daily.yml` posts one image a day at 10:47 Dubai time.
It does nothing until you complete these steps:

1. **Instagram account:** switch the company Instagram to a *Professional → Business* account and link it to a Facebook Page.
2. **Meta developer app:** at developers.facebook.com create an app (type *Business*), add the *Instagram* product and request the `instagram_basic` and `instagram_content_publish` permissions. Generate a **long-lived access token** for the account and note the **Instagram user ID**. Long-lived tokens last about 60 days, so refresh it before then.
3. **GitHub settings** (repository → Settings → Secrets and variables → Actions):
   - Secret `IG_USER_ID` = the Instagram user ID
   - Secret `IG_ACCESS_TOKEN` = the long-lived token
   - Variable `IG_START_DATE` = the date of Day 1, e.g. `2026-11-03`
   - Variable `GRAPH_HOST` = `graph.instagram.com` only if you created the token with *Instagram Login*; leave it unset for Facebook Login.
4. **Merge this branch into `main`.** GitHub runs scheduled workflows only from the default branch.
5. **Test first:** Actions → *Instagram daily post* → *Run workflow*, day `1`, dry run ticked. Check the log, then run again with dry run unticked to publish Day 1 manually.

Never paste the access token into a file, an issue or a chat; keep it only in GitHub Secrets.
