from flask import Flask, render_template, request, jsonify
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)

# Initialize the ChatAnthropic model
model = ChatAnthropic(
    model="claude-3-opus-20240229", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Create a prompt for recipe creation
recipe_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that creates recipes."),
        (
            "human",
            "Create a recipe using the following ingredients: {ingredients}. The cuisine style should be {cuisine}. Consider these dietary restrictions: {dietary_restrictions}.",
        ),
    ]
)

# Create a prompt for meal planning
meal_plan_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that creates meal plans."),
        (
            "human",
            "Create a {days}-day meal plan considering these dietary preferences: {dietary_preferences}. Each day should total approximately {calories} calories.",
        ),
    ]
)

# Create chains
recipe_chain = recipe_prompt | model
meal_plan_chain = meal_plan_prompt | model


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    try:
        ingredients = request.form["ingredients"]
        cuisine = request.form["cuisine"]
        dietary_restrictions = request.form["dietary_restrictions"]

        result = recipe_chain.invoke(
            {
                "ingredients": ingredients,
                "cuisine": cuisine,
                "dietary_restrictions": dietary_restrictions,
            }
        )

        return jsonify({"recipe": result.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/create_meal_plan", methods=["POST"])
def create_meal_plan():
    try:
        days = request.form["days"]
        dietary_preferences = request.form["dietary_preferences"]
        calories = request.form["calories"]

        result = meal_plan_chain.invoke(
            {
                "days": days,
                "dietary_preferences": dietary_preferences,
                "calories": calories,
            }
        )

        return jsonify({"meal_plan": result.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
