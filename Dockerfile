from alpine
maintainer Jesse Miller (jessea@jessebmiller.com)

run apk update && \
    apk add --update \
      build-base \
      python \
      python-dev \
      py-pip

run pip install --upgrade pip \
                          bottle
    
run rm -rf /var/cache/apk/*  \
    && apk del \
       build-base \
       python-dev \

run mkdir /app
add app /app

cmd python -u app

