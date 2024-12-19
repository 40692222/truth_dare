from app import db, TruthDare, app

# Sample Truths and Dares
truths_and_dares = [
    {"type": "truth", "difficulty": "easy", "content": "What is your favorite color?"},
    {"type": "dare", "difficulty": "easy", "content": "Do 10 push-ups."},
    {"type": "truth", "difficulty": "medium", "content": "Have you ever cheated on a test?"},
    {"type": "dare", "difficulty": "medium", "content": "Sing a song loudly."},
    {"type": "truth", "difficulty": "hard", "content": "What is your deepest secret?"},
    {"type": "dare", "difficulty": "hard", "content": "Call a random person and tell them a joke."},

]

# Ensure the application context is active
with app.app_context():
    db.create_all()  # Create the database tables if not already present
    for item in truths_and_dares:
        # Check if the question already exists in the database
        existing_item = TruthDare.query.filter_by(content=item['content']).first()
        if not existing_item:
            new_item = TruthDare(**item)
            db.session.add(new_item)
    db.session.commit()
    print("Database populated!")
