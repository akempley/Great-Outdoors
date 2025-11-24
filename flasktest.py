from flask import Flask

app = Flask(__name__)

hikes = [
    {"id": 1, "name": "Easy Trail", "difficulty": "easy"},
    {"id": 2, "name": "Medium Hike", "difficulty": "moderate"},
    {"id": 3, "name": "Hard Climb", "difficulty": "difficult"}
]

@app.route('/')
def home():
    return "<h1>Hiking Trails</h1><p>Simple page works!</p>"

if __name__ == '__main__':
    app.run(debug=True)