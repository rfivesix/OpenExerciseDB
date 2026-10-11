#!/usr/bin/env python3
"""Build the static SQLite explorer used by GitHub Pages.

The browser loads ``catalog.db`` itself with sql.js. No API or server-side
database is involved, which keeps the published explorer identical to the
release database.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape

from build_ai_catalog import export_catalog


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "artifacts" / "openexercisedb.db"
DEFAULT_OUTPUT = ROOT / "artifacts" / "explorer-site"
SOURCE = ROOT / "web"


def default_site_url() -> str:
    """Derive the GitHub Pages URL from Actions context or the local origin."""
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not repository:
        repository = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=ROOT,
            text=True,
        ).strip()
        match = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", repository)
        if not match:
            raise SystemExit("Could not derive GitHub Pages URL from remote.origin.url; pass --site-url.")
        repository = f"{match.group(1)}/{match.group(2)}"
    if "/" not in repository:
        raise SystemExit("GITHUB_REPOSITORY must be in owner/repository form.")
    owner, project = repository.split("/", 1)
    project = project.removesuffix(".git")
    base = f"https://{owner}.github.io"
    return base if project.lower() == f"{owner}.github.io".lower() else f"{base}/{project}"


def write_sitemap(output: Path, site_url: str) -> None:
    base = site_url.rstrip("/")
    pages = ["/", "/exercise-search.html", "/exercises.json", "/legal.html"]
    urls = "\n".join(f"  <url><loc>{escape(base + page)}</loc></url>" for page in pages)
    (output / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (output / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static database explorer")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite catalog to publish")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT, help="Output directory")
    parser.add_argument("--site-url", help="Canonical GitHub Pages URL (default: derived from repository)")
    args = parser.parse_args()

    database = args.db.resolve()
    output = args.out.resolve()
    if not database.is_file():
        raise SystemExit(f"Database not found: {database}. Run build/build_db.py first.")

    output.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "legal.html", "app.js", "style.css"):
        shutil.copy2(SOURCE / name, output / name)
    shutil.copy2(database, output / "catalog.db")
    export_catalog(database, output)
    write_sitemap(output, args.site_url or default_site_url())
    (output / ".nojekyll").touch()
    try:
        shown_output = output.relative_to(ROOT)
    except ValueError:
        shown_output = output
    print(f"Wrote {shown_output} (using {database.name})")


if __name__ == "__main__":
    main()
