# Blog

https://garybake.com  

###  Setup  
In the repo cloned folder

    python  - m venv venv
    source venv/bin/activate 
    pip install  -r requirements.txt
    git clone git@github.com:alexandrevicenzi/Flex.git

### Usage
Dev server

    pelican  -r  -l

Generate site

    pelican content

Generate html

    make html

Generate for upload to website

    make publish


Blog ideas
==========

Cool toys
 - ChatGPT
 - DallE 
   - Image fill
   - Best prompts

Coding
 - Pyspark automated tests

TinyML
 - motion surface detection

Visualisation
 - D3
 - Animated charting

ESP32
 - Sys
     - Bootstrap app
     - Debug, perf
     - Compile targets/freezing
 - Server
 - OLED shield
 - Button
      - Door bell
 - DHT shield
 - Relay shield
 - Motor shield
 - Micro SD shield
 - BMP180
 - Nokia screen
 - Traffic lights
 - Door bell

Microbit
 - Balance game
 - Racing game
 - Banana music
 - Paralax starfield


Add display functions  
http://hoardedhomelyhints.dietbuddha.com/2012/12/python 
- metaprogramming - dynamically.html


Dev notes
---------
I'll forget that I need this information

Update Flex/templates/partial/sidebar.html
Change the <h1>...SITETITLE...</h1> to be <h2> tags. This fixes SEO complaining about having more than one H1 tags in the page.