from budget.views import home,budget_search, search_budget_filter,new_budget, enviar_orcamento, cart, excluir_produto
from django.urls import path


urlpatterns = [
    path('budget/',home ),
    path('budget/search_budget/',budget_search),
    path('budget/new_budget/', new_budget),
    path('budget/enviar_orcamento/',enviar_orcamento),
    path('budget/filtrar_budget/',search_budget_filter ),
    path('budget/salvar-carrinho/', cart),
    path('budget/excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
]