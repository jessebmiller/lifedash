from frolvlad/alpine-python3
maintainer Jesse Miller (jessea@jessebmiller.com)

run pip install bottle \
                pyrsistent
    
run mkdir /app
add app /app

cmd python3 -u app
