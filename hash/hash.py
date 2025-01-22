votaram = {}
def verifica_eleitor(nome):
  if votaram.get(nome):
    print("Mande embora!")
  else:
    votaram[nome] = True
    print("Deixe votar!")
    
  cache = {}
  def pega_pagina(url):
    if cache.get(url):
      return cache[url]
    else:
      dados = pega_dados_do_servidor(url)
      cache[url] = dados
      return dados