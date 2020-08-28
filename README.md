[![Build Status](https://travis-ci.com/Slenderman00/Grindr-Web-Access.svg?branch=master)](https://travis-ci.com/Slenderman00/Grindr-Web-Access)

# GRINDR WEB ACCESS

Grindr web access is a framework for the new grindr v4 api
![](https://i.imgur.com/6SGvLxS.png)
Just scan the qrcode using your grindr app

## Installation
```
pip3 install git+https://github.com/Slenderman00/Pip-Grindr-Web-Access.git
```

## Usage

```python
# import the GrindrWebAccsess.api framework
import GrindrWebAccsess.api as api

#GrindrWebAccsess full login
tokens = api.fullLogin()
print(api.getProfileId(tokens[0]))

#on message
def onmessage(message, profileid, _type):

    #type: text, image, tap

    #do stuff with message
    print(_type + " " + message)

#open socket
socket = api.messageSocket(tokens, onmessage)
socket.start()
```

## Usage 2
```python

#fetch your own userid
api.getProfileId(tokens[0])

#send message
socket.message("<Userid>", "<Message body>")

#send tap
socket.tap("<Userid>", "<tapType>")
#tap type = 0, 1, 2
#0 = Friendly
#1 = Hot
#2 = Looking

#fetch array of all users
#                  authtoken    lat         long        parameters
api.fetchProfiles(tokens[0], 40.785091, -73.968285) # myType='false', online='false', faceOnly='false', photoOnly='false', notRecentlyChatted='false'

```

## Todo
- add search filters

## Dependencies
- requests==2.23.0
- asyncio==3.4.3
- pyqrcode==1.2.1
- websocket_client==0.57.0
- xmltodict==0.12.0
- pygeohash==1.2.0


## Contributing
If you want to contribute please go to:
<https://github.com/Slenderman00/Grindr-Web-Access/tree/experimental>

## License
[MIT](https://choosealicense.com/licenses/mit/)