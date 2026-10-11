# Exercise search website and JSON catalog

OpenExerciseDB publishes a static exercise index for people and a directly
fetchable JSON catalog for tools. They are generated from the same SQLite
database as the interactive explorer, so the search page, downloadable records,
and explorer share one data source.

## Configured Pages URLs

- [Exercise search](https://rfivesix.github.io/OpenExerciseDB/exercise-search.html)
  lists every catalog record without JavaScript. Use browser Find to search
  exercise names in available languages, IDs, muscles, or equipment. Each
  record shows its stable ID and status.
- [Machine-readable catalog](https://rfivesix.github.io/OpenExerciseDB/exercises.json)
  is plain JSON and can be fetched without running the explorer or querying
  SQLite. The top-level metadata includes content version, schema version,
  source, license, attribution link, and generation time.
- [Interactive database explorer](https://rfivesix.github.io/OpenExerciseDB/)
  provides the existing JavaScript-powered search and full database table view.
- [Train Libre AI routine guide](https://trainlibre.com/docs/user-guide/ai-workout-routines/)
  explains how to select catalog exercises and form importable routines.

Each JSON record includes `id`, canonical English `name`, localized `names`,
`slug`, `status`, `recommended_for_routines`, `category`, `body_region`,
`modality`, role-tagged `muscles`, typed `equipment`, `tracking_type`,
`load_mode`, `difficulty`, `movement_pattern`, `mechanic`, `laterality`, and
`usage_tags`. Muscle and equipment values use stable catalog vocabulary IDs;
muscle entries also include their primary or secondary role.

IDs are JSON strings copied exactly from SQLite `exercises.id`. Train Libre’s
catalog importer stores that value unchanged as `Exercise.uuid`, and routine
import resolves `uuid` against the same value. Do not convert or generate IDs.
Only active records with a canonical English name are marked
`recommended_for_routines: true`; merged, deprecated, and otherwise inactive
records remain visible with their status but are not recommended for new
routines. The search page and JSON catalog link to each other and to the Train
Libre guide. The guide links back to both catalog URLs.

The data remains under the repository’s [CC BY-SA 4.0 license](LICENSE.md) and
attribution requirements ([ATTRIBUTION.md](ATTRIBUTION.md)).

## Rebuild and validate locally

From the repository root, build the SQLite source and then the complete static
site:

```bash
python3 build/build_db.py --db-out artifacts/catalog.db
python3 build/check_database.py artifacts/catalog.db
python3 build/build_explorer_site.py --db artifacts/catalog.db --out _site
```

The site builder calls `build/build_ai_catalog.py` to export `exercises.json`
and `exercise-search.html` from that SQLite database. It also writes
`sitemap.xml` and `robots.txt` using the GitHub Pages URL derived from the
repository’s GitHub origin (or the `--site-url` override). The `_site` directory
contains those files together with `index.html`, `catalog.db`, the existing
explorer assets, and `.nojekyll`.

Before submitting data changes, run the repository validation and tests:

```bash
python3 build/validate.py
cd test && python3 -m unittest discover -p 'test_*.py'
```

## Publish

The [Deploy database explorer workflow](.github/workflows/deploy-explorer.yml)
rebuilds the database and static site, uploads `_site` as the GitHub Pages
artifact, and deploys it. It runs on pushes to `main` that change catalog data,
website/build inputs, or the workflow itself; it can also be started manually.
The repository’s Pages target is `https://rfivesix.github.io/OpenExerciseDB/`.
These are configured target URLs; check the GitHub Pages workflow deployment
status before treating any specific build as live.
