from alpine
maintainer Jesse Miller (jessea@jessebmiller.com)

run apk add --update python3 \
    && pip3 install bottle \
    && rm -rf /var/cache/apk/*

run mkdir /app
add app /app

cmd python3 -u app

