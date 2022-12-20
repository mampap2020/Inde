from src.models.database import Database

from src.models.cookie import Cookie
from hashlib import sha256

def login(mail, mdp):
    db = Database()
    mdp = sha256 (mdp.encode(encoding="utf-32")).hexdigest()
    
    res = db.execute(f"SELECT * FROM users WHERE email='{mail}' AND  password='{mdp}'").fetchone()

    
    if res != None:
        c = Cookie("data.json")
        c.update({"mail": res[1], "uid":res[0]})
        return True
    else:

        return False
def logout():
    c = Cookie("data.json")
    c.clean()
def signin(email, mdp):
    db = Database()
    mdp = sha256 (mdp.encode(encoding="utf-32")).hexdigest
    db = (f"INSERT INTO users(email,password) VALUES ({email,mdp})")
    db.commit()



