def erroMedio(real, previsao):
    """

      :param real: Receberá o array dos valores reais do dado
      :param previsao: Receberá o coeficiente polinomial qual irá prever os valores da previsão
            Ex: coeficiente = np.poly1d(np.polyfit(x, y , 1))
            previsao irá receber coeficiente
      :return: Média entre a soma das diferenças entre o valor real e o valor da previsão, dividido pela amostra
      """
    soma = 0
    for c in range(0, len(real)):
        soma = soma + abs(int(previsao(c)) - real[c])
    return soma / len(real)


def erroMedioQuadratico(real, previsao):
    """

      :param real: Receberá o array dos valores reais do dado
      :param previsao: Receberá o coeficiente polinomial qual irá prever os valores da previsão
            Ex: coeficiente = np.poly1d(np.polyfit(x, y , 1))
            previsao irá receber coeficiente
      :return: Média entre a soma do quadrado das diferenças entre o valor real e o valor da previsão, dividido pela amostra
      """
    soma = 0
    for c in range(0, len(real)):
        soma = soma + ((int(previsao(c)) - real[c]) ** 2)
    return soma / len(real)


def erroMedioMediano(real, previsao):
    """

      :param real: Receberá o array dos valores reais do dado
      :param previsao: Receberá o coeficiente polinomial qual irá prever os valores da previsão
            Ex: coeficiente = np.poly1d(np.polyfit(x, y , 1))
            previsao irá receber coeficiente

      :return: Reorganizará uma lista de erro, e retornará o valor do meio, ou seja, mediano
      """
    lista = []
    for c in range(0, len(real)):
        lista.append(abs(int(previsao(c)) - real[c]))
    lista = sorted(lista)
    if len(lista) % 2 == 0:
        return (lista[int(len(lista) / 2)] + lista[int(len(lista) / 2) + 1]) / 2
    else:
        return lista[int(len(lista) / 2 + 0.5)]