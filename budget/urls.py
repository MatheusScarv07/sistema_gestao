from budget.views import home,budget_search, search_budget_filter,new_budget, enviar_orcamento, cart, excluir_produto , clear_cart, efetuar_venda, page_details, delete_budget, editar_orcamento, salvar_orcamento, gerar_pdf, exportar
from django.urls import path


urlpatterns = [
    path('budget/', home),
    path('budget/search_budget/', budget_search, name='ver_orcamentos'),
    path('budget/new_budget/', new_budget),
    path('budget/enviar_orcamento/', enviar_orcamento),
    path('budget/filtrar_budget/', search_budget_filter),
    path('budget/salvar-carrinho/', cart),
    path('budget/excluir_produto/<int:id>/', excluir_produto),  # Nota: "/" no final
    path('budget/exportar/orcamentos', exportar),  # Nota: "/" no final
    path('budget/cancelar', clear_cart, name='cancelar_carrinho'),
    path('budget/new-sale/<int:num_orcamento>', efetuar_venda, name='aprovar_venda' ),
    path('budget/<int:number_budget>/info', page_details),
    path('budget/<int:number_budget>/delete', delete_budget),
    path('budget/editar/<int:number_budget>/', editar_orcamento, name='editar_orcamento'),
    path('orcamento/editar/salvar/<int:number_budget>/', salvar_orcamento, name='salvar_orcamento'),
    path('orcamento/gerar-pdf/<int:number_budget>', gerar_pdf, name='gerar_orcamento_pdf'),
    
]