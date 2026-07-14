import html
import os
from datetime import datetime
from pathlib import Path

import markdown


README_PATH = Path("README.md")
OUTPUT_PATH = Path("index.html")


def format_build_date(raw_value: str) -> str:
    """Convert an ISO-8601 timestamp into a compact UTC display value."""
    if not raw_value:
        return "Unavailable"

    try:
        parsed = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
        return parsed.strftime("%Y-%m-%d %H:%M UTC")
    except ValueError:
        return raw_value


def build_commit_link(repo_url: str, commit_sha: str) -> str:
    """Render commit metadata safely, with or without a repository URL."""
    short_sha = commit_sha[:7] if commit_sha else "Unavailable"

    if not repo_url or not commit_sha:
        return html.escape(short_sha)

    safe_url = html.escape(repo_url.rstrip("/"), quote=True)
    safe_sha = html.escape(short_sha)
    return f'<a href="{safe_url}/commit/{html.escape(commit_sha, quote=True)}">{safe_sha}</a>'


def main() -> None:
    if not README_PATH.exists():
        raise FileNotFoundError(f"{README_PATH} was not found")

    md_content = README_PATH.read_text(encoding="utf-8")

    # "extra" improves GitHub-like Markdown behavior.
    # "sane_lists" makes list parsing more predictable after headings/paragraphs.
    html_body = markdown.markdown(
        md_content,
        extensions=[
            "extra",
            "sane_lists",
        ],
        output_format="html5",
    )

    commit_sha = os.getenv("COMMIT_SHA", "")
    build_date = format_build_date(os.getenv("BUILD_DATE", ""))
    repo_url = os.getenv("REPO_URL", "")
    commit_html = build_commit_link(repo_url, commit_sha)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Dmitry Zhuravlev — Cloud DevOps, Platform Engineering & AI Infrastructure Portfolio</title>

<style>
:root {{
    color-scheme: light;
}}

* {{
    box-sizing: border-box;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    margin: 40px auto;
    max-width: 960px;
    line-height: 1.65;
    color: #111827;
    padding: 0 24px;
    background: #ffffff;
}}

h1, h2, h3, h4 {{
    line-height: 1.25;
    color: #0f172a;
}}

h1 {{
    margin: 0 0 20px;
    font-size: clamp(2rem, 4vw, 3rem);
}}

h2 {{
    margin-top: 48px;
    padding-bottom: 8px;
    border-bottom: 1px solid #e5e7eb;
}}

h3 {{
    margin-top: 30px;
}}

p {{
    margin: 12px 0 18px;
}}

ul, ol {{
    margin: 10px 0 22px;
    padding-left: 28px;
}}

li {{
    margin: 6px 0;
}}

strong {{
    color: #111827;
}}

a {{
    color: #2563eb;
    text-decoration: none;
}}

a:hover {{
    text-decoration: underline;
}}

hr {{
    margin: 40px 0;
    border: 0;
    border-top: 1px solid #e5e7eb;
}}

.footer {{
    margin-top: 64px;
    padding-top: 22px;
    border-top: 1px solid #e5e7eb;
    font-size: 14px;
    color: #6b7280;
}}

.footer a {{
    color: #2563eb;
}}

.status {{
    margin-bottom: 12px;
}}

@media (max-width: 640px) {{
    body {{
        margin: 24px auto;
        padding: 0 16px;
    }}

    h2 {{
        margin-top: 38px;
    }}
}}
</style>
</head>

<body>

{html_body}

<footer class="footer">
  <div class="status">
    Build passing<br>
    Auto-deployed via GitHub Actions<br>
    CI/CD enabled
  </div>

  <div class="meta">
    Last deploy: {html.escape(build_date)}<br>
    Commit: {commit_html}
  </div>
</footer>

</body>
</html>
"""

    OUTPUT_PATH.write_text(html_template, encoding="utf-8")
    print(f"{OUTPUT_PATH} generated successfully")


if __name__ == "__main__":
    main()
