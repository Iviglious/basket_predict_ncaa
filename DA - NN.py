import numpy as np
import pandas as pd
from sklearn import linear_model, model_selection, metrics
from sklearn.ensemble import RandomForestClassifier
# NN
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.regularizers import l2, l1
from sklearn.preprocessing import StandardScaler
# Plotting
import matplotlib.pyplot as plt


def ExecuteLR(dX, dY, trIds, tsIds):
    logi = linear_model.LogisticRegression()
    logi.fit(dX[trIds], dY[trIds])
    return logi.predict_proba(dX[tsIds])[:, 1]  # get just the second array


def ExecuteRF(dX, dY, trIds, tsIds):
    cls_rf = RandomForestClassifier(n_estimators=100, random_state=np.random.RandomState(0))
    cls_rf = cls_rf.fit(dX[trIds], dY[trIds])
    return cls_rf.predict_proba(dX[tsIds])[:, 1]


def ExecuteNN(dX, dY, trIds, tsIds):
    stdScaler = StandardScaler()
    X_train_scaled = stdScaler.fit_transform(dX[trIds])
    X_test_scaled = stdScaler.transform(dX[tsIds])
    model = Sequential()
    model.add(Dense(2560, input_dim=dX[trIds].shape[1], init='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(18, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(18, activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    sgd = SGD(lr=0.1, momentum=0.1, decay=0.0, nesterov=False)
    model.compile(loss='binary_crossentropy', optimizer='sgd')
    hist = model.fit(X_train_scaled, dY[trIds], nb_epoch=100, batch_size=32, verbose=2, validation_split=0.1)
    return model.predict(X_test_scaled)[:, 0]


def GetStats(Label, Pred, Test):
    result = Pred
    # Log Loss
    ll = metrics.log_loss(Test, result)
    # ROC curve stats
    # fpr, tpr, _ = metrics.roc_curve(Test, result)
    # auc = metrics.auc(fpr, tpr)

    # get results rounded
    rightnum = 0
    for i in range(0, result.shape[0]):
        if result[i] >= 0.5:
            result[i] = 1
        else:
            result[i] = 0
        if result[i] == Test[i]:
            rightnum += 1
    # Accuracy
    acc = (1.0 * rightnum) / result.shape[0]
    # Mean Squared Error
    mse = metrics.mean_squared_error(Test, result)

    # return all
    return dict(
        {
            'Label': Label
            , 'LogLoss': ll
            , 'Accuracy': acc
            , 'MSE': mse
            # ,'fpr':fpr
            # ,'tpr':tpr
            # ,'auc':auc
        })


def CompareScenarios():
    print("CompareScenarios: Started...")

    # Prepare data
    data = pd.read_csv('dataset/All_PCBR_For_2002_2016_Matchup.csv')
    DataY = data.WL.ravel()
    # range goes until 2016 not including (until 2015 including)
    train = data.loc[data.Season.isin(range(2002, 2016))].drop(['WL', 'Season'],
                                                               axis=1).index.values  # use 2002-2015 as training
    test = data.loc[data.Season == 2016].WL.index.ravel()  # use 2016 as test
    CRdf = pd.DataFrame(columns=[
        'Label'
        , 'LogLoss'
        , 'Accuracy'
        , 'MSE'
        # ,'fpr'
        # ,'tpr'
        # ,'auc'
    ])  # DataFrame containing all stats

    # Scenario 1 - all features - LR
    # DataX = data.drop(['WL','Season'], axis=1).values
    # pred = ExecuteLR(DataX, DataY, train, test)
    # ResDict = GetStats('Sc 1', pred, DataY[test])
    # CRdf = CRdf.append(ResDict, ignore_index=True)

    '''
    # Scenario 2 - all features - NN
    DataX = data.drop(['WL','Season'], axis=1).values
    pred = ExecuteNN(DataX, DataY, train, test)
    ResDict = GetStats('SC 2 - NN', pred, DataY[test])
    CRdf = CRdf.append(ResDict, ignore_index=True)
    '''

    # Scenario 2 - NN with just the top 6 features
    # DataX = data.drop(['WL','Season'], axis=1).values
    DataX = data[['T1_AdjEM', 'T1_Luck', 'T2_AdjEM', 'T2_Luck']].values
    pred = ExecuteNN(DataX, DataY, train, test)
    ResDict = GetStats('SC 2 - NN', pred, DataY[test])
    CRdf = CRdf.append(ResDict, ignore_index=True)

    ## Scenario 3 - without EM features
    # DataX = data[['T1_AdjEM','T2_AdjEM','T2_AdjO','T1_AdjO','T2_AdjD','T1_AdjD']].values
    # pred = ExecuteLR(DataX, DataY, train, test)
    # pred = ExecuteRF(DataX, DataY, train, test)
    # ResDict = GetStats('Sc 3 - RF', pred, DataY[test])
    # CRdf = CRdf.append(ResDict, ignore_index=True)

    print("CompareScenarios: Finished.")

    return CRdf

# Start the comparison
CRDF = CompareScenarios()

# Show the stats
CRDF[['Label','LogLoss','Accuracy','MSE']]