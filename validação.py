print("algoritmo para Validação de CPF em Python")


ponto = '.'
traco = '-'
contador = 10
posicao = 0
acumulo = 0
resto = 0
cont = 11
pos = 0
res = 0
acu = 0
cpf = str(input('Digite seu CPF, sem traços e pontos: ')).strip()



if len(cpf) == 11 and cpf.isnumeric():
cpf_formatado = cpf[0:3] + ponto + cpf[3:6] + ponto + cpf[6:9] + traco + cpf[9:]
print(f'O CPF informado foi: {cpf_formatado}')

for i in range(len(cpf[0:9])):
primeiro = int(cpf[posicao]) * contador
posicao += 1
contador -= 1
acumulo = acumulo + primeiro

if contador < 2 and posicao > 8:
resto = acumulo % 11
primeiro_verificador = 11 - resto
if primeiro_verificador >= 10:
primeiro_verificador = 0
print(f'Este é o primeiro dígito verificador de seu CPF: {primeiro_verificador}')
for x in range(len(cpf[0:10])):
segundo = int(cpf[pos]) * cont
pos += 1
cont -= 1
acu = acu + segundo

if cont < 2 and pos > 9:
res = acu % 11
segundo_verificador = 11 - res
if segundo_verificador >= 10:
segundo_verificador = 0
print(f'Este é o segundo dígito verificador de seu CPF: {segundo_verificador}')
primeiro_verificador = str(primeiro_verificador)
segundo_verificador = str(segundo_verificador)
if primeiro_verificador == cpf[9] and segundo_verificador == cpf[10]:
print('O CPF foi analisado e aprovado. CPF válido!')
else:
print('CPF inválido!')
elif len(cpf) == 14 and '.' == cpf[3] and '.' == cpf[7] and '-' == cpf[11]:
print(f'O CPF informado foi: {cpf}')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

for i in range(len(cpf[0:9])):
primeiro = int(cpf[posicao]) * contador
posicao += 1
contador -= 1
acumulo = acumulo + primeiro

if contador < 2 and posicao > 8:
resto = acumulo % 11
primeiro_verificador = 11 - resto
if primeiro_verificador >= 10:
primeiro_verificador = 0
print(f'Este é o primeiro dígito verificador de seu CPF: {primeiro_verificador}')
for x in range(len(cpf[0:10])):
segundo = int(cpf[pos]) * cont
pos += 1
cont -= 1
acu = acu + segundo
if cont < 2 and pos > 9:
res = acu % 11
segundo_verificador = 11 - res
if segundo_verificador >= 10:
segundo_verificador = 0
print(f'Este é o segundo dígito verificador de seu CPF: {segundo_verificador}')
primeiro_verificador = str(primeiro_verificador)
segundo_verificador = str(segundo_verificador)
if primeiro_verificador == cpf[9] and segundo_verificador == cpf[10]:
print('O CPF foi analisado e aprovado. CPF válido!')
else:
print('CPF inválido!')

else:
print('CPF inválido!')
