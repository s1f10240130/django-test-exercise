from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample(self):
        # This is a sample test case
        self.assertEqual(1 + 2, 3)# This should fail to demonstrate a failing test