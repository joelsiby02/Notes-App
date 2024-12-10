
# import deps
from flask import Flask

# Create a fn to make an app on flask
def create_app():
    app = Flask(__name__)
    
    
    # import the blueprionts
    
    from .views import views
    from.auth import auth
    
    # register the blueprints
    
    app.register_blueprint(views, url_prefix = '/')   
    app.register_blueprint(auth, url_prefix = '/')
    
    
    return app