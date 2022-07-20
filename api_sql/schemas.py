from pydantic import BaseModel


class EmbedItem(BaseModel):
    uuid: str
    owner_id: str
    date_added: str
    title: str
    description: str
    embed_name: str
    embed_description: str
    embed_inline: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    user_uuid: str
    username: str
    date_joined: str
    is_active: bool

    class Config:
        orm_mode = True
