from budget.views import home,budget_search, search_budget_filter,new_budget, enviar_orcamento, cart, excluir_produto , gerar_relatorio , enviar_whatsapp, clear_cart, efetuar_venda, page_details
from django.urls import path


urlpatterns = [
    path('budget/', home),
    path('budget/search_budget/', budget_search, name='ver_orcamentos'),
    path('budget/new_budget/', new_budget),
    path('budget/enviar_orcamento/', enviar_orcamento),
    path('budget/filtrar_budget/', search_budget_filter),
    path('budget/salvar-carrinho/', cart),
    path('budget/excluir_produto/<int:id>/', excluir_produto),  # Nota: "/" no final
    path('budget/gerar-relatorio/', gerar_relatorio, name='gerar_relatorio'),  # Nota: caminho correto
    path('budget/enviar_whatsapp/', enviar_whatsapp, name='enviar_whatsapp'),  # Nota: "/" no final
    path('budget/cancelar', clear_cart, name='cancelar_carrinho'),
    path('budget/new-sale/<int:num_orcamento>', efetuar_venda, name='aprovar_venda' ),
    path('budget/<int:number_budget>/info', page_details)
    
]