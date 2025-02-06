from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")  # Assure-toi d'avoir un dossier templates/
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'

db = SQLAlchemy(app)


# Modèle de base de données
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Routes CRUD
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Utilisateur ajouté !"})

# ✅ Ajoute cette route pour afficher la page HTML
@app.route('/')
def index():
    return render_template("index.html")  # Flask va chercher le fichier dans /templates

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
