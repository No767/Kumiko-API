import asyncio

import uvloop
from sqlalchemy import select

from . import models
from .db import SessionLocal


class CrudMethods:
    def __init__(self):
        self.self = self

    async def get_user_info(self, owner_id: str):
        async with SessionLocal() as session:
            async with session.begin():
                selectItem = select(models.User).filter(
                    models.User.user_uuid == owner_id
                )
                res = await session.execute(selectItem)
                return [row for row in res.scalars()]

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def get_embed_item(self, uuid: str):
        async with SessionLocal() as session:
            async with session.begin():
                selectItem = select(models.EmbedItem).filter(
                    models.EmbedItem.uuid == uuid
                )
                res = await session.execute(selectItem)
                return [row for row in res.scalars()]

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def post_embed_item(
        self,
        uuid: str,
        owner_id: str,
        date_added: str,
        title: str,
        description: str,
        embed_name: str,
        embed_description: str,
        embed_inline: bool,
    ):
        async with SessionLocal() as session:
            async with session.begin():
                insertItem = models.EmbedItem(
                    uuid=uuid,
                    owner_id=owner_id,
                    date_added=date_added,
                    title=title,
                    description=description,
                    embed_name=embed_name,
                    embed_description=embed_description,
                    embed_inline=embed_inline,
                )
                session.add_all([insertItem])
                await session.commit()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
