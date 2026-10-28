import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Course, Lesson, Question, Choice, Enrollment, Submission, Instructor, Learner

# Create admin superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Admin superuser created.")

# Create student user
student, created = User.objects.get_or_create(username='sumit', defaults={'first_name': 'Sumit', 'last_name': 'Kumar'})
if created:
    student.set_password('student123')
    student.save()
    print("Student user created.")

# Create instructor
instructor, _ = Instructor.objects.get_or_create(
    user=student,
    defaults={'full_time': True, 'total_learners': 150}
)

# Create learner profile
learner, _ = Learner.objects.get_or_create(
    user=student,
    defaults={'occupation': 'developer', 'social_link': 'https://github.com/sumit21012006'}
)

# Create course
course, _ = Course.objects.get_or_create(
    name='Introduction to Cloud Development with Django',
    defaults={
        'description': 'Learn full-stack web application development using Python, Django framework, and cloud databases.',
        'total_enrollment': 1
    }
)
course.instructors.add(instructor)

# Create lessons
lesson1, _ = Lesson.objects.get_or_create(
    title='Django MVT Architecture',
    order=0,
    course=course,
    defaults={'content': 'Django follows the Model-View-Template architectural pattern to separate business logic and presentation.'}
)

lesson2, _ = Lesson.objects.get_or_create(
    title='Models and Database Migrations',
    order=1,
    course=course,
    defaults={'content': 'Django models define database schema in Python code. Migrations automatically propagate changes into database tables.'}
)

# Create Question 1
q1, _ = Question.objects.get_or_create(
    course=course,
    question_text='Which architectural pattern is primarily used by Django framework?',
    defaults={'grade': 50}
)
c1_1, _ = Choice.objects.get_or_create(question=q1, choice_text='Model-View-Template (MVT)', defaults={'is_correct': True})
c1_2, _ = Choice.objects.get_or_create(question=q1, choice_text='Model-View-Presenter (MVP)', defaults={'is_correct': False})
c1_3, _ = Choice.objects.get_or_create(question=q1, choice_text='Microservices Architecture', defaults={'is_correct': False})

# Create Question 2
q2, _ = Question.objects.get_or_create(
    course=course,
    question_text='Which command is used to apply database migrations in Django?',
    defaults={'grade': 50}
)
c2_1, _ = Choice.objects.get_or_create(question=q2, choice_text='python manage.py migrate', defaults={'is_correct': True})
c2_2, _ = Choice.objects.get_or_create(question=q2, choice_text='python manage.py runserver', defaults={'is_correct': False})
c2_3, _ = Choice.objects.get_or_create(question=q2, choice_text='python manage.py createapp', defaults={'is_correct': False})

# Create enrollment
enrollment, _ = Enrollment.objects.get_or_create(user=student, course=course, defaults={'mode': 'honor'})

# Create a mock 100% submission
submission = Submission.objects.create(enrollment=enrollment)
submission.choices.add(c1_1, c2_1)
submission.save()

print(f"Data setup complete. Course ID: {course.id}, Submission ID: {submission.id}")
