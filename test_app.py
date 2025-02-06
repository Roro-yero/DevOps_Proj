import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Utilisation d'une DB temporaire
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200  # Vérifie que la page d'accueil fonctionne

# def test_create_user(client):
#     response = client.post("/users", json={"name": "Alice"})
#     assert response.status_code == 200  # Vérifie que la requête fonctionne
#     assert "Utilisateur ajouté" in response.data.decode("utf-8")

