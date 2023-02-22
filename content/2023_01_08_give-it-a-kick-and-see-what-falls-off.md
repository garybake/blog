Title: Give it a kick and see what falls off
Date: 2023-1-8 09:25
Tags: Blog, Repair
Category: Blog
Slug: blog
Summary: Test post to fix various bugs and generally update the site.
featured_image: /images/fixthings/support_team.jpg

## The site is down

Another year another resolution to write more. I should probably see when my last post was.  

Damn, my site is broke! How embarrasing.

![Support Team]({static}/images/fixthings/support_team.jpg)

A quick check and it looks like I was using a mix of http and https; this shows how long it was since the last update.

## The site is up

It was quick enough to fix, just updating the links in the page. 

This shouldn't be a problem, all links should be relative to the root page and use the same protocol. I'm using a static site generator ([pelican](https://getpelican.com/)), so either I or the generator is doing these shenanigans.

## Fix the things

If I'm going to create more amazing masterpiece posts this year then I need to crack open the code and check everything still works.

![gandalf memory]({static}/images/fixthings/gandalf_no_memory.jpg)  

I haven't use this software in a while. This isn't helped by me not documenting and taking various shortcuts. 

### Restart  

#### 1 - Get it working  

Git clone fails. This isn't a great start!  
There is a file that has a colon in the name (yey micro:bit). Good on linux, bad on windows! I can edit filenames on github and take a step forward.

Create a venv, install the requirements - bosh!
Compile the site - no bosh. It can't find the theme. I had put it in a folder on an old machine and hard linked to the path. Clone the theme repo and put it into the project folder. Link straight to it.. nice.

 - TODO I should use a sub repo
 - TODO requirements.txt should have version info

Take a step forward.

Site is up with no icons just as I planned <sad face>. We are missing font-awesome. I think these should come from the theme but that is missing some files in the latest version. They have stopped work on the theme and its now outdated! I really like this theme. Fixed by copying the latest set of files to the themes directory.    

 - TODO the theme should use a cdn.  
 - TODO what to do about the unsupported theme?  

Icons show, site looks good. Take another step foward.

#### 2 - Document  

Why did I add notes to a scratch file? There is a readme right there asking for it. Setup and startup instructions added. I also copied over the idea list and added some new ones.

#### 3 -  Get it working properly  

![python2]({static}/images/fixthings/python2.jpg)  

I think it uses python 2! or at least the generated files did. In 2016 when I generated the configs I was using python 2 in my role and I guess I had used that laptop. Anyways, I generated a blank pelican project and checked for any major differences. It looks like the only main change is to remove some polyfill imports and remove the unicode flag from the start of some strings. Easier than I thought, phew!

- TODO Use a newly generated config. There is all kinds of junk in the current one.

#### 4 - Test that it is working  
Generate the site with all the changes. Add a new blog post and upload to the web host.
If you are reading this then the test has passed.

tl;dr, this page is just a test.