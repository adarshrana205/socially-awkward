from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

import social.db.user as db_user

class User(UserMixin):
  def __init__(self, id, name):
    self.id = id
    self.name = name

def init_login(app):
	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'bp.log_in'

	@login_manager.user_loader
	def load_user(user_id):
            user = db_user.get_user(user_id)
            return User(user['id'], user['name'])

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=1212,debug=True)
