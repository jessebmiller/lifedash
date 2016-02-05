from bottle import (
    route,
    run,
    template,
)

@route('/')
def index():
    return template("<h1>init</h1>")

run(host="0.0.0.0", port="8000", debug=True)

