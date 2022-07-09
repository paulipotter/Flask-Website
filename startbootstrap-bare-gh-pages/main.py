from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from functools import wraps
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

info = {
    'email': 'dev DOT paulamendez AT gmail DOT com',
    'name': 'Paula Mendez',
    'nickname': 'paulipotter',
    'github': 'https://github.com/paulipotter',
    'linkedin': 'https://www.linkedin.com/in/paulamendez1/',
    'year': datetime.today().year,
    'title': 'Paula Mendez',
    'location': 'San Diego, CA'
}


@app.context_processor
def inject_contact_info():
    return dict(info=info)


@app.route('/')
def home():
    return render_template("index.html", info=info)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    inject_contact_info()
    app.run(host='0.0.0.0', port=5000, debug=True)