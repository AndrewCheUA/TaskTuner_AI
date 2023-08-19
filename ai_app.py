from flask import Flask, render_template, request, redirect, url_for

from app.database.models import User, UserProfile, Goal, Task, Habit
from app.database.connect import session

from app.openai_promts import goals_proposition

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    preferred_hours = request.form.get('preferred_hours')
    hold_back = request.form.get('hold_back')
    start_preference = request.form.get('start_preference')

    user_profile = UserProfile(name=name, preferred_hours=preferred_hours, hold_back=hold_back,
                               start_preference=start_preference)
    session.add(user_profile)
    session.commit()

    user = User(id=user_profile.id, username=name, email=f"temp{user_profile.id}@mail.com", password="password")
    session.add(user)
    session.commit()
    # active_goal_count = session.query(Goal).filter_by(user_id=user_profile.id, is_active=True).count() UPDATE USER PROFILE

    return redirect(url_for('set_goals', user_id=user_profile.id))


@app.route('/set_goals', methods=['GET', 'POST'])
def set_goals():
    user_id = request.args.get('user_id')

    if request.method == 'POST':
        goal_titles = request.form.getlist('goal_title[]')
        goal_descriptions = request.form.getlist('goal_description[]')

        for title, description in zip(goal_titles, goal_descriptions):
            if title and description:
                goal = Goal(title=title, description=description, user_id=user_id)
                session.add(goal)
        session.commit()
        return redirect(url_for('set_tasks', user_id=user_id))

    return render_template('set_goals.html')


@app.route('/set_tasks', methods=['GET', 'POST'])
def set_tasks():
    user_id = request.args.get('user_id')

    if request.method == 'POST':
        task_titles = request.form.getlist('task_title[]')
        task_descriptions = request.form.getlist('task_description[]')
        task_due_dates = request.form.getlist('task_due_date[]')

        for title, description, due_date in zip(task_titles, task_descriptions, task_due_dates):
            if title and description:
                task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
                session.add(task)
        session.commit()
        return redirect(url_for('user_profile', user_id=user_id))  # Redirect back to the user profile page

    return render_template('set_tasks.html', user_id=user_id)


@app.route('/user_profile/<int:user_id>')
def user_profile(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        profile_page = session.query(UserProfile).filter_by(id=user_id).first()
        goals = session.query(Goal).filter_by(user_id=user_id).all()
        tasks = session.query(Task).filter_by(user_id=user_id).all()
        habits = session.query(Habit).filter_by(user_id=user_id).all()
        return render_template('user_profile.html', user_id=user_id, user=user, user_profile=profile_page, goals=goals,
                               tasks=tasks, habits=habits)
    else:
        # Handle case when user is not found
        return "User not found"


@app.route('/goal_propositions/<int:user_id>')
def goal_propositions(user_id):
    # Retrieve existing goals from the database
    existing_goals = session.query(Goal).filter_by(user_id=user_id).all()

    # Generate goal propositions
    propositions = goals_proposition(existing_goals)

    return render_template('goal_propositions.html', user_id=user_id, propositions=propositions)


if __name__ == '__main__':
    app.run(debug=True)
