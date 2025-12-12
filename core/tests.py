from django.test import TestCase
from core.models import Response


# Create your tests here.
class Test(TestCase):
    def test_api(self):
        response = Response.objects.create()
        res = self.client.get("/responses/fields/")
        print(res.json())
        self.assertEqual(res.json()[0]["status"], response.get_status_display())

        res = self.client.get("/responses/exclude/")
        print(res.json())
        self.assertEqual(res.json()[0]["status"], response.get_status_display())
