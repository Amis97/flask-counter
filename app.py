from flask import Flask
import redis

app = Flask(_name_)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def visit():
    count = r.incr('counter')
    return f'این صفحه {count} بار بازدید شده است.'

if _name_ == '_main_':
    app.run(debug=True)
    