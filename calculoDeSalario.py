salarioAtual = float(input("Digite o valor do seu salário atual: "))
print('')

if salarioAtual > 0 and salarioAtual <= 280.00:
  salarioReajuste= (280.00 * 0.2) + salarioAtual
  inflacao= salarioReajuste - (salarioReajuste * 0.038)
  valorAumento= salarioReajuste - salarioAtual

  print(f"O valor do seu salário atual é de: R${salarioAtual}")
  print('O percentual de aumento aplicado foi de 20%')
  print(f"O valor do aumento foi de: R${valorAumento}")
  print(f"O valor do seu salário reajustado é de: R${salarioReajuste}")
  print(f"O valor do reajuste descontando o valor da inflação é de: R${inflacao}")

elif salarioAtual > 280.00 and salarioAtual <= 700.00:
  salarioReajuste= (280.00 * 0.15) + salarioAtual
  inflacao= salarioReajuste - (salarioReajuste * 0.038)
  valorAumento= salarioReajuste - salarioAtual

  print(f"O valor do seu salário atual é de: R${salarioAtual}")
  print('O percentual de aumento aplicado foi de 15%')
  print(f"O valor do aumento foi de: R${valorAumento}")
  print(f"O valor do seu salário reajustado é de: R${salarioReajuste}")
  print(f"O valor do reajuste descontando o valor da inflação é de: R${inflacao}")

elif salarioAtual > 700.00 and salarioAtual <= 1500.00:
  salarioReajuste= (280.00 * 0.10) + salarioAtual
  inflacao= salarioReajuste - (salarioReajuste * 0.038)
  valorAumento= salarioReajuste - salarioAtual

  print(f"O valor do seu salário atual é de: R${salarioAtual}")
  print('O percentual de aumento aplicado foi de 10%')
  print(f"O valor do aumento foi de: R${valorAumento}")
  print(f"O valor do seu salário reajustado é de: R${salarioReajuste}")
  print(f"O valor do reajuste descontando o valor da inflação é de: R${inflacao}")

elif salarioAtual > 1500.00:
  salarioReajuste= (280.00 * 0.05) + salarioAtual
  inflacao= salarioReajuste - (salarioReajuste * 0.038)
  valorAumento= salarioReajuste - salarioAtual

  print(f"O valor do seu salário atual é de: R${salarioAtual}")
  print('O percentual de aumento aplicado foi de 5%')
  print(f"O valor do aumento foi de: R${valorAumento}")
  print(f"O valor do seu salário reajustado é de: R${salarioReajuste}")
  print(f"O valor do reajuste descontando o valor da inflação é de: R${inflacao}")