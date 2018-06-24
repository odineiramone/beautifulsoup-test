from nest import nest
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def application_index():
    services_status = nest.go_spidey()
    return render_template('index.html', services_status=services_status)

@app.route('/api/status')
def api_status_index():
    json = nest.go_spidey()
    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=True)
