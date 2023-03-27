Title: Vector Database Application
Date: 2023-3-24 09:25
Tags: database
Category: Python
Slug: vector_database_application
Summary: Building an application using a vector database
featured_image: /images/vector_database/distractedbf.jpg

## Build a killer app using vector databases

![distracted me]({static}/images/vector_database/distractedbf.jpg) 

As a nosy person one of my fave datasets is the [Enron emails](https://en.wikipedia.org/wiki/Enron_Corpus). You can even get to know the people a bit more with the [documentary](https://www.imdb.com/title/tt1016268/). For this article we'll build something to store and query the emails using our new found vector know-how.  

_I intend to write another article around using the Enron emails with Graph Neural Networks_

Our cutting edge app is named **"Enronalyse"**. Thank you GPT4 for coming up with the awesome name, you are the best!

The repository is [here](https://github.com/garybake/enronalyse)

I'm using [Weaviate](https://weaviate.io/) as the vector database of choice. It has a really clean api and great documentation for getting you started.

## Dataset

The first thing is to download the data and get it into a nice ingestible format.

The source can be found [here](https://www.cs.cmu.edu/~enron/), it's pretty big at 1.7Gb. Don't worry if you are still on dial up I'll share a sample of it pickled in the repo (TODO remember this)

We'll start at the top chairman and CEO, Ken Lay. You only need to extract the `enron_mail_20150507.tar.gz\enron_mail_20150507.tar\maildir\lay-k\` folder and put it somewhere accessable.

## Parse emails
The code for parsing emails is in the `import/import_emails.py` file. Its not that complex. Weaviate expects records formatted as a dictionary.

	{
	    'send_date': 'Fri, 8 Dec 2000 07:49:00 -0800 (PST)', 
	    'em_from': 'a.b@enron.com', 
	    'em_to': None, 
	    'em_cc': None, 
	    'subject': "a subject", 
	    'content': "..."
	}

I'll come back to this later. But for now we have a array of email records with the text in the content field.

## Up and running with weaviate

There are 2 methods to get up and running. Our app will work with either.

### Weaviate hosted

The most easiest way is to use weaviate cloud services. Weavieate give you a free sandbox environment to evaluate the technology.

https://console.weaviate.io/
