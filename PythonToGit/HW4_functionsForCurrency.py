
def currencyCalc(InputCurrencyAmount):

    rubToUsdRate = 0.0127
    rubToEurRate = 0.0113
    rubToChfRate = 0.0117
    rubToGbpRate = 0.0094
    rubToCnyRate = 0.0806

    convertRubToUsd = (InputCurrencyAmount) * rubToUsdRate
    convertRubToEur = (InputCurrencyAmount) * rubToEurRate
    convertRubToChf = (InputCurrencyAmount) * rubToChfRate
    convertRubToGbp = (InputCurrencyAmount) * rubToGbpRate
    convertRubToCny = (InputCurrencyAmount) * rubToCnyRate

    if InputCurrencyAmount > 0:
        print("Ты ввел", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в USD =", convertRubToUsd)
        print("Конвертированная сумма в EUR =", convertRubToEur)
        print("Конвертированная сумма в CHF =", convertRubToChf)
        print("Конвертированная сумма в GBP =", convertRubToGbp)
        print("Конвертированная сумма в CNY =", convertRubToCny)



def currencyCalc2(InputCurrencyAmount,ChooseCur):

    rubToUsdRate = 0.0127
    rubToEurRate = 0.0113
    rubToChfRate = 0.0117
    rubToGbpRate = 0.0094
    rubToCnyRate = 0.0806

    convertRubToUsd = (InputCurrencyAmount) * rubToUsdRate
    convertRubToEur = (InputCurrencyAmount) * rubToEurRate
    convertRubToChf = (InputCurrencyAmount) * rubToChfRate
    convertRubToGbp = (InputCurrencyAmount) * rubToGbpRate
    convertRubToCny = (InputCurrencyAmount) * rubToCnyRate

    if InputCurrencyAmount > 0 and ChooseCur =='USD':
        print("Вы ввели", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в USD =", convertRubToUsd)
    if InputCurrencyAmount > 0 and ChooseCur == 'EUR':
        print("Вы ввели", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в EUR =", convertRubToEur)
    if InputCurrencyAmount > 0 and ChooseCur == 'CHF':
        print("Вы ввели", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в CHF =", convertRubToChf)
    if InputCurrencyAmount > 0 and ChooseCur == 'GBP':
        print("Вы ввели", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в GBP =", convertRubToGbp)
    if InputCurrencyAmount > 0 and ChooseCur == 'CNY':
        print("Вы ввели", InputCurrencyAmount, "Рублей")
        print("Конвертированная сумма в CNY =", convertRubToCny)
