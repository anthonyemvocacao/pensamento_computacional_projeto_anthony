
# definimos o dicionário (base de dados) 
preco_frutas = {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0

}
# definimos qual fruta queremos procurar
fruta_desejada = 'maçã'

# fazemos a busca direta usando metodo .get()
# O .get() tenta encontrar uma fruta; se não achar, mostra 'fruta não encontrada'
resultado = preco_frutas.get(fruta_desejada, 'fruta não encontrada')

# exibimos o resultado 
print(f"O preço da {fruta_desejada} é R$ {resultado}")