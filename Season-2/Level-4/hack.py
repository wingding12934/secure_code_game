# Simulate an attack by following these steps:

# 1. Start the application as instructed in 'code.py'
# 2. Enter the following in the planet input field: 
# &ltimg src='x' onerror='alert(1)'&gt

# The application should return a message stating that such a 
# planet is unknown to the system, without showing an alert box

from code import app, get_planet_info
import unittest
from flask_testing import TestCase

class MyTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        return app

    def test_index_route(self):
        planet = "&ltimg src='x' onerror='alert(1)'&gt"
        expected_info = 'XSS attempt detected. Input blocked.'
        result = get_planet_info(planet)
        self.assertEqual(result, expected_info)

if __name__ == '__main__':
    unittest.main()