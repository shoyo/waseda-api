"""Parameters for defining database objects for unit tests in `tests.py`."""

users = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "password1",
        "year": "B1",
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "password": "password2",
        "year": "B2",
    },
]

courses = [
    {
        "eligible_year": "4th year and above", 
        "instructor": "KATTO, Jiro", 
        "year": "2019\u00a0", 
        "school": "School of Fundamental Science and Engineering", 
        "first_academic_disciplines": "Informatics", 
        "credits": 2, 
        "classroom": "54-204", 
        "third_academic_disciplines": "Graphics and Visualization", 
        "second_academic_disciplines": "Graphics and Visualization", 
        "level": "Final stage advanced-level undergraduate", 
        "syllabus_url": "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=2603034015012019260702401326", 
        "course_code": "INFE41ZL", 
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09", 
        "term_day_period": "spring semester\u00a0\u00a0Fri.2", 
        "title": "Advanced Image Information", 
        "category": "Elective Subjects", 
        "course_class_code": "01", 
        "main_language": "English", 
    }, 
    {
        "eligible_year": "4th year and above", 
        "instructor": "MAEHARA, Fumiaki", 
        "year": "2019\u00a0", 
        "school": "School of Fundamental Science and Engineering", 
        "first_academic_disciplines": "Electrical and Electronic Engineering",
        "credits": 2, 
        "classroom": "61-310",
        "third_academic_disciplines": "Commumication/Network Engineering",
        "category": "Elective Subjects",
        "second_academic_disciplines": "Electrical and Electronic Engineering",
        "level": "Final stage advanced-level undergraduate", 
        "syllabus_url": "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=2603034022012019260702401726",
        "course_code": "ELCX41ZL",
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09",
        "term_day_period": "spring semester\u00a0\u00a0Mon.3",
        "main_language": "English", 
        "course_class_code": "01", 
        "title": "Wireless Signal Processing", 
    },
]

course_reviews = [
    {
        "course": 1,
        "reviewer": 1,
        "overall_rating": 5,
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin risus ligula, in porta est elementum a. Praesent id nulla finibus, hendrerit nibh vitae, suscipit lacus. Donec et dolor ut nibh elementum viverra. Quisque sed sollicitudin felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque venenatis nulla et eros tristique vehicula. Etiam finibus, elit sed placerat mattis, tellus nisi viverra lorem, eget dignissim orci magna a mauris. Nullam interdum, nisi a tempus tempus, orci orci ullamcorper massa, eu rhoncus est leo sit amet mauris. Duis id porta nibh, quis luctus est. Curabitur eu accumsan lectus. Praesent arcu eros, lobortis nec feugiat non, sodales in mi. Quisque sed quam ac dolor commodo elementum vel at velit. Vestibulum metus tellus, fringilla ultricies imperdiet sit amet, fringilla vitae odio. Sed a neque congue, condimentum enim ut, suscipit leo. Sed non vulputate lorem. Ut congue eros ut nisl volutpat, in vehicula augue egestas.",
        "anonymous": False,
    },
    {
        "course": 2,
        "reviewer": 2,
        "overall_rating": 1,
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin risus ligula, in porta est elementum a. Praesent id nulla finibus, hendrerit nibh vitae, suscipit lacus. Donec et dolor ut nibh elementum viverra. Quisque sed sollicitudin felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque venenatis nulla et eros tristique vehicula. Etiam finibus, elit sed placerat mattis, tellus nisi viverra lorem, eget dignissim orci magna a mauris. Nullam interdum, nisi a tempus tempus, orci orci ullamcorper massa, eu rhoncus est leo sit amet mauris. Duis id porta nibh, quis luctus est. Curabitur eu accumsan lectus. Praesent arcu eros, lobortis nec feugiat non, sodales in mi. Quisque sed quam ac dolor commodo elementum vel at velit. Vestibulum metus tellus, fringilla ultricies imperdiet sit amet, fringilla vitae odio. Sed a neque congue, condimentum enim ut, suscipit leo. Sed non vulputate lorem. Ut congue eros ut nisl volutpat, in vehicula augue egestas.",
        "anonymous": True,
    }
]

labs = [
    {
        "professor": "Professor 1",
        "topic": "Topic 1",
        "website": "https://topic1.example.com",
    },
    {
        "professor": "Professor 2",
        "topic": "Topic 2",
        "website": "https://topic2.example.com",
    },
]

lab_reviews = [
    {
        "lab": 1,
        "reviewer": 1,
        "overall_rating": 5,
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin risus ligula, in porta est elementum a. Praesent id nulla finibus, hendrerit nibh vitae, suscipit lacus. Donec et dolor ut nibh elementum viverra. Quisque sed sollicitudin felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque venenatis nulla et eros tristique vehicula. Etiam finibus, elit sed placerat mattis, tellus nisi viverra lorem, eget dignissim orci magna a mauris. Nullam interdum, nisi a tempus tempus, orci orci ullamcorper massa, eu rhoncus est leo sit amet mauris. Duis id porta nibh, quis luctus est. Curabitur eu accumsan lectus. Praesent arcu eros, lobortis nec feugiat non, sodales in mi. Quisque sed quam ac dolor commodo elementum vel at velit. Vestibulum metus tellus, fringilla ultricies imperdiet sit amet, fringilla vitae odio. Sed a neque congue, condimentum enim ut, suscipit leo. Sed non vulputate lorem. Ut congue eros ut nisl volutpat, in vehicula augue egestas.",
        "anonymous": False,
    },
    {
        "lab": 2,
        "reviewer": 2,
        "overall_rating": 1,
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin risus ligula, in porta est elementum a. Praesent id nulla finibus, hendrerit nibh vitae, suscipit lacus. Donec et dolor ut nibh elementum viverra. Quisque sed sollicitudin felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque venenatis nulla et eros tristique vehicula. Etiam finibus, elit sed placerat mattis, tellus nisi viverra lorem, eget dignissim orci magna a mauris. Nullam interdum, nisi a tempus tempus, orci orci ullamcorper massa, eu rhoncus est leo sit amet mauris. Duis id porta nibh, quis luctus est. Curabitur eu accumsan lectus. Praesent arcu eros, lobortis nec feugiat non, sodales in mi. Quisque sed quam ac dolor commodo elementum vel at velit. Vestibulum metus tellus, fringilla ultricies imperdiet sit amet, fringilla vitae odio. Sed a neque congue, condimentum enim ut, suscipit leo. Sed non vulputate lorem. Ut congue eros ut nisl volutpat, in vehicula augue egestas.",
        "anonymous": True,
    }
]

