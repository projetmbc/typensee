#!/usr/bin/env python3

from cbutils.core import *

import tomli

# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent
SRC_DIR  = THIS_DIR.parent

TOML_PYPROJ_FILE = SRC_DIR / "pyproject.toml"
MD_DEPS_FILE     = SRC_DIR / "readme" / "deps.md"


PATTERN_NAME_VERSION = re.compile(r"([^=<>~!]+)>=(.+)")

MD_HEADER = """
Dependencies
------------

Here are the `Python` libraries used. The version numbers in brackets are those used prior to the release of this version of the project.
""".lstrip()

MD_NO_DEPS_FOUND = """
<!--
If a 'pyproject.toml' file is in the project root folder, it will be
used to create content in this file listing the project's dependencies.
-->
""".lstrip()


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# No 'pyproject.toml' file.
if not TOML_PYPROJ_FILE.is_file():
    logging.warning(
        msg_title(
            title = 'Deps',
            desc  = f"No '{TOML_PYPROJ_FILE.name} file.",
        )
    )

    content = MD_NO_DEPS_FOUND

# There is a 'pyproject.toml' file.
else:
    logging.info(
        msg_creation_update(
            context = f"'{MD_DEPS_FILE.relative_to(SRC_DIR)}'",
            upper   = False,
        )
    )

    with TOML_PYPROJ_FILE.open("rb") as f:
        data = tomli.load(f)

    deps = data.get("project", {}).get("dependencies", [])

    content = [MD_HEADER]

    for dep in deps:
        match = PATTERN_NAME_VERSION.match(dep)

        if match is None:
            raise ValueError("BUG!")

        name  = match.group(1)
        nbver = match.group(2)

        content.append(f"  * `{name}`   **[{nbver}]**")

    content.append('')
    content = "\n".join(content)

# Let's write the content.
MD_DEPS_FILE.touch()
MD_DEPS_FILE.write_text(content)
