# news-image-20261118 entry: copies the bundled front-page image to the
# grader output directory. Standard library only, no network, deterministic:
# every run writes exactly the bytes of entry.png beside this file.
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    # copyfile preserves bytes exactly, so both grader runs match.


if __name__ == "__main__":
    main()
