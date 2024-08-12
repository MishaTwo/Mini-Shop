from flask import Flask
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from .models.base import create_db
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config["SECKRET_KEY"] = os.getenv("SECKRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFCATION"] = os.getenv("STM")

login_manager = LoginManager()
login_manager.init_app(app)

create_db()

@app.context_processor
def inject():
    return {"now": datetime.now()}