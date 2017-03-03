testData = [
    105.47000518,    102.73999566,  105.01000375,   96.37999898,   94.09999915,
     86.83000327,     92.73999622,   93.19999765,   95.46999978,   96.37999898,
      99.5600003,    120.46999838,  123.19999598,  114.10999573,  120.92999981,
    102.73999566,    101.82999647,   95.46999978
]

predictedDataARIMA = [
     89.95209524,     89.08171429,    89.37133333,    94.19419048,    96.99628571,
    100.0215238,      99.35561905,    99.42895238,    99.02314286,    97.65533333,
     96.526,           95.97180952,   100.6299048,    105.0548571,    108.2250476,    
    114.5905714,     114.8757143,     114.5541905
]

predictedDataLSTM = [
    105.82287598,  101.85159302,  100.00953674,  101.54121399,   95.7454834,
     94.23936462,   89.5847168,    93.34968567,   93.64979553,   95.14237976,
     95.74548340,   97.86930084,  111.78569031,  113.52400208,  107.63762665,
    112.08052826,  100.00953674,   99.39605713
]

predictedDataNN = [
         124.11,    110.7733333,    97.89,          103.9466667,    95.01666667,
    87.58666667,    82.88666667,    89.86333333,    97.29333333,    96.53333333,
    98.19666667,    101.2266667,    129.56,              138.05,          112.9,
    117.1433333,    101.2233333,    89.4
]

errorsLSTM = 0
errorsARIMA = 0
errorsNN = 0
datasetSize = len(testData)

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataLSTM[i])
    errorsLSTM += absoluteError

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataARIMA[i])
    errorsARIMA += absoluteError

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataNN[i])
    errorsNN += absoluteError

lstm_MAE = errorsLSTM/datasetSize
arima_MAE = errorsARIMA/datasetSize
nn_MAE = errorsNN/datasetSize

print("MAE ARIMA: ", arima_MAE) #10.92 com poucos dados
print("MAE LSTM: ", lstm_MAE) #5.20 com poucos dados, 9.34 com muitos
print("MAE NN: ", nn_MAE) #7.67 com poucos dados

