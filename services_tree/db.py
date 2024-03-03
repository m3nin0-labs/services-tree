#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from datetime import datetime
from uuid import UUID, uuid4

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlmodel import Field, SQLModel

from services_tree.config import settings


#
# Models
#
class Service(SQLModel, table=True):
    """Service model."""

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    """Service ID."""

    name: str = Field(nullable=False, index=True)
    """Service name."""

    description: str = Field(nullable=False, index=True)
    """Service description."""

    url: str = Field(nullable=False)
    """Service URL."""

    created: datetime = Field(nullable=False, default_factory=datetime.now)
    """Service creation datetime."""

    updated: datetime = Field(nullable=False, default_factory=datetime.now)
    """Service update datetime."""


#
# Utilities
#

# Database engine
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

# Database session
Session = scoped_session(sessionmaker(engine))

#
# CLI
#

cli = typer.Typer()


@cli.command()
def createdb():
    """Create database table."""
    SQLModel.metadata.create_all(bind=engine)


def init_cli(typer_app: typer.Typer):
    """Initialize module CLI."""
    typer_app.add_typer(cli, name="database")
