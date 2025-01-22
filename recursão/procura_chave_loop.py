def procura_pela_chave(caixa_principal):
  pilha = caixa_principal.crie_uma_pilha_para_buscar()
  while pilha is not vazia:
    caixa = pilha.pegue_caixa()
    for item in caixa:
      if item.e_uma_caixa():
        pilha.append(item)
      elif item.e_uma_chave():
        print('achei a chave!')