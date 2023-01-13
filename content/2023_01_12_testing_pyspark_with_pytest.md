Title: Testing pyspark with pytest
Date: 2023-1-12 09:25
Tags: spark, pyspark, pytest, testing
Category: Python
Slug: python

# Using pytest to test your pyspark code

In my past couple of roles I've used pyspark and needed to to add tests to the code as part of the CI pipeline.
I couldn't really find much out there that describes the process neatly, mostly a couple of stackoverflow questions. 

Originally I used unittest but recently switched over to use pytest. I find it a lot cleaner to use and the tests are easier to read.

The code for this post can be found on [github](https://github.com/garybake/pyspark_pytest)  

# Basic pytest

I'll start with getting a normal test running with pytest. It's a noddy project used to illustrate the code. The layout of the project is

    Project
    |- src
    |- tests
    Dockerfile
    README.md
    requirements.txt

With the main code for the app going in src and tests in test. There is a root folder above this that also contains some setup files, I'll talk about these when needed.

# Docker

Spark can be a bit of a faff to setup, especially on windows. Docker makes this a million times easier. The dockerfile is pretty basic for what we need.

```
FROM apache/spark-py:v3.3.1

USER root

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /app
WORKDIR /app/Project
```

Here we use the official pyspark 3.3.1 docker base image, installs the pyspark and pytest libraries and creates the project folder.  

You can use a dockerfile as part of your CI pipeline on with [bitbucket pipelines](https://bitbucket.org/product/features/pipelines) which boots the image, runs the tests and then clear it all out. 

One important thing to take note is that you **need to match the versions in your test environment to your production environment** else your tests can be invalid.
You need to find and match the versions of
 - Java
 - Spark
 - Python
 - Pyspark library
 - ... any other dependencies used in production


To build the image

    docker build -t "test_pyspark" .

To launch the container using the image, for linux/mac

    docker run -it -v $(pwd):/app test_pyspark bash

For windows

    docker run -it -v ${pwd}:/app test_pyspark bash

TODO: I tried getting the docker-compose working but it was really hacky to get the box to stay running.

# Pytest

Lets create a noddy app to test

in Project/src/main.py

    def add_one(val):
        return val + 1

Add the file for the tests in Project/tests/test_something.py

    class TestMe:

        def test_add_one(self):
            assert add_one(3) == 4

I don't intend this to be an article about the best ways to write tests, just to say I find it easier to use one test class per file. That class should represent one object in the app or an endpoint. Then that class should contain a barrage of tests for that object. Also I haven't added any notes to the code.

-TODO should probably add type hints-

as
