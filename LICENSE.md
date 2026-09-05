# License

This repository contains two kinds of material under two different licenses.

## Data — CC BY-SA 4.0

Everything under `data/`, `vocab/`, and every database artifact published from
this repository is licensed under the
**[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa-4]**.

You are free to share and adapt this data for any purpose, including
commercially, provided that you:

- **give appropriate credit** — see [ATTRIBUTION.md](ATTRIBUTION.md), and link
  back to this repository;
- **distribute your contributions under the same license** if you remix,
  transform, or build upon the data;
- **do not apply legal or technological measures** that restrict others from
  doing anything the license permits.

The full legal code is in [`LICENSE-CC-BY-SA-4.0.txt`](LICENSE-CC-BY-SA-4.0.txt).

## Code — MIT

Everything under `build/`, `import/`, `oedb/`, `test/`, `web/`, `schema/`, and `.github/` — the
tooling, testing suites, schemas, and pipeline that validate source files and generate the
database — is original work and is licensed under the
**MIT License**, see [`LICENSE-MIT.txt`](LICENSE-MIT.txt).

The tooling is separate from the data on purpose: a permissive license lets
other projects reuse the build pipeline and library modules without inheriting ShareAlike
obligations on their own software.

---

## Upstream provenance

This database began as a fork of the exercise data from the
[wger project](https://github.com/wger-project/wger). wger licenses its
exercise data **per entry**, not under a single blanket license. As of the
import (2026-09-02, 871 exercises / 3,336 translations) the distribution was:

| Original license | Translations |
|---|---|
| CC BY-SA 4.0 | 2,918 |
| CC BY-SA 3.0 | 333 |
| CC0 1.0 | 85 |

Each imported record retains its original license and author in an `upstream`
block, and those values are carried through into every published database as
the `upstream_license` / `upstream_license_author` columns. Nothing about the
relicensing is hidden — it is auditable per row.

CC BY-SA 3.0 permits distributing adaptations under a later version of the same
license, and CC0 material carries no restrictions, so the combined work is
distributed under CC BY-SA 4.0. Original attribution is preserved regardless of
the outbound license.

wger's application code is AGPL-3.0-or-later. **No wger code is used in this
repository** — only data obtained through its public API.

> This section describes our reading of the applicable license terms. It is not
> legal advice.

[cc-by-sa-4]: https://creativecommons.org/licenses/by-sa/4.0/
