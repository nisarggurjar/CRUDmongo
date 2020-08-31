# CRUDmongo

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

It is a web application made by using django and djangorest as frameworks and MongoBD as DBMS


## Feature
  it has API to GET, PUT, DELETE, POST

## API patterns
assuming server is running using 
```sh
python manage.py runserver 8000
```

* GET (all) - localhost:8000
* GET (one) -  localhost:8000/getArticleDetail/<ObjectId (_id)>
* POST -  localhost:8000/${data in proper format}
* PUT -  localhost:8000/getArticleDetail/<ObjectId (_id)>
* DELETE - localhost:8000/getArticleDetail/<ObjectId (_id)>

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### DATABASE - 
mongodb dumped database directry is present as API_CRUD_Mongo in the repository.

export that data in local machine mongoDB to try API(s)