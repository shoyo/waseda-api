# Rate My Waseda API
[![CircleCI](https://circleci.com/gh/shoyo-inokuchi/rate-my-waseda-api/tree/production.svg?style=shield&circle-token=f6ab685a6862214510891e2fe190379012666e2b)](https://circleci.com/gh/shoyo-inokuchi/rate-my-waseda-api/tree/production)

## Setting Up
Note: Python 3.6 is preferred since that's the version that's running on the EC2 instance, but 3.6+ should be fine.
* Clone this repo.
* Create a python virtual environment and run `$ pip install -r requirements.txt` to install dependencies.
* Add the following lines to your `~/.bash_profile`.

      # Rate My Waseda API environment variables
      export ENVIRONMENT="development"

  Update your terminal with this change by running `$ source ~/.bash_profile` or starting a new terminal.
* Run database migrations with `$ python manage.py migrate`.
* Run `$ python manage.py runserver` and open `http://localhost:8000`.

## Development
During development, run the environment locally and make requests to `http://localhost:8000/`.

## Testing
If you make any changes, you can run tests with `$ python manage.py test`. Note that the local server doesn't have to be running for testing to take place.

## Production
To interact with endpoints in production, make requests to `https://api.ratemywaseda.com/`.

## Endpoints
`users/`
* `GET`: show all users
* `POST`: create new user

`users/<slug:username>/`
* `GET`: show user
* `PUT`: update user **[must provide admin credentials]**
* `DELETE`: delete user **[must provide admin credentials]**

`courses/` and `labs/`
* `GET`: show all courses or labs
* `POST`: create new course or lab **[must provide admin credentials]**

`courses/<int:pk>/` and `labs/<int:pk>/`
* `GET`: show course or lab
* `PUT`: update course or lab **[must provide admin credentials]**
* `DELETE`: delete course or lab **[must provide admin crendentials]**

`courses/<int:pk>/reviews/` and `labs/<int:pk>/reviews/`
* `GET`: show all course reviews or lab reviews
* `POST`: create new course review or lab review **[must provide user credentials]**

`courses/<int:course_id>/reviews/<int:review_id>/` and `labs/<int:lab_id>/reviews/<int:review_id>/`
* `GET`: show course review or lab review
* `PUT`: update course review or lab review **[must provide admin credentials]**
* `DELETE`: delete course review or lab review **[must provide admin credentials]**

## Examples
### cURL
* `$ curl -X GET https://api.ratemywaseda.com/courses/`
* `$ curl -X POST -u username:password -d "param1=value1&param2=value2" https://api.ratemywaseda.com/courses/`
* `$ curl -X POST -H 'Content-Type: application/json' -u username:password -d '{"param1": "value1", "param2": "value2"}' https://api.ratemywaseda.com/courses/`

### Javascript
To be added
