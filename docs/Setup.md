Thanks for being intersted in Congredi! We appreciate your early adopion.
Find your opporating system on the left to get started. 

Or if you would like to contribute. You can use the development version : 

```
git clone https://github.com/congredi/congredi
cd congredi
pip install -r requirements.txt
green congredi
python setup.py install 
```

# Linux

## Step 1 - Check Prerequisites
Congredi will only run on Python2.7, or Python3.3 To 3.6 

Versions 2.6 and 3.2 are not supported. 

To check your python version enter `python --version`

## Step 2 - Install Congredi

Install redis with your local package manager,

For Debian/Ubuntu run `sudo apt-get install redis-server`

For Fedora/CentOS run `sudo dnf install redis`

For Alpine/CoreOS run `apk add --update redis`

To install the library run `pip install congredi`

## Finish!

Confirm everthing is working by running `congredi peer`

# Mac OS X 

## Step 1 - Check Prerequisites

If you don't have Python you can it with [Homebrew](http://brew.sh)
byentering this command in the terminal `brew install python` 

## Step 2 -Install Congredi 

If you need Redis on your mac run `brew install redis`

If you have Python then run `pip install congredi`

## Step 3 - Finish!

Confirm everything is working by running `congredi peer`

# Windows 

We don't support Windows (***Yet***)

If you would like to contribute to windows support. See issue [#21} (https://github.com/congredi/congredi/issues/21)

# Docker 

For making custom images : 
```
From congredi/congredi
From congredi/delegito 
```

For scaling :
```
redis:
    image: redis:alpine
    ports:
     - "6379:6379"
    volumes:
    - /data/redis:/data
neo4j:
    image: neo4j:3.0
    ports:
     - "7474:7474"
     - "7473:7473"
     - "7687:7687"
congredi:
    image: congredi/congredi:latest
    ports:
     - "8800:8800"
delegito:
    image: congredi/delegito:latest
    ports:
        "443:443"
        "80:80"
``` 
