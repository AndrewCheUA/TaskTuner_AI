from flask import Flask, render_template, request, redirect, url_for

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

    # Process the data or save it to a database if needed
    # ...

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
