from django.test import TestCase
from django.urls import reverse
from .models import Student
# Create your tests here.


class StudentModelTests(TestCase):
    def test_add(self):
        # self.client.post(reverse('my_app:get_student_list'))
        response = self.client.post('/my_app/get_student_list/')
        self.assertEqual(response.status_code, 200)
