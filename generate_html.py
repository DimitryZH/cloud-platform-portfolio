import html
import os
import re
from datetime import datetime
from pathlib import Path

import markdown


README_PATH = Path("README.md")
OUTPUT_PATH = Path("index.html")
PORTFOLIO_HEADING_PATTERN = re.compile(
    r"^<h1>(?P<name>[^<]+)</h1>\n<h2>(?P<title>[^<]+)</h2>",
    re.MULTILINE,
)


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


def format_portfolio_heading(html_body: str) -> str:
    """Render the README name and portfolio title as a single styled heading block."""

    def replace_heading(match: re.Match[str]) -> str:
        return (
            '<div class="portfolio-heading">\n'
            f'  <h1 class="name">{match.group("name")}</h1>\n'
            f'  <div class="portfolio-title">{match.group("title")}</div>\n'
            "</div>"
        )

    return PORTFOLIO_HEADING_PATTERN.sub(replace_heading, html_body, count=1)


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

    html_body = format_portfolio_heading(html_body)

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

.hero-banner {{
    width: 94%;
    margin: 0 auto 36px;
}}

.hero-banner img {{
    display: block;
    width: 100%;
    height: auto;
    border-radius: 12px;
}}

.portfolio-heading {{
    margin-bottom: 24px;
}}

.name {{
    margin: 0 0 6px;
    font-size: clamp(2.2rem, 4vw, 2.8rem);
}}

.portfolio-title {{
    font-size: clamp(1.35rem, 2.6vw, 1.7rem);
    font-weight: 600;
    line-height: 1.35;
    color: #334155;
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

    .hero-banner {{
        width: 100%;
        margin-bottom: 28px;
    }}

    .name {{
        font-size: 2rem;
    }}

    .portfolio-title {{
        font-size: 1.25rem;
    }}

    h2 {{
        margin-top: 38px;
    }}
}}
</style>
</head>

<body>

<div class="hero-banner">
  <img
    src="assets/portfolio_pages_banner.jpg"
    alt="Dmitry Zhuravlev — Cloud DevOps Engineer and GitHub Developer Program Member"
  >
</div>

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
