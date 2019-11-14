"""Parameters for defining database objects for unit tests in `tests.py`."""
import json

users = [
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "password": "password1",
        "year": "B1"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "password": "password2",
        "year": "B2"
    },
    {
        "id": 3,
        "username": "admin",
        "email": "admin@example.com",
        "password": "password",
        "is_staff": True
    }
]

courses = [
    {
        "id": 1,
        "title": "Advanced Image Information",
        "course_class_code": "01",
        "course_code": "INFE41ZL",
        "level": "Final stage advanced-level undergraduate",
        "category": "Elective Subjects",
        "eligible_year": "4th year and above",
        "credits": 2,
        "main_language": "English",
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09",
        "year": "2019\u00a0",
        "term": "spring semester",
        "syllabus_url": "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=2603034015012019260702401326",
        "academic_disciplines": [
            "Informatics",
            "Graphics and Visualization",
            "Graphics and Visualization"
        ],
        "instructors": [
            "KATTO, Jiro"
        ],
        "schools": [
            "School of Fundamental Science and Engineering",
            "School of Advanced Science and Engineering",
            "School fo Creative Science and Engineering"
        ],
        "sessions": [
            {
                "day": "Friday",
                "period": "2",
                "classrooms": ["53-102"]
            },
            {
                "day": "Friday",
                "period": "2",
                "classrooms": ["55-102", "22-123"]
            }
        ]
    },
    {
        "id": 2,
        "title": "Signal Processing",
        "course_class_code": "01",
        "course_code": "ABCDE",
        "level": "Final stage advanced-level undergraduate",
        "category": "Required Subjects",
        "eligible_year": "3rd year and above",
        "credits": 2,
        "main_language": "English",
        "campus": "Nishi-Waseda\uff08Former: Okubo\uff09",
        "year": "2019\u00a0",
        "term": "spring semester",
        "syllabus_url": "https://www.wsl.waseda.jp/syllabus/JAA104.php?pLng=en&pKey=qwerty",
        "academic_disciplines": [
            "Communications",
            "Informatics",
            "Computer Science"
        ],
        "instructors": [
            "Professor A"
        ],
        "schools": [
            "School of Fundamental Science and Engineering",
            "School of Advanced Science and Engineering",
            "School fo Creative Science and Engineering"
        ],
        "sessions": [
            {
                "day": "Friday",
                "period": "2",
                "classrooms": ["53-102"]
            }
        ]
    }
]

labs = [
    {
        "id": 1,
        "professor": "Professor 1",
        "topic": "Topic 1",
        "website": "https://topic1.example.com",
    },
    {
        "id": 2,
        "professor": "Professor 2",
        "topic": "Topic 2",
        "website": "https://topic2.example.com",
    },
]
