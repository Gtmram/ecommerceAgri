from app import app, db, Product  # Import the app, db, and Product model

# Create an application context
with app.app_context():
    # Create a new product instance
    new_product = Product(
        name="Fresh Apples", 
        price=5, 
        description="Crisp, juicy, and sweet apples freshly picked from organic farms.", 
        rating=4.5, 
        in_stock=True,
        image_url="https://foodfornet.com/wp-content/uploads/Fresh-red-apples-and-a-few-apple-halves-in-a-pile.jpg"
    )

    # Add the product to the session
    db.session.add(new_product)

    # Commit the session to the database
    db.session.commit()

    print("Product added successfully!")
