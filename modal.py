# from app import db

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Float, nullable=False)  
#     description = db.Column(db.Text, nullable=True) 
#     rating = db.Column(db.Float, nullable=True) 
#     in_stock = db.Column(db.Boolean, default=True)

#     def __repr__(self)->str:
#         return f"{self.name}-{self.price}{self.in_stock}"