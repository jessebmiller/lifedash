from bottle import (
    route,
    run,
    template,
)

from components import (
    render,
)

@route('/')
def index():
    return render(index)

run(host="0.0.0.0", port="8000", debug=True)
 
