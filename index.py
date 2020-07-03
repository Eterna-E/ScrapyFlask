from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    title = 'Flask test'
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')