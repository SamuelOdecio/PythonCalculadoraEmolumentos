print("Para FINALIZAR A EXECUÇÃO DO CODIGO - DIGITE 0\n")
#quantidade = int(input("Digite a quantidade de RECEBIMENTOS: "))
quantidade = 100
emolumentos = 0
contador = 0
repasse = 0
while (contador < quantidade):
    #contador = contador+1
    valor = float(input("Digite o Valor do título: R$"))
    if valor > 0 and valor <= 50.00:
        emolumentos = emolumentos + 48.30
        repasse = repasse + valor

    if valor >= 50.01 and valor <= 100:
        emolumentos = emolumentos + 48.72
        repasse = repasse + valor

    if valor >= 100.01 and valor <= 150.00:
        emolumentos = emolumentos + 49.60
        repasse = repasse + valor

    if valor >= 150.01 and valor <= 200.00:
        emolumentos = emolumentos + 55.00
        repasse = repasse + valor

    if valor >= 200.01 and valor <= 250.00:
        emolumentos = emolumentos + 59.05
        repasse = repasse + valor

    if valor >= 250.01 and valor <= 300.00:
        emolumentos = emolumentos + 61.75
        repasse = repasse + valor

    if valor >= 300.01 and valor <= 350.00:
        emolumentos = emolumentos + 67.15
        repasse = repasse + valor

    if valor >= 350.01 and valor <= 400.00:
        emolumentos = emolumentos + 71.20
        repasse = repasse + valor

    if valor >= 400.01 and valor <= 450.00:
        emolumentos = emolumentos + 76.60
        repasse = repasse + valor

    if valor >= 450.01 and valor <= 500.00:
        emolumentos = emolumentos + 80.65
        repasse = repasse + valor

    if valor >= 500.01 and valor <= 1000.00:
        emolumentos = emolumentos + 84.70
        repasse = repasse + valor

    if valor >= 1000.01 and valor <= 2000.00:
        emolumentos = emolumentos + 125.20
        repasse = repasse + valor

    if valor >= 2000.01 and valor <= 3000.00:
        emolumentos = emolumentos + 165.70
        repasse = repasse + valor

    if valor >= 3000.01 and valor <= 4000.00:
        emolumentos = emolumentos + 207.55
        repasse = repasse + valor

    if valor >= 4000.01 and valor <= 5000.00:
        emolumentos = emolumentos + 249.40
        repasse = repasse + valor

    if valor >= 5000.01 and valor <= 10000.00:
        emolumentos = emolumentos + 291.25
        repasse = repasse + valor

    if valor >= 10000.01 and valor <= 15000.00:
        emolumentos = emolumentos + 331.75
        repasse = repasse + valor

    if valor >= 15000.01 and valor <= 20000.00:
        emolumentos = emolumentos + 373.60
        repasse = repasse + valor

    if valor >= 20000.01 and valor <= 30000.00:
        emolumentos = emolumentos + 414.10
        repasse = repasse + valor

    if valor >= 30000.01 and valor <= 40000.00:
        emolumentos = emolumentos + 457.30
        repasse = repasse + valor

    if valor >= 40000.01 and valor <= 50000.00:
        emolumentos = emolumentos + 457.30
        repasse = repasse + valor

    if valor >= 50000.01 and valor <= 100000.00:
        emolumentos = emolumentos + 457.30
        repasse = repasse + valor

    if valor >= 100000.01:
        emolumentos = emolumentos + 457.30
        repasse = repasse + valor

    if valor == 0:
        contador = quantidade

print(f"\nVALOR DOS EMOLUMENTOS RECEBIDOS:      R${emolumentos:.2f}")
print(f"VALOR TOTAL DE REPASSE:               R${repasse:.2f}")
