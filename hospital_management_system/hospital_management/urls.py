from django.urls import path
from . import views
urlpatterns=[
    path('home',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact ,name="contact"),
    path('booking/',views.booking,name="booking"),
    path('doctors/',views.doctors,name="doctor"),
    path('department/',views.department,name="department"),

    # path('signup',views.signup,name='signup')
]

