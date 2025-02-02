from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set up the database URI (SQLite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Movie database model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database tables (only need to run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Fetch all movies from the database
    movies = Movie.query.all()
    return render_template('a.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
