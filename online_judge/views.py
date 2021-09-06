from online_judge.models import Problem
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Problem
from .forms import SubmitSolutionForm


class HomeView(ListView):
    model = Problem
    template_name = 'home.html'


class ProblemDetail(DetailView):
    model = Problem
    template_name = 'problem_detail.html'


def submit(request, id):
    return render(request, 'add_submission.html', {'form': SubmitSolutionForm()})
