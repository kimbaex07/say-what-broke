[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kimbaex07/say-what-broke/rank.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kimbaex07/say-what-broke/reward.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

One line of error copy that tells the user the brutal truth — and makes them laugh on the way.

## The line

> The server ran out of disk space mid-save and gave up without telling anyone. Your work is still in this tab — copy it somewhere safe before you close it.

154 characters, no trailing newline — comfortably inside the 200-character limit.

## Why it fits the brief

- **It names the real failure in plain words:** the server ran out of disk space in the middle of saving. No vague apology, no "something went wrong".
- **It tells the user what to do next:** the work is still in the tab, so copy it somewhere safe before closing. The line is useful, not just funny.
- **It is funny on a single read:** the server "gave up without telling anyone" — the quiet, cowardly failure everyone who has ever lost a save recognises instantly, and it is the kind of line people repeat to a colleague.
- **It would survive in a real product dialog:** honest, specific, and actionable, with no shock value and nothing a team would be embarrassed to ship.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-say-what-broke python3 main.py
```

`main.py` (pure Python standard library) reads `entry.txt` beside it, validates it is 1–200 characters, and writes its exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output`), mode 0644. It writes only to the output directory, never beside its own source.
