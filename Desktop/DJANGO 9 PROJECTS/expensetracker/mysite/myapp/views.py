from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm
from .models import Expense
import datetime
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("myapp:index")
    else:
        form = ExpenseForm()
    
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = sum(expense.amount for expense in expenses)
    
    #Logic to calc 365 day expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    datas = Expense.objects.filter(user=request.user, date__gt=last_year)
    yearly_sum = sum(data.amount for data in datas)
    
    #Logic to calc 30 day expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    datas = Expense.objects.filter(user=request.user, date__gt=last_month)
    monthly_sum = sum(data.amount for data in datas)
    
    #Logic to calc 7 day expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    datas = Expense.objects.filter(user=request.user, date__gt=last_week)
    weekly_sum = sum(data.amount for data in datas)
    
    daily_sums = Expense.objects.filter(user=request.user).values('date').order_by('date').annotate(sum=Sum('amount'))
    categorical_sums = Expense.objects.filter(user=request.user).values('category').order_by('date').annotate(sum=Sum('amount'))
    
    context = {
        "form":form,
        "expenses":expenses,
        "total_expenses": total_expenses,
        "yearly_sum": yearly_sum,
        "monthly_sum": monthly_sum,
        "weekly_sum": weekly_sum,
        "daily_sums": daily_sums,
        "categorical_sums": categorical_sums,
    }
    
    return render(request, "myapp/index.html", context)

@login_required
def edit(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("myapp:index")
    else:
        form = ExpenseForm(instance=expense) 
        
    return render(request, "myapp/edit.html", {"form": form})   

@login_required
def delete(request, id):
    Expense.objects.get(id=id).delete()
    return redirect("myapp:index")
    