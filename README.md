# SEO Analyzer 

## This is system for collecting information about web-pages visited by users

You have two main endpoints here:

First one is for making analytics by users

```
POST localhost:5000/create_analytics

-d {"url": "https://kryshtalevypalats.gov.ua/ukr/"}
```

Second one for the investigation

```
POST localhost:5000/investigate_analytics

-d {"domain_name": "kryshtalevypalats.gov.ua"}
```

## Local Setup

`pip install -r requirements.txt`

`cd gateway`

`export FLASK_APP=server:app`

`flask run`