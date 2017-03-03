testData = [
     122,    519,   1585,   5713, 10018,   
    8634,   6253,   1231,    239,    75,    
      56,    110,    171,    224,    219,    
     361,    517,    969,    738,    274,
     110,     36,     54,     60, 91,     
      90,    207,    268
]

predictedDataLSTM = [
   372.93981934,   362.70343018,    656.4019165,  1476.51953125,  4865.57617188,
  8197.84667969,  7181.86523438,  5307.49414062,   1199.5501709,    448.52728271,
   328.40447998,   314.56820679,   353.93652344,   398.57046509,   437.48928833,
   433.81222534,   538.67730713,   654.90496826,   997.39581299,   821.32873535,
   474.32180786,   353.93652344,   300.02191162,   313.11270142,   317.47970581,
   340.06918335,   339.33981323,   424.99194336
]

predictedDataARIMA = [
    611.124183,     892.4444444,    882.5620915,    1000.235294,    1991.869281,
    3831.424837,    5176.124183,    5833.934641,    5259.522876,    4462.130719,
    3723.575163,    3154.392157,    2809.30719,     2481.359477,    1937.091503,
    1321.830065,    717.3660131,    142.9215686,    -333.437908,    -879.294118,
    -1488.44444,    -1989.88889,    -1939.24837,    -1210.54902,    -466.058824,    
    142.1960784,    214.5816993,    205.6666667
]

predictedDataNN = [
    -267.988889,     -876.624306,   -1183.31736,    -1287.15486,    -558.217361,
    1685.759028,    4228.277083,    6539.861806,    6945.647917,    5647.919444,
    3122.459028,    378.9743056,    -2054.12847,    -3202.14444,    -3009.77292,
    -2064.30903,    -756.821528,    89.86944444,    608.4666667,    779.4402778,
    708.5902778,    533.6277778,    363.8611111,    138.0083333,    -68.39375,  
    -188.14166,7    -254.610417,    -183.15625
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


print("MAE ARIMA: ", arima_MAE) #2117.82 com poucos dados
print("MAE LSTM: ", lstm_MAE) #775.57 com poucos dados, 268.72 com muitos
print("MAE NN: ", nn_MAE) #2462,42 com poucos dados

