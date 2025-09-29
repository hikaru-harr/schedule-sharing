from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal  # あなたのasync用SessionFactory

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session