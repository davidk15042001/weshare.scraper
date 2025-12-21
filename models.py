from sqlalchemy import Boolean, Column, Integer, String, Float, Table, ForeignKey, DateTime, CheckConstraint, Text, BigInteger, Date, func
from database import Base


class GithubScrape(Base):
    __tablename__ = "github_scrape"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(127), nullable=False)
    last_name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(15), nullable=True)
    country = Column(String(63), nullable=True)
    platform = Column(Text, nullable=True)
    title = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)


class GitlabScrape(Base):
    __tablename__ = "gitlab_scrape"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(127), nullable=False)
    last_name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(15), nullable=True)
    country = Column(String(63), nullable=True)
    platform = Column(Text, nullable=True)
    title = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)


class StackOverflowScrape(Base):
    __tablename__ = "stack_overflow_scrape"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(127), nullable=False)
    last_name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(15), nullable=True)
    country = Column(String(63), nullable=True)
    platform = Column(Text, nullable=True)
    title = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)


class VimeoScrape(Base):
    __tablename__ = "vimeo_scrape"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(127), nullable=False)
    last_name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(15), nullable=True)
    country = Column(String(63), nullable=True)
    platform = Column(Text, nullable=True)
    title = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)


class GoogleScrape(Base):
    __tablename__ = "serp_api_scrape"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(127), nullable=False)
    last_name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(15), nullable=True)
    country = Column(String(63), nullable=True)
    platform = Column(Text, nullable=True)
    title = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    snippet = Column(Text, nullable=True)