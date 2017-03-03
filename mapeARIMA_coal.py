errorsARIMA = [
-0.05308031,
-0.17402659,
-0.33304247,
-0.38154122,
-0.08491351,
0.154286599,
0.248730585,
0.337762592,
0.256290483,
-0.08070678,
0.024472574,
0.098397204,
0.109425962,
0.16266438,
0.078248588,
0.049193548,
-0.09554018,
-0.23236579,
-0.03636204,
-0.09324074,
-0.44913749,
-0.05539406,
0.051862256,
-0.06554842,
-0.01829565,
-0.14306973,
0.137758744,
0.214722222,
0.122718053,
-0.14803523,
-0.04712783,
-0.00767895,
-0.04942101,
0.027909426,
0.110566449,
0.131096836,
0.171495226,
0.114804411,
0.043780193,
-0.03154944

]

sumWrongErrors = 0
sumCorrectErrors = 0

absoluteErrorsARIMA = []

for i in range(len(errorsARIMA)):
    absoluteErrorsARIMA.append(abs(errorsARIMA[i]))

for i in range(len(errorsARIMA)):
    sumWrongErrors += errorsARIMA[i]

for i in range(len(absoluteErrorsARIMA)):
    sumCorrectErrors += absoluteErrorsARIMA[i]


print("MAPE errado: ", sumWrongErrors / len(errorsARIMA))  # 0.0016527222750000003
print("MAPE correto: ", sumCorrectErrors / len(absoluteErrorsARIMA))  # 0.13065659427499995 ARIMA é melhor
