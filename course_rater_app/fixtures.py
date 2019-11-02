"""Parameters for defining database objects for unit tests in `tests.py`."""
import json

users = [
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "password1",
        "year": "B1"
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "password": "password2",
        "year": "B2"
    },
    {
        "username": "admin",
        "email": "admin@example.com",
        "password": "password",
        "is_staff": True
    }
]

courses = [
    {
        "title": "Advanced Image Information",
        "course_class_code": "01",
        "course_code": "INFE41ZL",
        "level": "Final stage advanced-level undergraduate",
        "category": "Elective Subjects",
        "eligible_year": "4th year and above",
        "credits": 2,
        "main_language": "English",
        "school": "School of Fundamental Science and Engineering",
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09",
        "year": "2019\u00a0",
        "term": "spring semester",
        "academic_disciplines": [
            "Informatics",
            "Graphics and Visualization",
            "Graphics and Visualization"
        ],
        "instructors": [
            "KATTO, Jiro"
        ],
        "syllabus_urls": [
            "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=2603034015012019260702401326"
        ],
        "classrooms": [
            "54-204"
        ],
        "sessions": [
            ["Friday", "2"]
        ]
    },
    {
        "title": "Signal Processing",
        "course_class_code": "01",
        "course_code": "ABCDE",
        "level": "Final stage advanced-level undergraduate",
        "category": "Required Subjects",
        "eligible_year": "3rd year and above",
        "credits": 2,
        "main_language": "English",
        "school": "School of Fundamental Science and Engineering",
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09",
        "year": "2019\u00a0",
        "term": "spring semester",
        "academic_disciplines": [
            "Communications",
            "Informatics",
            "Computer Science"
        ],
        "instructors": [
            "Professor A"
        ],
        "syllabus_urls": [
            "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=qwerty"
        ],
        "classrooms": [
            "52-101"
        ],
        "sessions": [
            ["Wednesday", "6"]
        ]
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

