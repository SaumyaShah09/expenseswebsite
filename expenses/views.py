from django.shortcuts import render
import expenseswebsite
from expenseswebsite import templates
# Create your views here.

def index(request):
    return render(request,'expenseswebsite/index.html')
def add_expenses(request):
    return render(request,'expenseswebsite/add_expenses.html')