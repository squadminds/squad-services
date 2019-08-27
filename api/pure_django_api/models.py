from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.CharField(max_length=256)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

    class Meta():
        ordering=('id',)
