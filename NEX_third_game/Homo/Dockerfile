FROM python:3.10.4-slim

RUN useradd -U -m -s /bin/bash ctf

RUN apt-get update && apt-get upgrade -y
RUN apt install -y python3 socat
WORKDIR /home/ctf
COPY chall.py ./ 

RUN chmod 500 /home/ctf/chall.py
RUN chown -R ctf:root /home/ctf

RUN pip install --upgrade pip
RUN pip install pycryptodome

USER ctf

CMD socat TCP-L:13341,fork EXEC:"python3 /home/ctf/chall.py",reuseaddr,stderr