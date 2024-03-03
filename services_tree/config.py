#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Configurations handler."""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="ST",
    settings_files=["settings.toml"],
)
