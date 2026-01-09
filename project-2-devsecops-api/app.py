from flask import Flask, jsonify

# Initialise the Flask application
# _name_ helps Flask find resources like templates/static files
app = Flask(_name_)

@app.route('/')
def home():
    return jsonify({
        "project": "DevSecOps Secure API",
        "description": "Python Flask API with automated CI/CD and Security Scanning",
        "author": "Ghozlane"
    }), 200

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "checks": {
            "database": "connected",
            "memory": "optimal"
        }
    }), 200

if _name_ == "_main_":
    # Run on 0.00.0 so it is accessible from outside the Docker container
    app.run(host='0.0.0.0', port=5000)