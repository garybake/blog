# Blog

https://garybake.com  

###  Setup  
In the repo cloned folder

    python -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt
    git clone git@github.com:alexandrevicenzi/Flex.git

### Usage
Dev server

    pelican -r -l

Generate site

    pelican content

Generate html

    make html

Generate for upload to website

    make publish
