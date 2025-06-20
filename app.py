from flask import Flask, render_template
from tools.mainsail import mainsail_bp
from tools.gennaker import gennaker_bp

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Register tools
app.register_blueprint(mainsail_bp)
app.register_blueprint(gennaker_bp)

# Production startup
import os
port = int(os.environ.get("PORT", 5000))
app.run(debug=False, host='0.0.0.0', port=port)
