from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.db import Base
import datetime

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    text = Column(Text)  # full concatenated text
    pages = Column(Text) # JSON string mapping page->text
