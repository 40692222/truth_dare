from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///truth_dare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the TruthDare model
class TruthDare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # 'truth' or 'dare'
    difficulty = db.Column(db.String(10), nullable=False)  # 'easy', 'medium', 'hard'
    content = db.Column(db.Text, nullable=False)  # Question or challenge text

# Application routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        difficulty = request.form.get("difficulty", "easy")
        t_or_d = request.form.get("type", "truth")
        question = TruthDare.query.filter_by(type=t_or_d, difficulty=difficulty).first()
        if question:
            return render_template("play.html", question=question.content)
        return "No questions available for the selected type and difficulty."
    return render_template("play.html", question=None)


# Run the application
if __name__ == "__main__":
    # Ensure the application context is active when initializing the database
    with app.app_context():
        db.create_all()  # Create the database tables if not already present
    app.run(debug=True)
