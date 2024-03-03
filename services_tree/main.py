#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services_tree import __version__
from services_tree.config import settings
from services_tree.routes import router

#
# Application
#
app = FastAPI()

#
# Middleware
#
app.add_middleware(CORSMiddleware, **settings.CORS)

#
# Routes
#
app.include_router(router)


#
# Index
#
@app.get("/")
async def index():
    """Application frontpage."""
    return {"name": "Services Tree", "version": __version__}


#
# Debug entry point
#
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
