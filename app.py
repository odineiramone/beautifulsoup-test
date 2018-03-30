from nest import nest
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    json = nest.go_spidey()
    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=True)
