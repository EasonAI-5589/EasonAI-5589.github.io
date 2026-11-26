# EasonAI-5589.github.io · personal homepage

Jekyll site (Minimal Light layout, `_layouts/minimal.html`) served at https://easonai-5589.github.io in English (`/`) and Chinese (`/zh/`). GitHub Pages builds `main` with the `pages-build-deployment` workflow; there is no other CI.

## Build and check

Jekyll is not installed on the NTU Mac mini, so you verify the site through the Pages build after you push:

```sh
R=EasonAI-5589/EasonAI-5589.github.io
git push origin main
ID=$(gh run list -R $R -L 1 --json databaseId --jq '.[0].databaseId')
until gh run view $ID -R $R --json status --jq .status | grep -q completed; do sleep 10; done
gh run view $ID -R $R --json conclusion --jq .conclusion      # expect: success
# Run the site checks against the exact files Pages built:
D=$(mktemp -d) && gh run download $ID -R $R -n github-pages -D $D && mkdir $D/site && tar -xf $D/artifact.tar -C $D/site
python3 scripts/verify_bilingual.py $D/site                       # expect: OK
```

- If the deploy step fails with HTTP 500/504 ("Failed to create deployment") but the build step passed, the cause is on GitHub's side. Re-run it later with `gh run rerun <id> -R $R`; do not change code to fix it.
- With a local Ruby setup, `bundle exec jekyll build` and then `python3 scripts/verify_bilingual.py _site` do the same check.

## Where things live

- Page text: `_data/homepage.yml`. The `en:` and `zh:` trees must have the same keys; add every new UI string to both.
- Papers: `_publications/*.md` front matter holds the title, authors, links and `status`. Per-paper summary, role and contribution text is in `_data/homepage.yml` under `papers`, keyed by `arxiv_id`.
- Order of the "Selected Work" cards and the top of the publication list: `selected_order` (1 = first). `scripts/verify_bilingual.py` (`test_work_panels_keep_selected_and_ongoing_entries_separate`) hard-codes the same order, so update it in the same commit.
- Review scores: optional `review:` front matter (`venue`, `scores`, optional `rank`) is rendered by `_includes/review-status.html` on cards, lists and project pages. Take the scores from Eason or his CV, never guess them.
- News: `_data/news.yml`, newest first, one emoji per category (see the header of that file).
- Ongoing projects: `_data/projects.yml`; project pages: `_data/project_pages.yml`.
- `_publications` has `output: false`, so per-paper pages are not generated. `_layouts/research-publication.html` is unused.
- Analytics: `_config.yml` → `analytics.google.tracking_id` (GA4) and `mapmyvisitors_id` (visitor map at the bottom of the homepage). Use MapMyVisitors; ClustrMaps is unreachable.

## Don'ts

- Do not edit the legacy Academic Pages folders listed under `exclude:` in `_config.yml`; they are not published.
- Do not add scores, acceptances or rankings that Eason has not confirmed.
- Everything on `main` goes public within minutes. Show Eason any new public claims (news, scores, bios) before you push.

## Done means

The Pages run for your commit concluded `success`, `verify_bilingual.py` passed against its built files, and you read back the changed text from the live English and Chinese pages (add `?v=$RANDOM` to bypass the cache).
