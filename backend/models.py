from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class NavigationUrl(Base):
    __tablename__ = 'navigation_urls'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    icon = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow) 