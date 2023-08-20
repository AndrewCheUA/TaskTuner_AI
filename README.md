# Goal Tracker Web Application

The **Goal Tracker Web Application** is a Flask-based web application designed to help users set and track their goals, tasks, and habits. With this application, users can create and manage their personal goals, break them down into tasks, and receive AI-generated task propositions based on their preferences and existing commitments.

## Features

- **User Profiles**: Users can create personalized profiles with their name, preferred working hours, hold-backs and day start preferences.

- **Goal Setting**: Users can set their goals by providing titles and descriptions. The application allows users to track their progress toward each goal.

- **Task Management**: Users can create tasks related to their goals. Each task includes a title, description, and due date. Users can mark tasks as completed as they make progress.

- **AI-Generated Goal Propositions**: The application utilizes AI-generated goal propositions to provide users with suggestions for new goals based on their preferences and existing commitments.

- **AI-Generated Task Propositions**: The application also suggests tasks that align with users' goals and schedules, making it easier to manage their time effectively.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Set up your database configuration in `app.database.connect` to establish a connection to your chosen database.

3. Run the application by executing `python ai_app.py`. The application will start a development server and can be accessed via a web browser.

4. Navigate to the application's various routes to create user profiles, set goals, manage tasks, and receive AI-generated propositions.

5. Experience seamless goal and task tracking along with personalized recommendations to enhance your productivity.

## Dependencies

- Flask
- SQLAlchemy
- OpenAI GPT-3 (for AI-generated propositions)
- LangChain

## Contributors

- Artur
- Andrii

## License

This project is licensed under the [MIT License](LICENSE).
