testData = [
   4.20000009,   8.40000007,  13.3999995,   16.39999916,  16.00000011,
  15.60000016,  14.70000026,  10.19999986
]

predictedDataARIMA = [
    1.866666667,    0.533333333,    1.693333333,    5.533333333,
    10.46666667,    14.9,           18.05333333,    19.76666667,
]

predictedDataLSTM = [
   6.84588575,   6.84588575,   9.1156311,   11.88966942,  13.49961853,
  13.28898335,  13.0770092,   12.59543037
]

predictedDataNN = [
        7.3,    4.2,    12.6,   18.4,   19.4,
        15.6,   15.2,   13.8
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

print("MAE ARIMA: ", arima_MAE) #6.49 com poucos dados
print("MAE LSTM: ", lstm_MAE) #2.73 com poucos dados, 2.24 com muitos
print("MAE NN: ", nn_MAE) #2.20 com poucos dados

