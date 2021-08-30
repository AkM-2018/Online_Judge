from django.urls import path
from .views import HomeView, ProblemDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('problem/<int:pk>', ProblemDetail.as_view(), name='problem_detail')
]
