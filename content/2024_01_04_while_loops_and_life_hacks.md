Title: While Loops and Life Hacks
Date: 2024-1-4 09:25
Tags: database
Category: Python
Slug: development
Summary: Applying Software Engineering Principles to Everyday Challenges
featured_image: /images/devlife/dev_chaos_x.jpg

![dev chaos]({static}/images/devlife/dev_chaos_x.jpg)  

## Applying Software Engineering Principles to Everyday Challenges

Its that time of year and again I've made a resolution to post once a month. We'll see how far I get.  

I was looking around for posts and came accross the old trello board we used when buying a house. How it made the whole process less daunting. Using an agile board to manage projects is something I use every day as a developer. I'm sure there's other ideas I use as a developer that I use in my normal life to make it easier. I'll make a list and share it with the world.

Note that I have chatgpt alongside as a copilot. Not to write the article, more to bounce ideas off. I use it everyday for programming and would like to think my productivity and output quality has improved.

### Modularization
I think I may have done this on my first A-Level computing lesson (in the old days). You have a huge task, you don't know where to start or how it will get done.
We'll use the example of booking a holiday.

You first break the task down into its major components. Flights, accomodation and activities.
Take each of them tasks and break them down, say flights -> get passport, find flights, book flight.
Find flights can be further split down into find availability, find cheapest.

By the end of the process you should have a load of easily achieaveble tasks. 

You also need to consider the dependancies amongst the tasks. For example the location of the activites you plan will be dependant on the location of the accomodation.

### Kanban Boards
![dev chaos]({static}/images/devlife/kanbanboard_x.jpg)  

This is what gave me the idea for the article. Something most companies use to manage development work.
Each peice of work has a ticket. In the most basic example there are 3 columns, To Do, Doing, Done.
Tickets start in the todo column. Tickets have a name on the ticket for who is working on it.

You pick up a todo ticket, and put it in the doing column. Do the work and once the work is done its put in the Done column.
If work is blocked you pick up another todo ticket (sometimes a manager or scrum master will help clear the blockages).

You don't want to put all of your work into the todo column because it will become really unweildly. You have another column called 'backlog'. Put all of the work in there. 
I work on 2 week 'sprints'. This means taking, from the backlog, what we think can be achieved in 2 weeks and puttin them in todo.
Then you have 2 weeks to move those tickets accross to do. At the end of the sprint, in an ideal world, you clear down the done column and start a new sprint.

When moving house we used kanban to manage the project and it took a huge amount of stress out of it. We used trello (https://trello.com/garybake/recommend), the free online board.

![dHouse kanban]({static}/images/devlife/kanban_house.png)  

### DRY/YAGNI

DRY - Don't Repeat Yourself
YAGNI - You Ain't Gonna Need It

I've put these two together as they are vaguelly related. 

DRY is removing duplication. Each function in a program doesn't really need to contain the same code to talk to a database. They all talk to the same database driver. This means you only have one set of code to handle the database interactions, that does one thing and does it well.

In real life this could be something like having two hedge trimmers. Nobody needs two, put one on ebay and buy something useful!

YAGNI for developers means removing code that is no longer needed and also not adding code 'just in case' its needed in the future. Some developers can get sentimental but having old code hanging about means that code still needs be maintained and can cause bugs.

In real life this can be something like still having a DVD player plugged into your TV. If you haven't watched a DVD in 12 months, unplug it and put it into the loft at least.

Yagni is also something the Money Saving Expert guy preaches. Even if something is super cheap, if you buy it and don't use it, then it was expensive.

### Backups

Data storage is cheap and being able to get an application backup and running after a failure is hugely important.
Having a backup and recovery strategy should be part of every application.

I've seen it too many times, how a persons phone has broke and they have now lost all their pictures if the grandkids. You can plan for this.
It could be taking regular backups of your phone, or extracting them to a seperate usb drive. 
My facourite is google photos (https://photos.google.com/). Put it on your phone and it automatically backsup all of your photos to the cloud with no technical know how.

Its hard or pointless to backup a lot of physical things. My wife and I have a shared calendar online (https://calendar.google.com/). If we receive a doctors appointment in the post, it takes a couple of minutes to create a calendar event, take a picture of the letter and add it to the event.

### Pair programming - Bus factor

A good way to get new developers up to speed it pair programming. This is where two programmers sit at one computer and build a task. Having two people working together should provide a cross polination of ideas and up skilling.

Bus factor is an odd one. How many devs could get hit by a bus before there isn't enough knowledge to keep an application running. You could have 20 developers but if only 1 developer knows how part of the app works then you have a bus factor of 1 and are at risk.

My wife and I sort out a lot of the important things together. Things that affect the household are organised through the joint bank account, things like house insurance and the tesco clubcard. I'm hoping that for keeping our house running we have a bus factor of 2.

### KISS

Keep It Simple Stupid

Don't over engineer things. Don't make it too complicated. Build it as obvious and simple as possible. This makes code easier to maintain and understand.

In real life you can benefit from streamlining things. Having bank accounts accross multiple banks, cooking meals with tons of ingredients when a few core ingrediants will do.

### Technical debt

Tech debt is where you intend to change some code to work better but due to time constraints you can't. You intend to fix it in the future but it sits in the code for months. Over time if you don't take time to fix this debt you can endup with a bad codebase. It takes longer and longer to add new features.

If something needs fixing in your life it is often quicker to fix it now than later on. Wobbly door handle? fix it now before it falls off or one of the kids gets stuck in the bathroom. Batteries in the remote need changing? nobody likes having to standup and press buttons on a tv like some kind of caveman!

A constant stream of small fixes and maintenance can pay huge benefits over a lifetime.

### Others

There are some other dev principles that can apply to real life but I'm ill and ending the post here.
 - Debugging
 - Root cause analysis
 - Continous deployment
 - Technical debt

### TODO
 - Backups
 - Debugging/Tracing
 - RootCause Analysis
 - DRY
 - KISS
 - Continuous Deployment:Refactoring Life:
 - YAGNI



