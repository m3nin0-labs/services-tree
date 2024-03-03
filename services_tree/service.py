#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from datetime import datetime
from typing import List, Union
from uuid import UUID

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import or_

from services_tree.db import Service as ServiceModel
from services_tree.db import Session


def search(
    text: Union[str, None] = None, offset: int = 0, limit: int = 100
) -> List[ServiceModel]:
    """Search service.

    Args:
        text (Union[str, None]): Text query.

        offset (int): Results offset (From which position we should start
                                     to get the results).

        limit (int): Max number of results.

    Returns:
        List[ServiceModel]: List of services.
    """
    results = []

    with Session() as session:
        # building query
        query = session.query(ServiceModel)

        if text:
            query = query.filter(
                or_(
                    ServiceModel.name.ilike(f"%{text}%"),
                    ServiceModel.description.ilike(f"%{text}%"),
                )
            )

        query.offset(offset).limit(limit)
        results = query.all()

    return results


def read(sid: UUID) -> ServiceModel:
    """Read metadata from a given service.

    Args:
        sid (UUID): Service ID.

    Returns:
        ServiceModel: Service metadata
    """
    with Session() as session:
        # building query
        result = session.query(ServiceModel).where(ServiceModel.id == sid).first()

        if not result:
            raise HTTPException(status_code=404, detail="Service not found.")

    return result


def create(document: ServiceModel) -> ServiceModel:
    """Create a new service model into the database.

    Args:
        document (ServiceModel): Service object.

    Returns:
        ServiceModel: New service model registered.
    """
    with Session() as session:
        session.add(document)
        session.commit()

        session.refresh(document)

    return document


def update(sid: UUID, document: ServiceModel) -> ServiceModel:
    """Update a service.

    Args:
        sid (UUID): Service ID.

        document (ServiceModel): Service object.

    Returns:
        ServiceModel: New service model registered.
    """
    allowed_properties = ["name", "description", "url"]

    current_service = read(sid)
    document_json = jsonable_encoder(document)

    has_allowed_properties = any(
        [p in allowed_properties for p in document_json.keys()]
    )

    if not has_allowed_properties:
        raise HTTPException(
            status_code=400,
            detail="Invalid properties. Use `name`, `description`, or `url`.",
        )

    for allowed_property in allowed_properties:
        if allowed_property in document_json:
            setattr(current_service, allowed_property, document_json[allowed_property])

    with Session() as session:
        current_service.updated = datetime.now()

        session.add(current_service)
        session.commit()

        session.refresh(current_service)

    return current_service
