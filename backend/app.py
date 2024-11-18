from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 全てのオリジンからのリクエストを許可

# デバッグモードを有効化
app.config["DEBUG"] = True

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
