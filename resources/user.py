from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/")
class User(MethodView):
    def get(self):
        return { "message": "Hello, World!" }