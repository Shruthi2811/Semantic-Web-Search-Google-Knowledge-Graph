from flask import Flask, render_template, jsonify
import utilities as util

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/search/<keyword>")
def search(keyword):
	result = util.getResult(keyword)
	return jsonify(**result)

if __name__ == "__main__":
    app.run()
