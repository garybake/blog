Title: Connected to the world
Date: 2016-7-29 12:36
Tags: esp8266, micropython
Category: esp8266
Slug: connected-to-the-world

We have the d1 mini and able to run python code on it, yey us!

The big sell of the ESP8266 is the embedded wifi. With this entry we'll go through using this with micropython.  

#### Get Connected

![wifi]({static}/images/wifi.png)

Connect to the D1 and enter the following into the repl. I'll explain the code a chunk at a time.

```python
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.isconnected()
```

The network module is what gives us all the wonderful code to use the wifi.

network.STA_IF is the connection where the ESP8266 connects to the internet and acts like a client.  
network.AP_IF is the other way round, where devices connect to the ESP8266 and it acts like a server.  

We are going to be sending requests out to the internet so we use STA_IF.
Then use our connection object to check if we are connected.  

```python
sta_if.active(True)
sta_if.connect('SSID', 'password')
```

First we activate the interface, use ```sta_if.active()``` to check/confirm the interface is active.
Then the real work is done with the next line. ```sta_if.connect```
Once executed you are returned to the repl but if you wait a couple of seconds you should see connection information coming through.

```
state: 0 -> 2 (b0)
state: 2 -> 3 (0)
state: 3 -> 5 (10)
add 0
aid 2
cnt 

connected with VM739083-2G, channel 1
dhcp client start...
ip:192.168.0.18,mask:255.255.255.0,gw:192.168.0.1
```

I'm not sure what the top few lines of info are.
The next line shows a successful connection, the router and which channel.
DCHP is started and from this the ESP8266 gains an ip address.  
You then see your ip address, the gateway mask and the gateway ip.

You can get these settings from the lines below

```python
sta_if.isconnected()
print('network config:', sta_if.ifconfig())
```

And thats your device connected to the world!

Note that your device will remember your connection settings and will try to connect using these setting each time the esp8266 is restarted.
This is a feature of the esp8266 chip rather than micropython.

#### Requests

To do a simple GET request you can use the instructions [here](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#http-get-request) or import urequests.

I'll go through pip-micropython at some point but for now the urequest library can be found [here](https://github.com/micropython/micropython-lib/blob/master/urequests/urequests.py).

Use the Ctrl+E method to past the code into the device.
I think there must be a small buffer for this as it failed to paste. I found that I had to paste the code in 3 sections - Response, request and then the rest.

If you've ever used the normal [python requests library](http://docs.python-requests.org/) you'll appreciate how powerful it is.

```python
r = get('http://micropython.org/ks/test.html')
print(r.status_code)
print(r.text)
```

The d1 has sent a request through the internet and received a response, yey!