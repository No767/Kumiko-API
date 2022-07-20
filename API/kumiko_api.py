import sys
import uuid
from datetime import datetime
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from api_sql import CrudMethods
from api_sql.db import SessionLocal

app = FastAPI()
utils = CrudMethods()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


class EmbedItemPost(BaseModel):
    title: str
    description: str
    embed_name: str
    embed_description: str
    embed_inline: bool


@app.get("/embed-items/{uuid}", response_class=ORJSONResponse)
async def get_embed(uuid: str, db: Session = Depends(get_db)):
    embed_item = await utils.get_embed_item(uuid)
    if not embed_item:
        raise HTTPException(status_code=404, detail="Embed item not found")
    return embed_item


@app.post("/embed-items/{owner_id}", status_code=200, response_class=ORJSONResponse)
async def post_embed(owner_id: str, item: EmbedItemPost, db: Session = Depends(get_db)):
    itemUUID = str(uuid.uuid4())
    today = datetime.now().isoformat()
    await utils.post_embed_item(
        uuid=itemUUID,
        owner_id=owner_id,
        date_added=today,
        title=item.title,
        description=item.description,
        embed_name=item.embed_name,
        embed_description=item.embed_description,
        embed_inline=item.embed_inline,
    )
    return {"status": "success"}
