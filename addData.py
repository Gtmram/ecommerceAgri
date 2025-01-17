from app import app, db, Product  # Import the app, db, and Product model

# Create an application context
with app.app_context():
    # Create a new product instance
    new_product = Product(
        name="Fresh Cauliflower", 
        price=6, 
        description="Crisp, juicy, and sweet apples freshly picked from organic farms.", 
        rating=0,
        in_stock=True,
        image_url="https://th.bing.com/th/id/R.0d1381daaca3c82b3c2e7584cf6b938b?rik=Y3XEuT0DCrwI1Q&pid=ImgRaw&r=0"
    )

    # Add the product to the session
    db.session.add(new_product)

    # Commit the session to the database
    db.session.commit()

    print("Product added successfully!")
