from app.database.connect import session
from app.database.models import User, UserProfile, Goal, Task, Habit


db_existing_goals = session.query(Goal).filter_by(user_id=9).all()
existing_goals = ""
for goal in db_existing_goals:
    existing_goals += f"Goal id: {goal.id}; Goal Title: {goal.title}; Description: {goal.description}\n"

print(existing_goals)