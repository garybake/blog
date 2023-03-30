Title: Vector Database Application
Date: 2023-3-24 09:25
Tags: database
Category: Python
Slug: vector_database_application
Summary: Building an application using a vector database
featured_image: /images/vector_database/distractedbf.jpg

## Build a killer app using vector databases

![distracted me]({static}/images/vector_database/distractedbf.jpg) 

As a nosy person one of my fave datasets is the [Enron emails](https://en.wikipedia.org/wiki/Enron_Corpus). Enron was a huge energy company that was ran by bad people and ultimately collapsed. You can even get to know the people a bit more with the [documentary](https://www.imdb.com/title/tt1016268/). For this article we'll build something to store and query the emails using our new found vector know-how.  

_I intend to write another article around using the Enron emails with Graph Neural Networks_

Our cutting edge app is named **"Enronalyse"**. Thank you GPT4 for coming up with the awesome name, you are the best!

![search UI]({static}/images/vector_database/search_ui.jpg) 

The repository is [here](https://github.com/garybake/enronalyse)

First pull the repo and create a ".env" file. This contains all of the settings relevant to your project (and saves me the worry of leaking my own secrets). I'll show which settings to add as we work through the app.

I'm using [Weaviate](https://weaviate.io/) as the vector database of choice. It has a really clean api and great documentation for getting you started.

## Dataset

The first thing is to download the data and get it into a nice ingestible format.

The source can be found [here](https://www.cs.cmu.edu/~enron/), it's pretty big at 1.7Gb. Don't worry if you are still on dial up I've shared a sample of it pickled in the repo (emails_500.pkl)

We'll start at the top, chairman and CEO, Ken Lay. You only need to extract the `enron_mail_20150507.tar.gz\enron_mail_20150507.tar\maildir\lay-k\` folder and put it somewhere accessible.

Add the folder to your .env file, replacing with your own folder. The `**/*_` at the end tells python to filter all subfolders and then the files ending in an underscore.

	EMAIL_FOLDER = "./data/lay-k/**/*_"  # NonWindows

	EMAIL_FOLDER = "data\lay-k\**\*_"    # Windows



## Parse emails
The code for parsing emails is in the `import/read_emails.py` file. Its not that complex. Weaviate expects records formatted as a dictionary.

	{
	    'send_date': 'Fri, 8 Dec 2000 07:49:00 -0800 (PST)', 
	    'em_from': 'a.b@enron.com', 
	    'em_to': None, 
	    'em_cc': None, 
	    'subject': "a subject", 
	    'content': "..."
	}

You can run the this file and it will print out a count to show its all working.
I'll come back to this later. But for now we have a array of email records with the text in the content field.

## Up and running with weaviate

There are 2 methods to get up and running. Our app will work with either. The cloud method is much easier whereas using docker will give you a bit more understanding and a bit more scope to play.

### 1. Weaviate hosted

The most easiest way is to use weaviate cloud services. Weaviate give you a free sandbox environment to evaluate the technology.

[https://console.weaviate.io/](https://console.weaviate.io/)

Sign up to create an account. Press the + button to create a new instance.


| Setting | Value |
| --- | ----------- |
| Name | Anything |
| Subscription Tier | Sandbox |
| Weaviate Version | Latest |
| Enable Authentication | Disabled for now (*don't* upload any sensitive data) |


Press the create button and wait a couple of minutes for your instance to be created.

Add the url of the instance to the .env file. It should be the name with the weaviate network of the domain. i.e. If your instance name is _abcde_ add the following

	VDB_URL = "https://abcde.weaviate.network"

You now have some cutting edge architecture at your disposal, how easy was that!

You'll also need a vectoriser, something to transform your sentences into vectors. 
I'd recommend signing up to [OpenAI](https://platform.openai.com/signup). Have a look around, these are the people building the cutting edge.
Create yourself an access token [here](https://platform.openai.com/account/api-keys) and add that token to the .env

	OPENAI_API_KEY="*****"

Also have a look at [Hugging Face](https://huggingface.co/). This site is amazing for hosting your own models and interacting with other pretty huge models.
I went with openai for this article because the number of requests you could maker per second was more generous on the free tier.



### 2. Docker

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

You will need to **change the first part of the volumes parameter** to a folder on your local on your machine. This allows us to persist the database between sessions.

You can see there are 2 main containers, the weaviate database and the transformer. The transformer uses the [multi-qa-MiniLM-L6-cos-v1](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1) model. This is a smaller language model that produces vectors that are 384 elements in length. 

For comparison the bert model has 768 and ada has 1024 elements. The larger the vector size the larger and richer the vector space. Though you then pay the cost of compute converting the sentences, search complexity and also the size of the db on disk. If you look into the weaviate tutorial it's fairly easy to switch out and use openAI, HuggingFace or Cohere apis to generate your vectors. The example below uses the openai api setup above.

### Connect and create the class

Lets put some data into the database. The code for this part is in the `import/import_emails.py` file

![wrong database]({static}/images/vector_database/wrongdatabase.jpg) 

I've created a VDB class that our database interactions talk to.
The first part is the connection to the database. The connection handles authentication and various API keys but we are keeping it simple so just need the url from the .env file.

	def connect(self):
		db_url = os.getenv("VDB_URL")
		api_key = os.getenv("OPENAI_API_KEY")

		self.client = weaviate.Client(
			url=db_url, additional_headers={"X-OpenAI-Api-Key": api_key}
		)
		return self

The next part is where to store the data. Everything related to email uploading is in the EmailUploader class.
Weaviate uses the notion of 'classes' (not the same as python classes) which are akin to tables. We are going to store everything in an 'Email' class.
The easiest example just needs the name and the vectorizer. Later on you can add things like formally declaring the schema for the class.

	class_obj = {
		"class": "Email",
		"vectorizer": "text2vec-openai"
	}

The full create schema function looks like this

	def create_schema(self):
		class_obj = {
			"class": "Email",
			"vectorizer": "text2vec-openai"
		}

		db = VDB().connect()
		# db.client.schema.delete_class("Email")  # uncomment to delete table if needed
		db.client.schema.create_class(class_obj)

If you are recreating the class you'll need to uncomment the delete line. Trying to overwrite will fail. This is also useful for quickly emptying the table. The database will now have the email class and be ready to accept data.

### Upload data

If this is your first run, its best to try with fewer emails. The get_email_data() function has a max_emails parameter. Set this to something like 20 while you get it to work.

Inserts are done in batches. It depends on your volume and size of the texts you are uploading. I found I had timeouts when uploading 3000+ full page documents (for another project) and batches of 50 worked well.

	def insert_emails(self, email_data):
		db = VDB().connect()

		with db.client.batch as batch:
			batch.batch_size=50
			for email in email_data:
				db.client.batch.add_data_object(email, "Email")


You can confirm the data has loaded at https://your-database-code.weaviate.network/v1/objects.   
Once you are confident its working, recreate the email class and upload 500 messages.

### Query the data

Now we come to the powerful part, using the vector search.

Note. if you run this and get the error 'Model .... is currently loading ...'. You should wait a couple of minutes. It just means the instance is turned off due to it being free and weaviate are rebooting it.

The first part is what information we want returned. Just the main ones will do, as long as 'content' is there.

	search_headers = ["email_id", "send_date", "em_to", "subject", "content"]


The next part is the nearText. This is our query text; that gets turned into a point in the vector space and returns the emails nearby to it. We pass the query_term into the function.

	nearText = {
		"concepts": [query_term],
	}

Then these are put together into a 'get' query. Also note the row_count of how many rows we want returned.

	result = (
		db.client.query.get("Email", search_headers)
		.with_near_text(nearText)
		.with_limit(row_count)
		.do()
	)

The full function is below.

	def query(self, query_term, row_count=2):
		db = VDB().connect()

		search_headers = ["email_id", "send_date", "em_to", "subject", "content"]

		nearText = {
			"concepts": [query_term],
		}

		result = (
			db.client.query.get("Email", search_headers)
			.with_near_text(nearText)
			.with_limit(row_count)
			.do()
		)

		return result

Lets make like a journalist and look for those emails talking about the bad things

	eup = EmailData()
	result = eup.query("criminality")
	print(json.dumps(result, indent=4))

The first result is a bit of fluff, the second however

	"subject": "Anonymous report on violations by senior Enron officials"
	"content": "Please see attached file.  I wish to remain anonymous...",

Scooby doo and his gang would be all over this. We don't have the attachment sadly. 
You can see though how this email didn't contain the word 'criminality' but due to the wonders of vector search the context is correct.

![Enron Scooby]({static}/images/vector_database/enron_scooby.jpg) 

How about something a bit more far out, something more than a single word - "the captain of the titanic". The results are below.

	"subject": "Cruise",
	"content": "I trust you are already planning our next trip..."

	"subject": "Dear Cruisers",
	"content": " - CRUISE~1.DOC",

Emails about going on a trip on a cruise ship! Considering this is emails from the CEO of an energy company, these results are pretty good.

From here you can add things like 

I'm not going through that here instead I'm adding something a bit more of a platform to build from.

### Build the app

Lets build an app that uses the super search functionality. 

This isn't a fastapi tutorial that can be found [here](https://fastapi.tiangolo.com/tutorial/). It feels like a bit of a draw the owl momement.

![Draw Owl]({static}/images/vector_database/draw_owl.png) 

This is not production code and more of a proof of concept. I've basically mashed some code from other projects together with the code above.

To run it ensure your .env has the VDB_URL and OPENAI_API_KEY in and working

    EMAIL_FOLDER = "***"
    VDB_URL = "https://***.weaviate.network"
    OPENAI_API_KEY="***"

Then run `uvicorn app.main:app --reload` and open [http://localhost:9000/](http://localhost:9000/)

Enter your search term, press the search button and boom, it renders your search results from the vector database.
You can see the swagger api docs at [http://localhost:9000/docs](http://localhost:9000/docs). These allow you to test and play with the endpoints.

I'll go over the main components of the app

app/core/db - Utility class for connecting to the database
app/api/v1/email	-	Handles the api requests for the search term
app/models/email	-	Anything to do with the email model is here. Talks to the db class and cleans the input/output from it.
app/views/index	-	Handles rendering the front end
static/ - images, css and js
static/js/index - JQuery code to handle the search press, api request and rendering the result
templates - Jinja templates of html. Uses bootstrap.

There isn't much too it but I think it looks impressive.

### Expand Enronalyse

Looking for ideas to expand the app?

 - Add summaries of the emails using the [hugging face api](https://huggingface.co/facebook/bart-large-cnn)
 - Add moveTo and moveFrom so you can (de)emphasise parts of your query
 - Return the similarity scores
 - Plot the space in 3d
 - Formally declare the schema of the class
 - Add your own vectorizer and pass the vectors to the db.
 - Add more classes
 - Add authentication to the db and app.
