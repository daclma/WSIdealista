from config import Config
from flask import Flask
from routes.process_url_routes import process_url_routes
from flask_mail import Mail
from extensions import db, mail

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize mail service
mail = Mail()
mail.init_app(app)

# Register blueprints
app.register_blueprint(process_url_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)