from app.database.connect import session
from app.database.models import User, UserProfile, Goal, Task, Habit

# db_existing_goals = session.query(Goal).filter_by(user_id=9).all()
# existing_goals = ""
# for goal in db_existing_goals:
#     existing_goals += f"Goal id: {goal.id}; Goal Title: {goal.title}; Description: {goal.description}\n"
#
# print(existing_goals)

text = "Goal id: 1; Goal Title: Read More Books; Description: Set aside two hours each day to read books. Start your day with a cup of coffee to help you stay focused and motivated. If you find yourself feeling lazy, break up the two hours into smaller chunks of time throughout the day. Goal id: 2; Goal Title: Master Financial Literacy and Investment Strategies; Description: Spend two hours each day learning about personal finance, budgeting, saving, investing, and managing debt. Research different investment options such as stocks, bonds, real estate, and entrepreneurship. Take courses, read books, follow reputable financial news sources, and consider seeking advice from financial experts. Goal id: 3; Goal Title: Create Diversified Income Streams; Description: Spend two hours each day researching and exploring opportunities to create multiple streams of income. Prioritize opportunities that align with your skills, interests, and long-term financial goals. Consider starting a side business, investing in dividend-paying stocks, generating passive income through real estate investments, or creating and selling digital products."

# Split the text into individual goal sections
goal_sections = text.split("Goal id: ")[1:]

new_goals = []
# Process each goal section
for goal_section in goal_sections:
    goal_info = goal_section.split("; ")
    goal = {"goal_id": int(goal_info[0]), "goal_title": goal_info[1].split(": ")[1],
            "goal_description": goal_info[2].split(": ")[1]}
    new_goals.append(goal)


new_goal={'goal_id': 3, 'goal_title': 'Create Diversified Income Streams', 'goal_description':
    'Spend two hours each day researching and exploring opportunities to create multiple streams of income.'
    'Prioritize opportunities that align with your skills, interests, and long-term financial goals. Consider starting'
    'a side business, investing in dividend-paying stocks, generating passive income through real estate investments,'
    'or creating and selling digital products.'}

print(new_goal['goal_description'])
