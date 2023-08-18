from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    active_targets = Column(Integer())
    created_at = Column('created_at', DateTime, default=func.now())
    is_active = Column(Boolean, default=False)

    goals = relationship('Goal', back_populates='user')
    tasks = relationship('Task', back_populates='user')
    habits = relationship('Habit', back_populates='user')


class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    description = Column(String(250), nullable=False)
    done = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = relationship('User', back_populates='goals')


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

    user = relationship('User', back_populates='tasks')
    goal = relationship('Goal', back_populates='tasks')


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

    user = relationship('User', back_populates='habits')
    goal = relationship('Goal', back_populates='habits')


class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    preferred_hours = Column(String(550), nullable=False)
    hold_back = Column(String(550), nullable=False)
    start_preference = Column(String(550), nullable=False)
