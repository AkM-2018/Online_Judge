from django.db import models


class Problem(models.Model):
    statement = models.CharField(max_length=10000)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " | " + self.difficulty


class Solution(models.Model):
    submitted_code = models.FileField(upload_to='submissions/')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True, blank=True)


class TestCase(models.Model):
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
