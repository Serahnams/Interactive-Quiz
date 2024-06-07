from flask import Blueprint, render_template, request, session, redirect, url_for
from app.forms import QuestionsForm
from flask_login import login_required
from datetime import datetime
from app import db
bp = Blueprint("route",__name__ )
# Define total allowed time in seconds, e.g., 600 seconds for 10 minutes
TOTAL_ALLOWED_TIME = 300
def fetch_questions():
    return Question.query.all()

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/instruction")
@login_required
def instruction():
    return render_template("instruction.html")

class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, option4, correctOption):
        self.q_id = q_id 
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3
        elif self.correctOption == 4:
            return self.option4

q1 = Question(1, "What is the capital city of Kenya?", "Kisumu", "Nairobi", "Lusaka", "Dodoma", 2)       
q2 = Question(2, "Which ancient civilization built the pyramids?", "Romans", "Greeks", "Egyptians", "Mayans", 3)
q3 = Question(3, "Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2)
q4 = Question(4, "What force keeps us grounded on the Earth?", "Magnetism", "Friction", "Gravity", "Inertia", 3)
q5 = Question(5, "If a triangle has sides of 3, 4, and 5 units, what type of triangle is it?", "Equilateral", "Isosceles", "Scalene", "Right-angled", 4)


questions_list = [q1, q2, q3, q4, q5]
    
@bp.route("/quiz<int:id>")
@login_required
def quiz(id):
    return render_template("quiz.html", questions_list = questions_list, id=id)

@bp.route("/submitquiz", methods=["POST", "GET"])
def submit():
     correct_Count = 0
     for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form.get(question_id)
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_Count += 1

     return render_template('score.html', correct_Count=correct_Count, questions_list=questions_list)
