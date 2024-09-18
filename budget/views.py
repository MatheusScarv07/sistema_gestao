from django.shortcuts import render
from datetime import datetime
from budget.models import BudgetInfo,Budget


# Create your views here.
def home (request):
  return render (request, 'budget/pages/home.html')





def budget_search(request):
  data = datetime.today()

  budget = BudgetInfo.objects.filter(data_orcamento=data)
  print(budget)
  return render(request, "budget/pages/search_budget.html",{"budget":budget})



def budget_detail(request, budget_id):
    budget_id = Budget.objects.filter(number_budget=budget_id)
        
    return render(request, "budget/pages/detail_budget.html",{"budget":budget_id})




