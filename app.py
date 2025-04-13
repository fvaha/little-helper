from flask import Flask, jsonify
from routes import sysinfo, network, docker, db, k8s, pipelines

app = Flask(__name__)

app.register_blueprint(sysinfo.bp)
app.register_blueprint(network.bp)
app.register_blueprint(docker.bp)
app.register_blueprint(db.bp)
app.register_blueprint(k8s.bp)
app.register_blueprint(pipelines.bp)

@app.route("/")
def index():
    return {"message": "Welcome to the Diagnostic API"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
