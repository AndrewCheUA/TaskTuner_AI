# Use Ubuntu-based image
FROM python:3.10.12

# Set environment variable
ENV APP_HOME /app

# Set the working directory inside the container
WORKDIR $APP_HOME

# Copy other files into the container's working directory
COPY . /app

# Update pip to the latest version
RUN pip install --upgrade pip

# Install dependencies inside the container
RUN pip install -r requirements.txt

# Install dotenv
RUN pip install pydantic[dotenv]

# Specify the port where the application runs inside the container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=ai_app.py

# Run our application inside the container
CMD ["flask", "run", "--host=0.0.0.0"]