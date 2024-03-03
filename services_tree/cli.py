#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from importlib import import_module

import typer

app = typer.Typer()

#
# CLIs
#
CLI_MODULES = ["services_tree.db"]

#
# Initializing modules
#
for cli_module in CLI_MODULES:
    mod = import_module(cli_module)

    mod.init_cli(app)
