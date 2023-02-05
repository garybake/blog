Title: Testing pyspark with pytest
Date: 2023-1-15 09:25
Tags: spark, pyspark, pytest, testing
Category: Python
Slug: pyspark_pytest

# Using pytest to test your pyspark code

![drake meme]({filename}/images/pytest/drake_test.jpg)  

In my past couple of roles I have been developing on the pyspark platform and needed to to add tests to the code as part of the CI pipeline.
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

Here we use the official pyspark 3.3.1 docker base image. Then we install the pyspark and pytest libraries and create the project folder. 

![spark meme]({filename}/images/pytest/spark-meme.jpg)  

You can use a dockerfile as part of your CI pipeline with [bitbucket pipelines](https://bitbucket.org/product/features/pipelines) which boots the image, runs the tests and then clears it all out. 

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

![got meme]({filename}/images/pytest/got_meme.jpg)

in `Project/src/main.py`

    def add_one(val):
        return val + 1

Add the file for the tests in `Project/tests/test_something.py`

    class TestMe:

        def test_always_passes(self):
            assert True

        def test_add_one(self):
            assert add_one(3) == 4

I've added a quick test that always passes. You wouldn't put this in any normal code but it helps to show you have your environment setup correctly.

I don't intend this to be an article about the best ways to write tests, just to say I find it easier to use one test class per file. That class should represent one object in the app or an endpoint. Then that class should contain a barrage of tests for that object. Also I haven't added any comments to the code or type hints.

To run the tests ensure you are in the docker container and in the `/app/Project` directory and run the following

    pytest tests/

This will run all of the tests in the test directory. Anything in files called test_*.py.


    root@fc85736f011c:/app/Project# pytest tests/
    ================================================= test session starts ==================================================
    platform linux -- Python 3.9.2, pytest-7.2.0, pluggy-1.0.0
    rootdir: /app/Project
    collected 2 items                                                                                                      

    tests/test_something.py ..                                                                                       [100%]

    ================================================== 2 passed in 0.08s ===================================================


You can see that both tests passed. We can force a fail and see what output we see when something is wrong.

    root@fc85736f011c:/app/Project# pytest tests/
    ================================================= test session starts ==================================================
    platform linux -- Python 3.9.2, pytest-7.2.0, pluggy-1.0.0
    rootdir: /app/Project
    collected 2 items                                                                                                      

    tests/test_something.py .F                                                                                       [100%]

    ======================================================= FAILURES =======================================================
    _________________________________________________ TestMe.test_add_one __________________________________________________

    self = <tests.test_something.TestMe object at 0x7f04324f4f70>

        def test_add_one(self):
            print('---woohoo-')
    >       assert add_one(3) == 22
    E       assert 4 == 22
    E        +  where 4 = add_one(3)

    tests/test_something.py:28: AssertionError
    ------------------------------------------------- Captured stdout call -------------------------------------------------
    ---woohoo-
    =============================================== short test summary info ================================================
    FAILED tests/test_something.py::TestMe::test_add_one - assert 4 == 22
    ============================================= 1 failed, 1 passed in 0.14s ==============================================
    root@fc85736f011c:/app/Project# 


You also get anything that has been printed to the console on an error.

To show everything output to the console including on passing tests add the '-s' parameter when running tests.

    pytest -s tests/


# Pyspark

![no spark meme]({filename}/images/pytest/no_spark_meme.jpg)    

Imagine that the code below is part of your mega application that is destined to change the world.  



    import pyspark.sql.functions as F

    class SuperDataTransformer:

        def do_the_agg(self, df):
            df_agg = df\
                .groupBy('name')\
                .agg(
                    F.sum(F.col('value')).alias('sumval')
                )
            return df_agg

        def do_the_other_agg(self, df):
            df_agg = df\
                .groupBy('name')\
                .agg(
                    F.max(F.col('value')).alias('maxval')
                )
            return df_agg

There are two functions that do basic aggregations on the passed in dataframe, sum and max. The functions are part of a class that could be part of a pipeline.

# Pyspark tests

![am i testing]({filename}/images/pytest/amitesting.png)   

Now we are at the beef of this article, you need to test the pyspark code. The first thing you'll need is a spark session. When I built tests previously I had a class (SparkTestCase) that derived from unittest.TestCase. Then in the unittest setUp() function it created the sparksession and attached it as a property of the SparkTestCase. This worked well. Pytest has better ways of doing things - [fixtures](https://docs.pytest.org/en/6.2.x/fixture.html)!

Fixtures are used to feed things into your test and make things more modular and generally neater. There are many builtin fixtures such as tmpdir which creates a temporary folder for your test. They are also used to control the startup and teardown functions of tests.

You are going to have a lot of tests using this functionality so it should be in a seperate file (or folder if you have many other fixtures) called tests/spark_base.py

    import pytest
    from pyspark.sql import SparkSession

    def get_spark():
        spark = SparkSession.builder\
            .master("local[*]") \
            .appName('sparkTesting') \
            .getOrCreate()

        return spark

    @pytest.fixture()
    def spark():
        print("spark setup")
        spark_session = get_spark()
        yield spark_session
        print("teardown")

We are going to create our own spark fixture. The fixture has the @fixture decorator. Here we are using the startup and teardown functionality. For this we do the setup, yield what we need to the calling test and then do whatever teardown is needed. A pseudo code example may help

    run initialization/startup code in fixture
    create objects and pass them to the test
    run the test
    run tear down code in fixture

In the file that runs the tests `Project/tests/test_something.py`


    import pytest

    import pyspark.sql.functions as F

    from src.main import SuperDataTransformer
    from tests.spark_base import spark


    class TestMe:

        def get_data(self, spark):
            data = [
                {'id': 1, 'name': 'abc1', 'value': 22},
                {'id': 2, 'name': 'abc1', 'value': 23},
                {'id': 3, 'name': 'def2', 'value': 33},
                {'id': 4, 'name': 'def2', 'value': 44},
                {'id': 5, 'name': 'def2', 'value': 55}
            ]
            df = spark.createDataFrame(data).coalesce(1)
            return df

        def test_can_agg(self, spark):
            df = self.get_data(spark)
            trans = SuperDataTransformer()
            df_agg = trans.do_the_agg(df)

            assert 'sumval' in df_agg.columns

            out = df_agg.sort('name', 'sumval').collect()

            assert len(out) == 2
            assert out[0]['name'] == 'abc1'
            assert out[1]['sumval'] == 132

        def test_can_do_other_agg(self, spark):
            df = self.get_data(spark)
            trans = SuperDataTransformer()
            df_agg = trans.do_the_other_agg(df)

            assert 'maxval' in df_agg.columns

            out = df_agg.sort('name', 'maxval').collect()

            assert len(out) == 2
            assert out[0]['name'] == 'abc1'
            assert out[1]['maxval'] == 55


At the top we import the object to test (SuperDataTransformer) and the our spark fixture.

The first method is `get_data()`. This builds a dataframe with data for use in the tests. I find having it generated in a single place saves on duplication. You can have a number of these data generator methods if you are testing different parts of a pipeline. Each test should be isolated so you should know what data is being passed into the function.

A spark session is required for creating the dataframe so this is passed in as a parameter. When the dataframe is returned, one thing I found helpful was to add `.coalesce(1)`. This reduces the number of partitions of the dataframe down to a single partition and makes the tests run slightly faster. With the low volume of data we have in the tests this saves time on shuffling.

I'll focus on just the first test as the second one is pretty much the same

1. The spark session (spark) is passed in as a parameter from the fixture.
2. The dataframe is created
3. The object under test is created
4. The function this test is testing is ran using the test dataframe
5. A test to check the correct columns are in the output. We can check here before collecting the data as we want it to fail fast and spark keeps a record of the columns without running everything.
6. Then we collect the output of the function. Spark doesn't guarantee any order so it is reccomended to sort the output to ensure it is consistent.
7. From here the tests are ran how you would normally build tests. Test for length, types, individual fields in the rows etc.

If you print the 'out' variable just after the `collect()` you will see something like 

    [Row(name='abc1', sumval=45), Row(name='def2', sumval=132)]

This is the structure you are running tests against.

# Running sets of tests

Spark tests can take time to run. Sometimes you may want to run just the spark tests or all the tests excluding spark, or even specific tests.

![I dont always meme]({filename}/images/pytest/i-dont-always-meme.jpg)   

Create a file called `pytest.ini` in the Project folder _(TODO I'm not sure if this is the best place for it)_.

    [pytest]
    addopts = --strict-markers
    markers =
        is_spark: marks tests requiring a spark session (deselect with '-m "not is_spark"')

With pytest you can add flags and then only run the tests with those flags (or only tests without those flags).
It is good practice to add the `--strict-markers` at the top. Any tests with a flag not mentioned in pytest.ini will then trigger an error.

Here I've created an 'is_spark' flag and added it to the relavent tests using the pytest.mark decorator

    def test_always_passes(self):
        ...

    def test_add_one(self):
        ...

    @pytest.mark.is_spark
    def test_can_agg(self, spark):
        ...

    @pytest.mark.is_spark
    def test_can_do_other_agg(self, spark):
        ...

Running the tests with the -m parameter will run just the tests that have the flag.

    pytest -s -m is_spark tests/

Within the test output you can see `collected 4 items / 2 deselected / 2 selected` showing only the the ones we wanted were ran.

To run with the inverse of the flag, all the none spark tests, use the 'not' word in front of the flag i.e.

    pytest -s -m "not is_spark" tests/

This set of tests should run super quick as there is no spark session to create.

You can run tests based on a keyword in the test name i.e. this will just run the tests with the word 'add' in the name.

    pytest -s tests/ -k 'add'

The [-k parameter](https://docs.pytest.org/en/7.1.x/example/markers.html#using-k-expr-to-select-tests-based-on-their-name) takes an expression so you can build some pretty complex filters for your test run.

# Notes

There are still somethings I'm unsure off with this setup

 - Tests ran a lot quicker on bitbucket pipelines than when ran locally. I don't think bb pipelines run on super beefy machines but I seen full tests sets take 2 hours to run locally and then 20 minutes on the pipeline. 
 - The docker image should start off a single spark instance and then all the tests connect to that for their spark session.
 - `Spark.shutdown()` I could never get working cleanly. The session was always closed before the teardown. 
 - Should the dataframe from get_data() be created using a fixture?

Things I couldn't get working for this article but weren't really essential.

 - Keeping the docker image open needed nasty hacks. I would have liked to use docker compose.
 - I'm not sure why I needed to install the pyspark library on the spark image.

# Fin

I do like pytest. I went through an excellent tutorial by [Mika Tebeka on linkedin](https://www.linkedin.com/learning/testing-python-data-science-code/testing-scientific-applications?autoplay=true&u=140446626). He shows how to add a lot more power to your tests especially if you have data science applications and have the uncertainty/accuracy to deal with.

Final call to arms - ensure you match your library versions to you production environment else it could bite you in the ass.