[![Travis](https://img.shields.io/travis/suminb/tldr.svg)](https://travis-ci.org/suminb/tldr)
[![Coveralls](https://img.shields.io/coveralls/suminb/tldr.svg)](https://coveralls.io/github/suminb/tldr)

TL;DR
-----
TL;DR, which stands for "Too Long; Didn't Read", is a text summarization service.

Obtaining Docker Image
----------------------
The pre-built Docker image can be obtained by running the following commands:

    docker pull sumin/tldr

Code Build
----------
If you would like to build the code yourself, you will need the following
things:

- Docker
- Python 2.x or 3.x
- Java 6 or higher

The Docker image can be built by running the following command:

    docker build ${directory containing Dockderfile}

Run
---

    docker run -d -p 8804:${host port} sumin/tldr

For example, if you would like to map the 8804 port of the guest host to the
identical port number (8804) of the host, you may want to run the following
command.

    docker run -d -p 8804:8804 sumin/tldr

Invocation
----------
RESTful APIs can be invoked via any standard HTTP client. Use of `curl` or
`wget` is advised.


### Text Summarization

    curl -XPOST -d "text=This is a text" http://localhost:8804/api/v1/summarize

### Text Extraction

    curl -XPOST -d "html=<html><body>Example</body></html>" \
        http://localhost:8804/api/v1/extract-text

Tests
-----

    py.test -v tests
