from sklearn import metrics
import pandas as pd

def logloss(pred, true):
    p = pred[true.WL != -1]
    t = true[true.WL != -1]
    return metrics.log_loss(t.WL, p.Pred)
