#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Query

from services_tree import service
from services_tree.db import Service as ServiceModel

#
# Application router
#
router = APIRouter(
    prefix="/services", tags=["Service"], responses={404: {"description": "Not found"}}
)


#
# Operations
#
@router.get("/", response_model=List[ServiceModel])
async def search(
    q: Union[str, None] = None,
    offset: int = 0,
    limit: int = Query(default=100, le=1000),
) -> List[ServiceModel]:
    """Search services."""
    return service.search(q, offset, limit)


@router.get("/{sid}", response_model=ServiceModel)
async def read(sid: UUID) -> ServiceModel:
    """Get description of a given service.

    Args:
        sid (UUID): Service ID.

    Returns:
        ServiceModel: Service metadata.
    """
    return service.read(sid)


@router.post("/", response_model=ServiceModel)
async def create(document: ServiceModel) -> ServiceModel:
    """Create a new service.

    Args:
        document (ServiceModel): Service object.

    Returns:
        ServiceModel: New service model registered.
    """
    return service.create(document)


@router.put("/{sid}", response_model=ServiceModel)
async def update(sid: UUID, document: ServiceModel) -> ServiceModel:
    """Update service.

    Args:
        sid (UUID): Service ID.

        document (ServiceModel): Service object.

    Returns:
        ServiceModel: New service model registered.
    """
    return service.update(sid, document)
