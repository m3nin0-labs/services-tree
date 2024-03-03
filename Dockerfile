#
# Copyright (C) 2024 Services Tree.
#
# Services Tree is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

FROM python:3.9

# Working directory
WORKDIR /app

# Copy application
COPY . .

# Install dependencies
RUN pip install --no-cache-dir .

# Run the migration 
# (this is possible as the application was built to run in a SQLite)
RUN alembic upgrade head

# Base application
CMD ["gunicorn", "services_tree.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
