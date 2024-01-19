from flask import Flask, session

app = Flask(__name__)
app.secret_key="1234567890"

password="1234"
@app.route('/')
def index():
    if "user" in session and session['user']==password:
        return "Привет"
    return "Доступ к этой странице запрещен"

@app.route('/new')
def new():
    if "user" in session and session['user']=="1234":
        return "Привет new"
    return "Доступ к этой странице запрещен"

@app.route('/login')
def sesssions():
    passIn=password
    if passIn==password:
        session['user'] = passIn
        return "Пораль верный. Вы можете входить"
    return "Доступ запрещен"

@app.route('/logout')
def logout():
    session.pop('user',None)
    return "Досвидания"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

