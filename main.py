#!/usr/bin/env python3
"""Write the error-copy line from entry.txt to the output directory.

Reads entry.txt next to this script, validates it is 1..200 characters
of non-whitespace text, and writes its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output"), mode 0644.
Writes only to the output directory, never beside the source.
Pure Python standard library.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    try:
        data = source.read_bytes()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        print("entry.txt is not valid UTF-8", file=sys.stderr)
        return 1

    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry.txt must be 1..{MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(data)
    os.chmod(out_path, 0o644)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
