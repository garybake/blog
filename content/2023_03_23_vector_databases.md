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

The great thing about these vector representations is that by their nature similar things will be close together in the space. So 'cat' will be near to 'dog' but far away from ['chocolate and peanut butter sandwich'](https://www.food.com/recipe/grilled-chocolate-and-peanut-butter-sandwich-114053).


### The tech
Creating this embedding mapping is beyond this article but there is a good article (here)[https://pub.towardsai.net/create-your-own-mini-word-embedding-from-scratch-c7b32bd84f8e].

Word2vec is one of the earliest libraries I can remember. Things have moved on since then with the advancement of deep learning. We had models such as GloVe and BERT which enabled full sentences to be encoded. With this came new companies that provide apis to the larger cutting edge models. Companies like (hugging face)[https://huggingface.co/sentence-transformers] and (openai)[https://platform.openai.com/docs/guides/embeddings].

### Why vector databases?

Now that we have a rushed description of embeddings, why would you want to store them? 
Imagine you had a million stored documents, you are a solicitor maybe. You are working on a gnarly case about Jack Sparrow and piracy

![cat pirate]({static}/images/vector_database/iwasapirate.jpg)  

You could do a text search for words like 'piracy' and 'sea' but you would miss a lot of documents. Words like 'marine' wouldn't be found and you may get a lot of documents back relating to software piracy. What you want is something that understands the context of what you are asking. 

Now imagine all of your documents are stored as points in this big vector space. Your query text is also converted to a point in the space and we look for the documents that are nearest to this point and return them to the user - amazing idea eh!

There are many things you can do with this technology
 - Find documents similar to a document or query text
 - Question / answering
 - Look for clusters in the space and use that to tag your data
 - Anomaly detection - why is this document far away from any others?
 - Matching texts roles to resumes, dating 
 - Deduplication of documents

With the recent explosion in generative AI you should soon be able to the following
 - Generate summaries of documents (you can already do this)
 - Move the document around the space. Imagine being able to make a document less aggressive sounding or maybe make everything a bit more geography related.
 - What is the difference between these documents.

### Fast search

If we have millions of documents how can we efficiently search them? The R-tree doesn't scale to large numbers of vectors. 

One of the most popular vector index types is HNSW (Hierarchical Navigable Small World). This trades insert time for improved query time.

The video below explains it really well

<iframe width="560" height="315" src="https://www.youtube.com/embed/QvKMwLjdK-s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### The fun part

Part 2 of this article, an example build using a vector database can be found (here)[todo]