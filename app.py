from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def visit():
    count = r.incr('counter')
    return f'این صفحه {count} بار بازدید شده است.'

if __name__ == '_main_':
    app.run(debug=True)
