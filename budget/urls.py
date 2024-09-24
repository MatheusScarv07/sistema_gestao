from budget.views import home,budget_search, search_budget_filter
from sale.views import enviar_orcamento
from django.urls import path


urlpatterns = [
    path('budget/',home ),
    path('budget/search_budget/',budget_search),
    path('budget/new_budget/', enviar_orcamento),
    path('budget/filtrar_budget/',search_budget_filter )
]