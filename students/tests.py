from django.test import TestCase
form django.urls import reverse

class studentpageTests(Testcase):
    def test_student_form_page_loads(self):
        response=self.client.get(
            reverse("student_form")

        )self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"student_form")

# Create your tests here.
