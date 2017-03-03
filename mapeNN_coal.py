errorsNN = [
-0.0926114,
-0.21521339,
-0.46527536,
-0.65714478,
-0.2871148,
0.107203652,
0.372890532,
0.563515566,
0.506639263,
0.096649156,
0.057088608,
0.100210894,
0.121458469,
0.218789308,
0.163585217,
0.102685932,
-0.09929114,
-0.32449542,
-0.13289752,
-0.18295602,
-0.63974505,
-0.19438792,
0.004073034,
-0.07990424,
0.008172259,
-0.11559311,
0.136842731,
0.278108333,
0.251236759,
-0.06144986,
-0.05966828,
-0.0803352,
-0.12094362,
0.009136388,
0.160669329,
0.193079348,
0.264832899,
0.226269247,
0.125714573,
-0.01019623

]

sumWrongErrors = 0
sumCorrectErrors = 0

absoluteErrorsNN = []

for i in range(len(errorsNN)):
    absoluteErrorsNN.append(abs(errorsNN[i]))

for i in range(len(errorsNN)):
    sumWrongErrors += errorsNN[i]

for i in range(len(absoluteErrorsNN)):
    sumCorrectErrors += absoluteErrorsNN[i]


print("MAPE errado: ", sumWrongErrors / len(errorsNN))  # 0.006240703924999988
print("MAPE correto: ", sumCorrectErrors / len(absoluteErrorsNN))  # 0.197201870925 ARIMA é melhor
