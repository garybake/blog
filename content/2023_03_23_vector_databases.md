Title: Fun with Vector Databases
Date: 2023-3-23 09:25
Tags: database
Category: Python
Slug: vector_databases
Summary: Fun with vector databases
featured_image: /images/vector_database/isthisadb.jpg

## The best place to store you favourite kinds of data

![king queen]({static}/images/vector_database/isthisadb.jpg)  

A while ago I was reading up on how databases work with native geospatial datatypes, basically lat/lon pairs, 2 dimensional vectors. This then lead on to adding altitude and time, 3 and 4 dimensional vectors. How does the indexing and search work with these? for 2 and 3 dimensions many use [R-trees](https://en.wikipedia.org/wiki/R-tree).

What would you need to do if you had say 8, 15 or even 1024 dimensions? What sort of scifi nonsense is this?

![cat dimensions]({static}/images/vector_database/cat_dimensions.jpg)  

### What about n-dimensional vectors?

First lets show the main use case for storing n-dimensional vectors. In machine learning, especially with neural networks, you are are using numerical data. The learning models don't understand things like text, pictures, sound etc. We need a method transforming this unstructured data into numbers. 

There are many, many methods to do this but here we are concerned with vectors, sometimes called embeddings. I'll talk through using text, but the input can be anything unstructured (or even structured).

The embedding function takes in the sentence and outputs the vector.

> "The cat sat on the mat" &rarr; [2.3, 4.5, 0.2]

What do these numbers mean? This may sound a bit woolly but they can be though of as 'concepts'. The first place could be how masculine/feminine the sentence is. Another value could be how much geography there is the sentence.

The classic example is shown below.

![cat dimensions]({static}/images/vector_database/king_queen.png)  

The vectors towards the lower right are more feminine, those to the upper left more masculine. The upper right, lower left is how royal an element is. If you added a queen point it would be feminine + royal and sit on the right hand side. 
