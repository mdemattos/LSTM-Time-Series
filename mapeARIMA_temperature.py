temperatureErrorsARIMA = [
-1.34222222,
-1.40229885,
-0.79880952,
-0.63492063,
0.234042553,
0.778703704,
0.830409357,
0.702396514,
0.395111111,
0.204938272,
-0.14351852,
-1.09689922,
-2.08805031,
-2.98181818,
-0.99090909,
-0.51919192,
0.697333333,
0.990946502,
0.875925926,
0.665027322,
0.420772947,
0.073182957,
-0.16822917,
-0.72198582,
-1.17777778,
-2.27008547,
-7.01818182,
0.004761905,
0.555555556,
0.936507937,
0.873631841,
0.662601626,
0.345833333,
0.044871795,
-0.22811791,
-0.9379085,
-2.00983607,
-6.85925926,
-1.07301587,
0.122666667
]
sumWrongErrors = 0
sumCorrectErrors = 0

absoluteTemperatureErrorsARIMA = []

for i in range (len(temperatureErrorsARIMA)):
    absoluteTemperatureErrorsARIMA.append(abs(temperatureErrorsARIMA[i]))

for i in range (len(temperatureErrorsARIMA)):
    sumWrongErrors += temperatureErrorsARIMA[i]

for i in range (len(absoluteTemperatureErrorsARIMA)):
    sumCorrectErrors += absoluteTemperatureErrorsARIMA[i]


print("MAE errado: ", sumWrongErrors/len(temperatureErrorsARIMA)) # -0.6011953743
print("MAE correto: ", sumCorrectErrors/len(absoluteTemperatureErrorsARIMA)) # 1.1219564321999997 ARIMA é melhor
