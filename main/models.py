from django.db import models


class Articles(models.Model):
    title = models.CharField('Bank name', max_length=50)
    int_rate = models.IntegerField('Interest rate')
    max_loan = models.IntegerField('Max loan')
    min_dep = models.IntegerField('Minimum down payment')
    loan_term = models.IntegerField('Loan term')

    def __str__(self):
        return f'Bank: {self.title}'

    def get_absolute_url(self):
        return f'/banking'

    class Meta:
        verbose_name = 'Your Bank'
        verbose_name_plural = "Your Banks"
