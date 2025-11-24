from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

<<<<<<< HEAD
# === HIKE DATA ===
hikes = {
    'base-towers': {
        'name': 'Base of the Towers',
        'difficulty': 'challenging',
        'description': 'Iconic hike with emerald lakes.'
    },
    'french-valley': {
        'name': 'French Valley',
        'difficulty': 'moderate',
        'description': 'Stunning glacier views.'
    },
    'grey-glacier': {
        'name': 'Grey Glacier',
        'difficulty': 'easy',
        'description': 'Beautiful glacier views with a boat tour.'
    }
}
# =================


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')


@app.route('/hikes')
def hikes_list():
    """Page showing all hikes"""
    return render_template('hikes_list.html', hikes=hikes)


@app.route('/hike/<hike_id>')
def hike_detail(hike_id):
    """Detail page for a specific hike"""
    hike = hikes.get(hike_id)
    if not hike:
        return "Hike not found", 404
    return render_template('hike_detail.html', hike=hike, hike_id=hike_id)


if __name__ == '__main__':
    # Ensure DB tables exist before starting
    with app.app_context():
        db.create_all()
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

=======
>>>>>>> dfbe10ade20959108e696c6d0b8e9073459f74b2
# Create the database tables
with app.app_context():
    db.create_all()

<<<<<<< HEAD
# === HIKE DATA ===
hikes = {
    'base-towers': {
        'name': 'Base of the Towers',
        'difficulty': 'challenging',
        'description': 'Iconic hike with emerald lakes.'
    },
    'french-valley': {
        'name': 'French Valley',
        'difficulty': 'moderate',
        'description': 'Stunning glacier views.'
    },
    'grey-glacier': {
        'name': 'Grey Glacier',
        'difficulty': 'easy',
        'description': 'Beautiful glacier views with a boat tour.'
    }
}
# =================

=======
>>>>>>> dfbe10ade20959108e696c6d0b8e9073459f74b2
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

<<<<<<< HEAD
@app.route('/hikes')
def hikes_list():
    """Page showing all hikes"""
    return render_template('hikes_list.html', hikes=hikes)

@app.route('/hike/<hike_id>')
def hike_detail(hike_id):
    """Detail page for a specific hike"""
    hike = hikes.get(hike_id)
    if not hike:
        return "Hike not found", 404
    return render_template('hike_detail.html', hike=hike, hike_id=hike_id)

if __name__ == '__main__':
    app.run(debug=True)
    
=======
if __name__ == '__main__':
    app.run(debug=True)

>>>>>>> dfbe10ade20959108e696c6d0b8e9073459f74b2
