Title: Go bananas with the BBC Micro Bit
Date: 2016-8-5 12:45
Tags: fruit, micropython, microbit
Category: microbit
Slug: go-bananas-with-the-bbc-micro_bit

I received the microbit a couple of weeks ago and it's a solid device with plenty of scope for fun times.
The best thing is that it runs micropython. Yey, go team!

I had a chance for a quick play with the microbit during the [butlins science weekend](https://www.butlins.com/where-to-stay-dine-and-play/where-to-play/astonishing-science-weekend/).
The weekend was awesome and I can't recommend it enough!

One of the displays my son really enjoyed was the banana piano. There were about 5 bananas on display. You hold the ground wire and are then able to tap out a tune on the bananas with your other hand.
I think they were using the [Makey Makey](http://makeymakey.com).

After the holiday, I had to wait for a couple of months for the microbit to be released to the public. The microbit doesn't just plug into a breadboard, so I ordered some crocodile clips from [aliexpress](http://s.click.aliexpress.com/e/JamUbynmy).  

Eventually it arrived in the post and I got to playing with it.  
I struggled with the [web ui](https://www.microbit.co.uk/create-code). It's ok, but to save your code you need a school account and it didn't seem set up for the public.

Then I found the [mu editor](http://codewith.mu/). This allows you to work on code locally and upload them to the microbit.
It is a simple editor and the developers have gone to great lengths to keep it simple. This means some things are missing that I use in my normal workflow.
We can't have everything and I can dream that someday there will be a sublime text plugin.

Anyways, it is a good editor and supports things like syntax highlighting and pep8 linting etc.

The basic process is:

1. Plug microbit into computer.  
2. Enter code into editor and save file.  
3. Press the flash button.  
4. Code is compiled and uploaded to microbit.  
5. Code runs on microbit (or maybe an error message).  

Sometimes the microbit can't be seen (I'm running Xubuntu). When I click on the flash button, I need to select the device in the folders menu and then retry the flashing.

####Banana Piano

I built a couple of [scripts](https://github.com/garybake/microbake) whilst I was playing around with the microbit. Once I was comfortable with the microbit it was time to recreate the banana piano!

<blockquote class="twitter-video" data-lang="en"><p lang="en" dir="ltr">Bananas are the real musical fruit <a href="https://twitter.com/hashtag/microbit?src=hash">#microbit</a> <a href="https://twitter.com/hashtag/micropython?src=hash">#micropython</a> <a href="https://t.co/jpufzOidJ8">pic.twitter.com/jpufzOidJ8</a></p>&mdash; Gary Bake (@MrGaryBake) <a href="https://twitter.com/MrGaryBake/status/757539736886050816">July 25, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

There are 3 outputs big enough for the crocodile clips. We are using one for the buzzer, so we have 2 left to use as switches; hence only 2 notes.  
But more than enough to play Happy Birthday!

![circuit]({static}/images/microbit/bananapiano_schem.png)

I couldn't find a fritzing pic of the micropython. Even worse - I don't think there is an official circuit symbol for banana!

####Micropython

I modified code from the is_touched() function in the [micropython docs](https://microbit-micropython.readthedocs.io/en/latest/).

```python
from microbit import *
import music

note_low = ["C4:4"]
note_high = ["C5:4"]

while True:
    if pin1.is_touched():
        music.play(note_low)
        display.show(Image.HAPPY)
    elif pin2.is_touched():
        music.play(note_high)
        display.show(Image.SURPRISED)
    else:
        display.show(Image.SAD)
```

We create 2 notes - in fact we create two tunes of one note each, hence the array notation.

Looping forever, the code checks to see if a pin/banana is touched and changes the screen/plays the note accordingly.  
Pretty smart stuff :)
