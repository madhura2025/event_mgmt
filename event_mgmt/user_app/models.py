from django.db import models

class User(models.Model):
    user_id = models.IntegerField(auto_created=True)
    fname = models.CharField(max_length=244)
    salary = models.IntegerField()

    def __str__(self):
        return self.fname

class Expense(models.Model):
    CATEGORY = [
    ('NEED', 'Need'),
    ('LUXURY', 'Luxury'),
    ('INVESTMENT', 'Investment')]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_title = models.CharField(max_length=244)
    expense_amount = models.IntegerField()
    
    date = models.DateField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY)

    def __str__(self):
        return self.expense_title

