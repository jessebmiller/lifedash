from datetime import date
from functools import singledispatch

from pyrsistent import (
    PRecord,
    field,
)


@singledispatch
def render(data):
    raise TypeError("no render function found for type {}".format(type(data)))

@render.register(list)
def _(xs):
    return "<ul>{}</ul>".format(
        ''.join(["<li>{}</li>".format(render(x)) for x in xs])
    )

@render.register(date)
def _(d):
    return '<time datetime="{}">{}</time>'.format(
        # YYYY-MM-DD   Weekday Month DD YYYY
        d.isoformat(), d.strftime("%A %B %d %Y"))

class Today(PRecord):
    date = field(type=date)
    weather = field(type=str)
    temp = field(type=int)

@render.register(Today)
def _(today):
    return """ 
    <div class="today">
      {date}
      <span class="weather">{weather}</span>
      <span class="temp">{temp}</span>
    </div>
    """.format(
        date=render(today['date']),
        weather=today.weather,
        temp=today.temp,
        )
