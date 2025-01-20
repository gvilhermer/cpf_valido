from projeto_cpf import validar_CPF
resposta = (input('Deseja criar um CPF? [S/N]')).upper()
if resposta in 'S':
    validar_CPF.cpf_valido(resposta)
else:
    print('pdp')