from flask import Flask, render_template, request
from models import Question, Result

app = Flask(__name__)

# Question Queue (FIFO)
questions = [
    Question("What is the capital of Nigeria?",
             ["Lagos", "Abuja", "Kano", "Kaduna"],
             "Abuja"),

    Question("Python is a ___?",
             ["Snake", "Programming Language", "Car", "Operating System"],
             "Programming Language"),

    Question("2 + 2 = ?",
             ["3", "4", "5", "6"],
             "4"),

    Question("HTML stands for?",
             ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "Hypertext Makeup Language"],
             "Hyper Text Markup Language"),

    Question("Which planet is known as the Red Planet?",         
           ["Earth", "Mars", "Jupiter", "Saturn"],
             "Mars"),

    Question("What is the largest mammal?",
             ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
             "Blue Whale"),                
]
@app.route("/")
def home():
    return render_template("index.html")

@app.route( "/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST" and "q0" in request.form:
        username = request.form.get("username")
        matric = request.form.get("matric")

        score = 0
        for i in range(len(questions)):
            selected = request.form.get(f"q{i}")
            if questions[i].check_answer(selected):
                score += 1

        return render_template(
            "result.html",
            username=username,
            matric=matric,
            score=score,
            total=len(questions)
        )
    
    if request.method == "POST":
        username = request.form.get("username")
        matric_val = request.form.get("matric") # mathed to index.html
    
        return render_template("quiz.html", questions=questions, username=username, matric=matric_val)
    
    return render_template("index.html", questions=questions)

if __name__ == "__main__" :
    app.run(debug=True)