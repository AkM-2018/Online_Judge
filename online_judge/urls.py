from django.urls import path
from .views import HomeView, ProblemDetail
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('problem/<int:pk>', ProblemDetail.as_view(), name='problem_detail'),
    path('submit/<int:id>/', views.submit, name='submit-solution')
]
