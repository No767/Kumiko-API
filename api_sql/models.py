from sqlalchemy import Boolean, Column, String, Text

from .db import Base


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
