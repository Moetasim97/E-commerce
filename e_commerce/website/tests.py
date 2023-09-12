from django.test import TestCase,Client
from django.urls import reverse
from website.models import *
import json
from django.contrib.auth.models import User
from website.forms import UserForm, CustomerForm  # Import your form classes
from website.views import registerCust  # Import your registration function
from django.test import override_settings

# Create your tests here.

@override_settings(ATOMIC_REQUESTS=False)
class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
    def test_home_GET(self):
        response=self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'website/home.html')


    
    def test_register_customer(self):
        # Define test data for the forms
        user_data = {
            "username": "testuser",
            "password": "testpassword",
            "email":"testEmail@test.com",
            "first_name":"test",
            "last_name":"case"
        }
        customer_data = {
            "phone":"0106968213",
            "address":"99 taayouniyeat smouha, sidi gaber, alexandria"
            
        }

        # Simulate a POST request
        response = self.client.post(reverse('registerCustomer'), { 
            "username": user_data["username"],
            "password": user_data["password"],
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "address": customer_data["address"],
             "phone": customer_data["phone"],
        })

        # Check if the registration was successful (e.g., status code, redirection)
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after successful registration

        # Check if a user and customer were created in the database
        self.assertTrue(User.objects.filter(username=user_data["username"]).exists())
        self.assertTrue(Customer.objects.filter(user__username=user_data["username"]).exists())

        # Check if the user is logged in
        self.assertTrue(self.client.login(username=user_data["username"], password=user_data["password"]))



 