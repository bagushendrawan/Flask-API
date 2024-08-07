from api import create_app
from flask import jsonify
import os

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))