from app import app
from contacts import contacts
import db  # carga la configuración de MySQL

app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)