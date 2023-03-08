Title: Sweet data science reads
Date: 2023-1-15 09:25
Tags: books
Category: Python
Slug: data_science_books
Summary: Sweet reading list for data scientists
featured_image: /images/books/books_window.jpg

## The only data science book list you need today.

![me reading]({static}/images/books/books_window.jpg)  

I see a lot of top 10 book lists and many seem a bit spammy and a bit samey.
Here I want to show a list of books that mean a lot to me and helped me in my career. Not just books on how to do data science but things that are interesting if you are in the field. 

## 1. Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow  
[![Hands-on Machine Learning]({static}/images/books/01_HandsOnMachineLearning.jpg)](https://amzn.to/41z1CEL)   
Aurelien Geron  
[ISBN: 978-1492032649](https://amzn.to/41z1CEL)  

Hands down my favourite book, so naturally goes first. It's my go to bible for any machine learning concepts. My old copy was well thumbed and thankfully a second edition means I have a neater up-to-date copy on my shelf. This book has everything you need to start in machine learning, all of the core algorithms and metrics, all explained in a really clear way. It has the maths in there but done at the right level to help you understand the concepts. It covers the 'why' of certain technique's along with where they aren't so strong.

I haven't used the second half - the deep learning half - of the book as much, I had another amazing book for that (see #2 below).

## 2. Deep Learning with Python  
[![Deep Learning with Python]({static}/images/books/02_DeepLearningWithPython.jpg)](https://amzn.to/3KF1qxY)  
François Chollet  
[ISBN: 978-1617296864](https://amzn.to/3KF1qxY)  

My second favourite DS book. Also recently updated to a second edition so I have a fresh copy. (Congratulations to the people on facebook who received my donated first editions). 

This is the book that helped me to learn about deep learning and all the fun of neural networks. The book is based on Keras and written by the author of Keras. It's a really dense book but again everything is explained in an easily digestible way. Along with fastapi and pyspark, keras has a special place in my list of favourite libraries. It's so clear and easy to use. You'll be building dog image detectors in no time.

_I'm just a little sad that I'm moving over to pytorch and haven't found a book that matches Chollet's readability._

## 3. Spark – The Definitive Guide  
 
[![Spark – The Definitive Guide]({static}/images/books/03_SparkTheDefinitiveGuide.jpg)](https://amzn.to/3IGCXpv)  
Bill Chambers, Matei Zaharia   
[ISBN: 978-1491912218](https://amzn.to/3IGCXpv)  

You want to know spark eh? How about a ton of spark? then this book is for you. The title says it all, it's the definitive guide. In an older role, I picked up spark on the job for the first few months. That can only get you so far. Our databricks rep suggested I pick up a copy of this book to take it to the next level. 

Spark is built to handle big big data, and is good at optimising your query before running it. However a good amount of understanding will help reduce your query times from days to hours/minutes. You'll learn about how spark is architected and the major idioms behind it. Pretty much all of the examples are shown in both python and scala versions. The journey then forks off into streamed data, machine learning and graph data. 

If you haven't used spark before and you struggle with huge volumes of date, or maybe you cringe when you need to use some big pandas dataframe, then you should drop everything and dive in to spark.  
You can get a partial version of the book [here](https://pages.databricks.com/definitive-guide-spark.html).


## 4. Clean Code: A Handbook of Agile Software Craftsmanship    
[![Clean Code]({static}/images/books/04_CleanCode.jpg)](https://amzn.to/3xYd7YO)  
Robert Martin  
[ISBN: 978-0132350884](https://amzn.to/3xYd7YO)  

As a Data scientist it may not be immediately obvious but you are still engineering something. You may still need to hand your code over to others, it may even be your code that will hit production. Writing readable, maintainable code makes life easier for you and your team. Robert Martin, more commonly known as Uncle Bob, explains many of the ideas you need to write beautiful code. The code used in the book is java but I don't believe you need to know java, the book is perfectly readable and the ideas still apply. 

I think it's important for data scientists to learn software development practices like version control, continuous integration, architecting etc.

## 5. Flask Web Development 2e: Developing Web Applications with Python  
[![Flask Web Development]({static}/images/books/05_FlaskWebDevelopment.jpg)](https://amzn.to/3Zb0t4N)  
Miquel Grinberg  
[ISBN: 978-1491991732](https://amzn.to/3Zb0t4N)  

At some point you want to build your model into a web app or api and who you gonna call? flask! (or fastapi). The flask webserver is a great start to learning how to build a web application. As with the other books above this is a great library paired with a great book to learn it. I've used the book as a template to build many apps, both quick proof of concepts and apps in production. It's one of the smaller books on the list and you can get really far in the first few chapters. 

The later chapters cover things like handling user authentication and testing. Things you may not need on a small DS app but the first part of the book is more than worth it.

_I've moved onto fastapi now with its more modern api, but this library is currently lacking a great book to learn from._

## 6. Deep Learning and the Game of Go  
[![Deep Learning Go]({static}/images/books/06_DeepLearningAndTheGameOfGo.jpg)](https://amzn.to/41Cx5pY)  
Max Pumperla  
[ISBN: 978-1617295324](https://amzn.to/41Cx5pY)  

If you haven't seen the [AlphaGo documentary](https://www.youtube.com/watch?v=WXuK6gekU1Y) go and watch it now! [(Trailer)](https://www.youtube.com/watch?v=8tq1C8spV_g) It's one of those critical moments in time where AI beats humanity at a previously unbeatable game.

The book goes through all of the concepts used in building AlphaGo. I've read a couple of reinforcement learning books in the past but this on is a bit different. It covers the main RL concepts but has so much more around it. Normally a book takes a straight arrow from simple to complex through the book. This one covers the basics and then there are separate units using different ideas that are built and then later, all integrated together to form AlphaGo.

I'd highly recommend this book if you are comfortable with DS and looking to build something fun and learn a few more ideas. I managed to cobble something together to play a good game of connect-4.


## 7. Prediction Machines, Updated and Expanded: The Simple Economics of Artificial Intelligence  
[![Prediction Machines]({static}/images/books/07_PredictionMachines.jpg)](https://amzn.to/3miQOug)  
Ajay Agrawal  
[ISBN: 978-1647824679](https://amzn.to/3miQOug)  

This was recommended at a data science meetup I went to. When building something in data science it's good to know the context it's being used within the business. The 'why' of data science, how your project adds value. This book asked the question but at a higher level and looks at the economic impact of AI, drilling down  What things are affected by cheaper prediction. I liked how they reframe DS as work that is used for decision support. The author presents a framework for assessing AI at this top economic level and drilling down through industry level and company level. Most projects aren't the end point and the model directly affects the real world, a lot of times they feed into a decision maker. Where should we focus changes to make a road safer? Where is the best place to sell my concrete and what are the best mix ratios?

The book is a bit of a tough sell but worth it. There are [youtube videos](https://www.youtube.com/results?search_query=prediction+machines) of the author, Ajay Agrawal doing a better job than me.

## 8. I, ROBOT  
[![I, ROBOT]({static}/images/books/08_IRobot.jpg)](https://amzn.to/3y19K3w)  
Isaac Asimov  
[ISBN: 978-0008279554](https://amzn.to/3y19K3w)  

_(Not the film)_  
I studied AI a long time ago at uni when it wasn't the hip cool subject it is now. At one of the first study group sessions the tutor asked why we'd chosen to study AI. At least half of the group mentioned Asimov's books. I've picked 'I, Robot' here but Asimov wrote quite a few others. 

There are 9 stories, all centered around Asimov's 3 laws of robotics. They are a mix of thriller and puzzle stories, combined with Asimov's awesome story telling make this a must read book.

## 9. Freakonomics: A Rogue Economist Explores the Hidden Side of Everything  
[![Freakonomics]({static}/images/books/09_Freakonomics.jpg)](https://amzn.to/3IHivEK)  
Steven D. Levitt   
[ISBN: 978-0141019017](https://amzn.to/3IHivEK)  

This is certainly a fun book to read and a great conversation starter. Levitt takes things we take for granted and uses data to flip them on the head. How drug dealers earn less than minimum wage and how to find cheating teachers for example.  

Why should a data scientist read this? It teaches not to trust your initial assumptions and how to use the data to show how things are really working. An import skill is to take data and tell a story from it, sharing the insights with others. Here is a fantastic example of data lead story telling.   

A similarly fun read if you like this is [The Undercover Economist](https://amzn.to/3IHiAIy)

## 10. The New Kingmakers: How Developers Conquered the World  
[![The New Kingmakers]({static}/images/books/10_Kingmakers.jpg)](https://amzn.to/3Y9Rrnh)  
Stephen O′grady   
[ISBN: 978-1449356347](https://amzn.to/3Y9Rrnh)  

I struggled to find a number 10, but it's a top 10 list and here we are. 

Kingmakers I read a long time ago, it talks of how with the advent of cloud and open source anybody can setup an online company really cheaply. All you need is a laptop and an internet connection. In the 90s you'd have to purchase expensive hardware and know how to maintain it yourself, then load purchase expensive software to run on it. All this you'd need to cost and you'd scale the business in big steps. Nowadays you can run on open source software for free. You can run it on the cloud paying only for the resources you need. Did your user base double overnight? sweet, just add more compute. The main lead in this revolution is the developers, you just need a good idea and the will to implement it.

All this is still relevant today in the data science world. I can download a cutting edge deep learning model for free. In the 90s you would pay huge licence fees, and for a cutting edge research implementation you are in crazy money territory.  

Turning an idea into a startup used to have real hurdles. Even today roles that create things such as building architects require a huge outlay, or setting up a small store selling baby clothes still carry a risk. Modern software development has a much lower risk.

I added the book as it gives an appreciation of what we have as developers/data scientists. We are a lot less limited and hugely lucky compared to other industries. Having awesome ideas and prototyping on them is a huge motivation to think big.

  
## Final Requests
I like a good book but there are some subjects I have struggled to find a quality read on. If you have any suggestions for the items below hit me up.

- A decent John von Neumann biography.
- A good statistics book.
- Requirements gathering and project management.
- Story telling and visualisation.  

_Note there are affiliate links on the book covers. There are also some small cosmetic changes on the site. I've been learning SEO._