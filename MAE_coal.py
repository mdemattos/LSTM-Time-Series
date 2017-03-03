testData = [
    416,
    403,
    422,
    459,
    467,
    512,
    534,
    552
]

predictedDataARIMA = [
    419.1944444,
    422.9166667,
    410.2222222,
    408.25,
    405.7777778,
    424.1944444,
    472.6944444,
    527.8333333
]

predictedDataNN = [
    449.4194444,
    451.7402778,
    418.1444444,
    385.2527778,
    376.8319444,
    376.4055556,
    413.1722222,
    482.6055556
]

predictedDataLSTM = [
    434.63931274,
    437.32705688,  
    428.61315918,
    441.36782837,
    466.41656494,
    471.83572388, 
    502.06552124,
    516.57006836
]

errorsARIMA = 0
errorsNN = 0
errorsLSTM = 0
datasetSize = len(testData)

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataARIMA[i])
    errorsARIMA += absoluteError

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataNN[i])
    errorsNN += absoluteError

for i in range(datasetSize):
    absoluteError = abs(testData[i] - predictedDataLSTM[i])
    errorsLSTM += absoluteError

arima_MAE = errorsARIMA/datasetSize
nn_MAE = errorsNN/datasetSize
lstm_MAE = errorsLSTM/datasetSize

print("MAE ARIMA: ", arima_MAE) #40.02
print("MAE LSTM: ", lstm_MAE) #23.16
print("MAE NN:", nn_MAE) # 71.97