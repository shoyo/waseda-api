# Rate My Waseda API

## Setting Up
Note: Python 3.6 is preferred since that's the version that's running on the EC2 instance, but 3.6+ should be fine.
* Clone this repo.
* Create a python virtual environment and run `$ pip install -r requirements.txt` to install dependencies.
* Add the following line to your `~/.bash_profile`.

      export ENVIRONMENT="development"

  Update your terminal with this change by running `$ source ~/.bash_profile` or starting a new terminal.
* Run database migrations with `$ python manage.py migrate`.
* Run `$ python manage.py runserver` and open `http://localhost:8000`.

## Development
During development, run the environment locally and make requests to `http://localhost:8000/`.

## Production
To test endpoints in production, make requests to `https://api.ratemywaseda.com/`.

## Endpoints
`/users`
* `GET`: show all users
* `POST`: create new user

`/users/<slug:username>`
* `GET`: show user
* `PUT`: update user **[must be admin]**
* `DELETE`: delete user **[must be admin]**

`/courses` and `/labs`
* `GET`: show all courses or labs
* `POST`: create new course or lab **[must be admin]**

`/courses/<int:pk>` and `/labs/<int:pk>`
* `GET`: show course or lab
* `PUT`: update course or lab **[must be admin]**
* `DELETE`: delete course or lab **[must be admin]**

`/courses/<int:pk>/reviews` and `/labs/<int:pk>/reviews`
* `GET`: show all course reviews or lab reviews
* `POST`: create new course review or lab review **[must be logged in]**

`/courses/<int:course_id>/reviews/<int:review_id>` and `/labs/<int:lab_id>/reviews/<int:review_id>`
* `GET`: show course review or lab review
* `PUT`: update course review or lab review **[must be admin]**
* `DELETE`: delete course review or lab review **[must be admin]**

## Examples
### cURL
* `$ curl -X GET https://api.ratemywaseda.com/courses`
* `$ curl -X POST -u username:password -d "param1=value1&param2=value2&param3=value3" https://api.ratemywaseda.com/labs`

### Javascript
To be added
