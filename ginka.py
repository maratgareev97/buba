from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("new_file.html")

@app.route('/vs')
def erik():
    erikcool=request.args.get("erikshow")
    return render_template("nasa.html",erikcaren=erikcool)





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
