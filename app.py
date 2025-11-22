from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Deployment Successful! Flask App Running in a Docker Container on EC2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2525)