a = input('quer saber seu IMC?(sim ou não)').lower().strip()
if a == 'sim':
            print('òtimo, vou precisar apenas de algumas informações:')
            peso = float(input('qual o seu peso em quilogramas?'))
            altura = float(input('qual a sua altura em metros?'))
            imc = peso / (altura ** 2)
            if imc >= 24.9:
                           print(f'seu IMC é:{imc:.2f}, seu peso está acima do recomendado')
            elif imc <= 18.5:
                             print(f'seu IMC é: {imc:.2f}, seu peso está abaixo do recomendado')
            else:
                 print(f'seu IMC é: {imc:.2f}, parabéns, seu peso está dentro dos limites recomendados')
elif a == 'não' or 'nao':
                         print('ok, mas se mudar de ideia estarei aqui!')
else:
     print('não entendi a sua resposta, tente novamente porfavor')
