FROM ubuntu:16.10

RUN apt-get update
RUN apt-get install -y g++ openjdk-8-jdk \
    python3-dev python3-dev python3-pip \
    git

RUN git clone https://github.com/suminb/tldr.git
WORKDIR tldr
RUN git checkout develop
RUN pip3 install -r requirements.txt

ENV PORT=8804
EXPOSE 8804
CMD python3 application.py
