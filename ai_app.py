from flask import Flask, render_template, request, redirect, url_for
from app.database.models import UserProfile
from app.database.connect import session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name')
    preferred_hours = request.form.get('preferred_hours')
    hold_back = request.form.get('hold_back')
    start_preference = request.form.get('start_preference')

    # Save data to the database
    # session = Session()
    user_profile = UserProfile(name=name, preferred_hours=preferred_hours, hold_back=hold_back,
                               start_preference=start_preference)
    session.add(user_profile)
    session.commit()
    session.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
