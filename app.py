from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("frontpage.html",title="Home")
@app.route('/features')
def features():
    return render_template("frontpage.html",title="features")
@app.route('/research_data')
def research_data():
    return render_template("frontpage.html",title="research_data")
@app.route('/student_zone')
def student_zone():
    return render_template("frontpage.html",title="student_zone")
@app.route('/contact')
def contact():
    return render_template("frontpage.html",title="contact")

@app.route('/marketplace')
def marketplace():
    return render_template("frontpage.html",title="marketplace")
if __name__ == '__main__':
    app.run(debug=True)
