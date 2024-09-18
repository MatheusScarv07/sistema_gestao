from budget.views import home,budget_search,budget_detail
from sale.views import enviar_orcamento
from django.urls import path


urlpatterns = [
    path('budget/',home ),
    path('budget/search_budget/',budget_search),
    path('budget/new_budget/', enviar_orcamento),
    path('orcamento/<int:budget_id>/', budget_detail)
]