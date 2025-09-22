#!/usr/bin/env python3

from cbutils.core.constants import *
from cbutils.core.logconf   import *


# ----------------------- #
# -- STANDARD MESSAGES -- #
# ----------------------- #

###
# prototype::
#     title : a title.
#     desc  : a short description.
#
#     :return: see inside the code.
###
def msg_title(
    title: str,
    desc : str,
) -> str:
    return f"{title.upper()} - {desc}"


###
# prototype::
#     context : context in which codes are created or updated.
#     upper   : set to ''True'', the context is printed in uppercase;
#               otherwise, no case changes are made.
#     several : set to ''True'', this indicates that several codes
#               are involved; otherwise, only one is processed.
#
#     :return: see inside the code.
###
def msg_creation_update(
    context: str,
    upper  : bool = True,
    several: bool = False,
) -> str:
    if upper:
        context = context.upper()

    plurial = 's' if several else ''

    return f"{context} code{plurial}: creation or update."


# ---------------------- #
# -- LOGGING MESSAGES -- #
# ---------------------- #

def log_raise_error(
    exception: Exception,
    context  : str,
    desc     : str,
    xtra     : str = '',
) -> None:
    logging.error(
        msg_title(
            title = context,
            desc  = desc
        )
    )

    if xtra:
        xtra = f" {xtra}"

    raise exception(f"{desc}{xtra}")
