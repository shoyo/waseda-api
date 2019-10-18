# Rate My Waseda API

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
* `PUT`: update course or lab **[must be admin**
* `DELETE`: delete course or lab **[must be admin]**

`/courses/<int:pk>/reviews` and `/labs/<int:pk>/reviews`
* `GET`: show all course reviews or lab reviews
* `POST`: create new course review or lab review **[must be logged in]**

`/courses/<int:course_id>/reviews/<int:review_id>` and `/labs/<int:lab_id>/reviews/<int:review_id>`
* `GET`: show course review or lab review
* `PUT`: update course review or lab review **[must be admin]**
