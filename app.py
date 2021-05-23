from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/facturacion"
app.secret_key = "my_secre_key"
db = SQLAlchemy(app)

# URLs
from resources.access import Access
api.add_resource(Access, '/api/login')

if __name__ == "__main__":
    app.run(debug=True)
