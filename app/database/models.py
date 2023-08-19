import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
# from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()


class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    preferred_hours = Column(String(550), nullable=False)
    hold_back = Column(String(550), nullable=False)
    start_preference = Column(String(550), nullable=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    active_goals = Column(Integer())
    created_at = Column('created_at', DateTime, default=func.now())
    is_active = Column(Boolean, default=False)


class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    description = Column(String(250), nullable=False)
    done = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    description = Column(String(550), nullable=False)
    finished_at = Column('finished_at', DateTime)  # Corrected column name
    done = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    goal_id = Column(Integer, ForeignKey('goals.id', ondelete='SET NULL'))


class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    description = Column(String(550), nullable=False)
    done = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    goal_id = Column(Integer, ForeignKey('goals.id', ondelete='SET NULL'))

