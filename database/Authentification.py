from flask import Flask, session,redirect, render_template,request

app = Flask(__name__)
app.secret_key="1234567890"

password="1234"
@app.route('/')
def index():
    if "user" in session and session['user']==password:
        return "Привет"
    return redirect('/login')

@app.route('/new')
def new():
    if "user" in session and session['user']=="1234":
        return "Привет new"
    return "Доступ к этой странице запрещен"

@app.route('/login', methods=["GET",'POST'] )
def sesssions():
    if request.method=="POST":
        passIn=request.form['password']
        if passIn==password:
            session['user'] = passIn
            return redirect('/')
    return render_template("passwd.html")

@app.route('/logout')
def logout():
    session.pop('user',None)
    return "Досвидания"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

