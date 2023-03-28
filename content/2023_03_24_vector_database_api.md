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

You'll need to create a ".env" file. This contains all of the settings relevant to your project (and saves me the worry of leaking my own information). I'll show which settings to add as we work through the app.

I'm using [Weaviate](https://weaviate.io/) as the vector database of choice. It has a really clean api and great documentation for getting you started.

## Dataset

The first thing is to download the data and get it into a nice ingestible format.

The source can be found [here](https://www.cs.cmu.edu/~enron/), it's pretty big at 1.7Gb. Don't worry if you are still on dial up I'll share a sample of it pickled in the repo (TODO remember this)

We'll start at the top chairman and CEO, Ken Lay. You only need to extract the `enron_mail_20150507.tar.gz\enron_mail_20150507.tar\maildir\lay-k\` folder and put it somewhere accessible.

Add the folder to your .env file, replacing with your own folder. The **/*_ at the end tells python to filter all subfolders and then the files ending in an underscore.

	EMAIL_FOLDER = "./data/lay-k/**/*_"  # NonWindows

	EMAIL_FOLDER = "data\lay-k\**\*_"    # Windows



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

There are 2 methods to get up and running. Our app will work with either. The cloud method is much easier whereas using docker will give you a bit more understanding and a bit more scope to play.

### 1. Weaviate hosted

The most easiest way is to use weaviate cloud services. Weaviate give you a free sandbox environment to evaluate the technology.

https://console.weaviate.io/

Sign up to create an account. Press the + button to create a new instance.


| Setting | Value |
| --- | ----------- |
| Name | Anything |
| Subscription Tier | Sandbox |
| Weaviate Version: | Latest |
| Enable Authentication | Disabled for now (don't upload any sensitive data) |


Press the create button and wait a couple of minutes for your instance to be created.

Add the url of the instance to the .env file. It should be the name with the weaviate network of the domain. i.e. If your instance name is abcde add the following

	VDB_URL = "https://abcde.weaviate.network"

You now have some cutting edge architecture at your disposal, how easy was that!

2. Docker

This method allows you to run your own weaviate instance locally. You'll need to have docker installed.

The weaviate tutorial has an excellent [piece on their website](https://weaviate.io/developers/weaviate/installation/docker-compose) that generates a docker-compose file for you.

I've attached the one I'm using below

	version: '3.4'
	services:
		weaviate:
			command:
			- --host
			- 0.0.0.0
			- --port
			- '8080'
			- --scheme
			- http
			image: semitechnologies/weaviate:1.17.5
			ports:
			- 8080:8080
			restart: on-failure:0
			environment:
				TRANSFORMERS_INFERENCE_API: 'http://t2v-transformers:8080'
				QUERY_DEFAULTS_LIMIT: 25
				AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
				PERSISTENCE_DATA_PATH: '/var/lib/weaviate'
				DEFAULT_VECTORIZER_MODULE: 'text2vec-transformers'
				ENABLE_MODULES: 'text2vec-transformers'
				CLUSTER_HOSTNAME: 'node1'
			volumes:
				- "D:/tmp/weaviate_vol:/var/lib/weaviate"
		t2v-transformers:
			image: semitechnologies/transformers-inference:sentence-transformers-multi-qa-MiniLM-L6-cos-v1
			environment:
				ENABLE_CUDA: '0'

You will need to change the first part of the volumes parameter to a folder on your local on your machine. This allows us to persist the database between sessions.

You can see there are 2 main containers, the weaviate database and the MiniLM transformer. This is a smaller language model that produces vectors that are 384 elements in length. For comparison the bert model has 768 and ada has 1024. The larger the output means you are storing your data in a larger much richer space. Though you then pay the cost of compute converting the sentences and also the size of the db on disk.