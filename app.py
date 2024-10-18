from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Predefined lists for genres, themes, and character types
genres = ["Mystery", "Fantasy", "Sci-Fi", "Romance", "Adventure", "Horror", "Historical Fiction", "Thriller", "Comedy", "Supernatural"]
themes = ["Love", "Betrayal", "Adventure", "Survival", "Redemption", "Friendship", "Courage", "Revenge", "Sacrifice", "Discovery"]
characters = ["Hero", "Villain", "Sidekick", "Mentor", "Anti-hero", "Detective", "Rebel", "Outsider", "Sage", "Explorer"]

# Feedback storage
feedback_log = []  # In-memory list to store feedback

# Function to generate a random story prompt
def generate_prompt():
    genre = random.choice(genres)
    theme = random.choice(themes)
    character = random.choice(characters)
    return f"Write a {genre} story about {theme} where the main character is a {character}."

# Route to handle the main page and story generation
@app.route('/', methods=['GET', 'POST'])
def index():
    story_prompt = ""  # Initialize prompt
    if request.method == 'POST':
        # Generate a new prompt if user submits the form
        story_prompt = generate_prompt()
    return render_template('index.html', prompt=story_prompt)

# Route to handle feedback submission
@app.route('/feedback', methods=['POST'])
def feedback():
    prompt = request.form['prompt']
    feedback = request.form['feedback']
    comments = request.form.get('comments', '')  # Optional comments
    
    # Store the feedback in a list (or you could log it to a file)
    feedback_log.append({
        'prompt': prompt,
        'feedback': feedback,
        'comments': comments
    })
    
    # Optionally, log to a file
    with open('feedback_log.txt', 'a') as log_file:
        log_file.write(f"Prompt: {prompt}\nFeedback: {feedback}\nComments: {comments}\n---\n")
    
    # Redirect back to the main page or show a thank-you message
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
