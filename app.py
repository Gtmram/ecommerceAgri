from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)  
    description = db.Column(db.Text, nullable=True) 
    rating = db.Column(db.Float, nullable=True) 
    image_url = db.Column(db.String(200), nullable=True)
    in_stock = db.Column(db.Boolean, default=True)

    def __repr__(self)->str:
        return f"{self.name}-{self.price}{self.in_stock}"
has_run_before = False

@app.before_request
def before_request():
    global has_run_before
    if not has_run_before:
        db.create_all()  
        has_run_before = True 

@app.route('/')
def Home():
    products = Product.query.all()
    return render_template("frontpage.html",title="Home",products=products)

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
