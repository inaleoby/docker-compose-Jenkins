import pytest
from app import app, db, Student

# Configuration de test : base SQLite en mémoire
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()  # donne accès au client de test
        db.session.remove()
        db.drop_all()

def test_index(client):
    """La page index.html doit répondre avec code 200"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'GESTION DES ETUDIANTS' in response.data

def test_add_student(client):
    """Ajouter un étudiant via le formulaire"""
    response = client.post('/add', data={'name': 'Alice'}, follow_redirects=True)
    assert response.status_code == 200

    students = Student.query.all()
    assert len(students) == 1
    assert students[0].name == 'Alice'

def test_get_students(client):
    """Tester l'API /api/students"""
    db.session.add(Student(name="Bob"))
    db.session.commit()

    response = client.get('/api/students')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == "Bob"

def test_delete_student(client):
    """Tester la suppression"""
    s = Student(name="Charlie")
    db.session.add(s)
    db.session.commit()

    response = client.get(f'/delete/{s.id}', follow_redirects=True)
    assert response.status_code == 200

    student = Student.query.get(s.id)
    assert student is None
