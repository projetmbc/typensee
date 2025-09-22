#!/usr/bin/env python3

from cbutils.core import *

from multimd import Builder, Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent
PROJ_DIR = THIS_DIR.parent


# ------------------ #
# -- BUILD README -- #
# ------------------ #

for readme_dir in PROJ_DIR.rglob(TAG_README):
    if not readme_dir.is_dir():
        continue

    folder = get_relpath(
        subpath  = readme_dir.parent,
        mainpath = PROJ_DIR
    )

    folder = "main" if str(folder) == '.' else f"'{folder}'"

    logging.info(
        f"'README.md' compilation in the '{folder}' folder."
    )

    readme_file = readme_dir.parent/ f"{readme_dir.name.upper()}.md"

    mybuilder = Builder(
        src   = readme_dir,
        dest  = readme_file,
        erase = True
    )

    mybuilder.build()
