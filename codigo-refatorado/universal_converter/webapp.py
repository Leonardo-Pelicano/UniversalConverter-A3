
# Optional simple Flask app to demo the converter via HTTP.
from flask import Flask, request, jsonify
from .service import ConversionService

app = Flask(__name__)
svc = ConversionService()

@app.route('/convert')
def convert_route():
    value = request.args.get('value')
    frm = request.args.get('from')
    to = request.args.get('to')
    out = svc.convert(value, frm, to)
    if out is None:
        return jsonify({'error':'invalid input or unit'}), 400
    return jsonify({'result': out})

if __name__ == '__main__':
    app.run(debug=True)
