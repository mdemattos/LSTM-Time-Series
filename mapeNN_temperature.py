temperatureErrorsNN = [
    -0.18666667,
0.327586207,
0.267857143,
-0.28571429,
0.404255319,
0.277777778,
0.149122807,
-0.01960784,
-0.28,
0.092592593,
-0.20833333,
-0.46511628,
0.471698113,
0.393939394,
0.704545455,
-0.66666667,
0.56,
0.172839506,
-0.03703704,
-0.10655738,
0.014492754,
-0.15789474,
0,
-0.30851064,
0.130434783,
-0.12820513,
0.181818182,
1.404761905,
-0.73809524,
0.5,
0.059701493,
-0.12195122,
-0.2125,
-1.1387E-16,
-0.03401361,
-0.35294118,
0.06557377,
-0.11111111,
1.595238095,
-0.32
]

sumWrongErrors = 0
sumCorrectErrors = 0

absoluteTemperatureErrorsNN = []

for i in range (len(temperatureErrorsNN)):
    absoluteTemperatureErrorsNN.append(abs(temperatureErrorsNN[i]))

for i in range (len(temperatureErrorsNN)):
    sumWrongErrors += temperatureErrorsNN[i]

for i in range (len(absoluteTemperatureErrorsNN)):
    sumCorrectErrors += absoluteTemperatureErrorsNN[i]


print("MAE errado: ", sumWrongErrors/len(temperatureErrorsNN)) # 0.075832823175 
print("MAE correto: ", sumCorrectErrors/len(absoluteTemperatureErrorsNN)) # 0.312878941675 ARIMA é melhor
