# Rate My Waseda API

## Endpoints
`/users`
* `GET`: show all users
* `POST`: create new user

`/users/<slug:username>`
* `GET`: show user
* `PUT`: update user **[if request.user == user]** [\*]

`/courses` and `/labs`
* `GET`: show all courses or labs
* `POST`: create new course or lab **[if is_admin(request.user)]**

`/courses/<int:pk>` and `/labs/<int:pk>`
* `GET`: show course or lab
* `PUT`: update course or lab **[if is_admin(request.user)]**
* `DELETE`: delete course or lab **[if is_admin(request.user)]**

`/courses/<int:pk>/reviews` and `/labs/<int:pk>/reviews`
* `GET`: show all course reviews or lab reviews
* `POST`: create new course review or lab review **[if request.user.is_logged_in]**

`/courses/<int:course_id>/reviews/<int:review_id>` and `/labs/<int:lab_id>/reviews/<int:review_id>`
* `GET`: show course review or lab review
* `PUT`: update course review or lab review **[if request.user == user]** [\*]

[\*] Even when this condition is met, there are still restrictions on which properties can be updated. (review written date, account creation date, etc.)
