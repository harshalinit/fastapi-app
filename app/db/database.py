from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "postgresql+asyncpg://superuser:magnumopus@localhost:5432/app"

engine = create_async_engine(DATABASE_URL)

SessionFactory = async_sessionmaker(engine)

async def get_session():
    async with SessionFactory() as session:
        yield session
    