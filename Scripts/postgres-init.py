import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, String, Text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


import asyncio

load_dotenv()

POSTGRES_PASSWORD = os.getenv("Postgres_Password_Dev")
POSTGRES_SERVER_IP = os.getenv("Postgres_Server_IP_Dev")
POSTGRES_USERNAME = os.getenv("Postgres_Username_Dev")
POSTGRES_DB = os.getenv("Postgres_DB_Dev")
POSTGRES_PORT = os.getenv("Postgres_Server_Port_Dev")

POSTGRES_DB_URL = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:{POSTGRES_PORT}/{POSTGRES_DB}"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_uuid = Column(String, primary_key=True)
    username = Column(String)
    date_joined = Column(String)
    is_active = Column(Boolean, default=True)

    def __iter__(self):
        yield "user_uuid", self.user_uuid
        yield "username", self.username
        yield "date_joined", self.date_joined
        yield "is_active", self.is_active

    def __repr__(self):
        return f"User(user_uuid={self.user_uuid}, username={self.username}, date_joined={self.date_joined}, is_active={self.is_active})"


class EmbedItem(Base):
    __tablename__ = "embeds_data"

    uuid = Column(String, primary_key=True)
    owner_id = Column(String)
    date_added = Column(String)
    title = Column(String)
    description = Column(Text)
    embed_name = Column(String)
    embed_description = Column(Text)
    embed_inline = Column(Boolean, default=True)

    def __iter__(self):
        yield "uuid", self.uuid
        yield "owner_id", self.owner_id
        yield "date_added", self.date_added
        yield "title", self.title
        yield "description", self.description
        yield "embed_name", self.embed_name
        yield "embed_description", self.embed_description
        yield "embed_inline", self.embed_inline

    def __repr__(self):
        return f"EmbedItem(uuid={self.uuid}, owner_id={self.owner_id}, date_added={self.date_added}, title={self.title}, description={self.description}, embed_name={self.embed_name}, embed_description={self.embed_description}, embed_inline={self.embed_inline})"


async def main():
    engine = create_async_engine(
        f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_IP}:5432/{POSTGRES_DB}",
        echo=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(main())
