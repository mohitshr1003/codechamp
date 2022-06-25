from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about_page),
    path('courses/', courses_page),
    path('faculty/', faculty_page),
    path('internship/', internship_page),
    path('contact/', contact_page),
    path('submitform/', form_page),
    path('login/', login_page),
    path('signup/', signup_page),
]
