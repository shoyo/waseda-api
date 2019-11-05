# Rate My Waseda API
[![CircleCI](https://circleci.com/gh/shoyo/rate-my-waseda-api.svg?style=shield&circle-token=f6ab685a6862214510891e2fe190379012666e2b)](https://circleci.com/gh/shoyo-inokuchi/rate-my-waseda-api)

## About
Rate My Waseda API is a RESTful web interface for **courses**, **labs**, and **reviews** at Waseda University. It was initially built as a back end API for a course-reviewing app called "Rate My Waseda", but has since been released publicly to help the wider developer community at Waseda. It uses [Django](https://www.djangoproject.com) and the [Django REST Framework](https://www.django-rest-framework.org/).

## How to use
### Endpoints
`courses/` and `labs/`
* `GET`: show all courses or labs
* `POST`: create new course or lab **[admin]**

`courses/<int:pk>/` and `labs/<int:pk>/`
* `GET`: show course or lab
* `PUT`: update course or lab **[admin]**
* `DELETE`: delete course or lab **[admin]**

`courses/<int:pk>/reviews/` and `labs/<int:pk>/reviews/`
* `GET`: show all course reviews or lab reviews
* `POST`: create new course review or lab review **[user]**

`courses/<int:course_id>/reviews/<int:review_id>/` and `labs/<int:lab_id>/reviews/<int:review_id>/`
* `GET`: show course review or lab review
* `PUT`: update course review or lab review **[admin]**
* `DELETE`: delete course review or lab review **[admin]**

`users/`
* `GET`: show all users **[admin]**
* `POST`: create new user **[admin]**

`users/<slug:username>/`
* `GET`: show user **[admin]**
* `PUT`: update user **[admin]**
* `DELETE`: delete user **[admin]**

`api-auth-token/`
* `POST`: obtain an API authorization token

### Response Format
Course:

    {
        "title": str,
        "course_class_code": str,
        "course_code": str,
        "level": str, 
        "category": str, 
        "eligible_year": str,
        "credits": int,
        "main_language": str, 
        "school": str, 
        "campus": str, 
        "year": str, 
        "term": str, 
        "academic_disciplines": [
             str, 
             str, 
            str, 
        ],
        "instructors": [
            str,
            str,
            ...
        ],
        "syllabus_urls": [
            str,
        ],
        "sessions": [
            {
                "day": str, 
                "period": str, 
                "classrooms": [str, str]
            },
            {
                "day": str, 
                "period": str,
                "classrooms": [str]
            },
            ...
        ]
    }
    
Lab:
    
    {
        To be added
    }

### Examples
#### cURL
* GET an endpoint:  
`$ curl -X GET <endpoint>`
* Obtaining an API token:  
`$ curl -X POST https://api.ratemywaseda.com/api-auth-token/ -H 'Content-Type: application/json' -d '{"username": "<username>", "password": "<password>"}'`
* Authenticating a request:  
`$ curl -X <method> <endpoint> -H 'Content-Type: application/json' -H 'Authorization: Token <token>' -d '<payload>'`

#### Python
To be added

#### Javascript
To be added

## Development
Docker is used to install Python 3.6.8, install dependencies, and spin up a local Postgres database.
### Setting up
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and run the daemon.
* Run `$ docker-compose build` to build the image. This takes a few minutes.

### Developing
* Run `$ docker-compose up` to spin up containers and open `localhost:8000` to access the web interface.
* Run `$ docker-compose down` to clean up.

### Testing
* Run `$ docker-compose run api python manage.py test` to run tests. Test results will be displayed.
* **Note**: Always run `$ docker-compose down` afterwards to clean up.

## Contact
The current maintainer of this project is [Shoyo Inokuchi](https://github.com/shoyo-inokuchi). If you have any questions, you can send an email to shoyoinokuchi@gmail.com. If you would like to report a problem, you can [create a new issue](https://github.com/shoyo-inokuchi/rate-my-waseda-api/issues).
