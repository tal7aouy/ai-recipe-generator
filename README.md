# Recipe Creator and Meal Planner

This project is a web application that uses AI to generate recipes and create meal plans. Built with Python and Flask, it leverages the Anthropic API to provide personalized recipe suggestions and meal planning based on user inputs such as ingredients, cuisine preferences, dietary restrictions, and calorie goals.

## Features

- **Recipe Creator**: Generate recipes based on available ingredients, cuisine style, and dietary restrictions.
- **Meal Planner**: Create customized meal plans for a specified number of days, considering dietary preferences and calorie targets.
- **User-friendly Web Interface**: Easy-to-use forms for inputting preferences and viewing results.
- **AI-Powered Suggestions**: Utilizes the Anthropic API to generate creative and tailored recipes and meal plans.

## Technology Stack

- **Backend**: Python 3.10+, Flask
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **AI Integration**: Anthropic API
- **Additional Libraries**: requests, python-dotenv

## Setup and Installation

1. Clone the repository:

```
git clone https://github.com/tal7aouy/ai-recipe-planner.git
cd ai-recipe-planner
```

2. Set up a virtual environment:

```python
python -m venv venv
# Mac & Linux
source venv/bin/activate
# On Windows use
venv\Scripts\activate
```

3. Install required packages:

```python
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Anthropic API key:

```
ANTHROPIC_API_KEY='sk-*****'
FLASK_ENV=development
```

5. Run the Flask application:

```sh
flask run
```

6. Open a web browser and navigate to `http://localhost:5000`
