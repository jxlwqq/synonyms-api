from flask import Flask
from flask import request
from waitress import serve
import synonyms as sy

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/synonyms/<word>')
def synonyms(word):
    size = int(request.args.get('size', 10))
    res = sy.nearby(word, size)
    return {
        "word": word,
        "size": size,
        "nearby": res[0],
        'scores': list(map(str, res[1]))
    }


if __name__ == '__main__':
    serve(app, listen='*:5000')
