from flask import Flask, g, request, render_template, flash, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey123'

currentdirectory = os.path.dirname(os.path.abspath(__file__))


def connect_db():
  sql = sqlite3.connect('./database')
  sql.row_factory = sqlite3.Row
  return sql


def get_db():
  if not hasattr(g, 'sqlite3'):
    g.sqlite_db = connect_db()
  return g.sqlite_db


@app.route('/')
def list_users():
  db = get_db()
  cursor = db.execute('SELECT id, name, email FROM users')
  users = cursor.fetchall()
  return render_template('index.html', users=users)


@app.route('/add', methods=('GET', 'POST'))
def add_user():
    if request.method == 'POST':
      name = request.form['name']
      email = request.form['email']

      if not name:
        flash('Name is required!')
      if not email:
        flash('Email is required!')
      else:
        db = get_db()
        db.execute('INSERT INTO users (name,email) VALUES (?,?)', (name, email))
        db.commit()
        db.close()
        return redirect(url_for('list_users'))
    return render_template('add.html')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port = port)