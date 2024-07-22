import random
from re import S
from tokenize import group


def generate_student_data(n_students, courses, cities, random_seed=42):
    """
    Create a list of dict with dictionaries representing each attributes of each student.
    """
    random.seed(random_seed)
    return [
        {
            "rollno": i,
            "city": random.choice(cities),
            **{course: random.randint(1, 100) for course in courses},
        }
        for i in range(1, n_students + 1)
    ]


def groupby(data: list, key: callable):
    """
    Given a list of items, and a key, create a dictionary with the key as key function called
    on item and the list of items with the same key as the corresponding value.
    The order of items in the group should be the same order in the original list
    """
    grouped_data = {}
    for item in data:
        k = key(item)  # like len(item)
        if k not in grouped_data:
            grouped_data[k] = []
        grouped_data[k].append(item)

    return grouped_data


def apply_to_groups(groups: dict, func: callable):
    """
    Apply a function to the list of items for each group.
    """
    return {key: func(value) for key, value in groups.items()}


def min_course_marks(student_data, course):
    """Return the min marks on a given course"""
    return min(student_data, key=lambda data: data[course])[course]


def max_course_marks(student_data, course):
    """Return the max marks on a given course"""
    return max(student_data, key=lambda data: data[course])[course]


def rollno_of_max_marks(student_data, course):
    """Return the rollno of student with max marks in a course"""
    return max(student_data, key=lambda x: x[course])["rollno"]


def sort_rollno_by_marks(student_data, course1, course2, course3):
    """
    Return a sorted list of rollno sorted based on their marks on the three course marks.
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    """
    sorted_students = sorted(
        student_data, key=lambda data: (data[course1], data[course2], data[course3])
    )
    return list(map(lambda x: x["rollno"], sorted_students))


def count_students_by_cities(student_data):
    """
    Create a dictionary with city as key and number of students from each city as value.
    """
    return apply_to_groups(groupby(student_data, lambda x: x["city"]), len)


def city_with_max_no_of_students(student_data):
    """
    Find the city with the maximum number of students.
    """
    counts = count_students_by_cities(student_data)
    return max(counts, key=counts.get)


def group_rollnos_by_cities(student_data):
    """
    Create a dictionary with city as key and
    a sorted list of rollno of students that belong to
    that city as the value.
    """
    grouped_data = groupby(student_data, lambda x: x["city"])
    return {
        city: sorted(student["rollno"] for student in students)
        for city, students in grouped_data.items()
    }


def city_with_max_avg_course_mark(student_data, course):
    """
    Find the city with the maximum avg course marks.
    """
    grouped_data = groupby(student_data, lambda x: x["city"])
    avg_marks = {
        city: sum(student[course] for student in students) / len(students)
        for city, students in grouped_data.items()
    }
    return max(avg_marks, key=avg_marks.get)


# data = [
#     {"roll": 1, "city": "delhi", "Math1": 80, "ENG1": 80, "Stat2": 99},
#     {"roll": 2, "city": "kolkata", "Math1": 60, "ENG1": 50, "Stat2": 98},
#     {"roll": 3, "city": "chennai", "Math1": 89, "ENG1": 58, "Stat2": 22, "Math2": 59},
# ]

# basis = "Math1"
# print(max(data, key=lambda x: x[basis]))
