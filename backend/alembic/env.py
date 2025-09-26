from __future__ import annotations

import os
import sys
import pkgutil
import importlib
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

# --- Alembic config & logging ---
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Ensure project root on sys.path (alembic/.. = backend/) ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# --- Load settings / Base ---
from app.core.config import settings
from app.db.session import Base

# --- Import all model modules so that tables are registered on Base.metadata ---
def import_submodules(package_name: str) -> None:
    pkg = importlib.import_module(package_name)
    for _, modname, _ in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        importlib.import_module(modname)

# app/models 配下の *.py（user.py など）を全読み込み
import_submodules("app.models")

# Alembic が参照するメタデータ
target_metadata = Base.metadata

# --- Offline migration ---
def run_migrations_offline() -> None:
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()

# --- Online migration ---
def do_run_migrations(connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    engine: AsyncEngine = create_async_engine(
        settings.DATABASE_URL,
        poolclass=pool.NullPool,
    )
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await engine.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
