from app import db, create_app
from app import models

app = create_app()
with app.app_context():
    user = models.User(username = "Serah",email = "serahnams@gmail.com")
    user.set_password("1234")
    db.session.add(user)
    db.session.commit()