import os
import joblib
import tensorflow as tf
#from xgboost import XGBClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#model path
MODELS_DIR = os.path.join(BASE_DIR,"models")
DNN_MODEL_PATH = os.path.join(MODELS_DIR,"dnn_saved_model")
#XGB_MODEL_PATH = os.path.join(MODELS_DIR,"xgboost_model.json")
LR_MODEL_PATH =  os.path.join(MODELS_DIR,"logistic_regression.pk1")
#RF_MODEL_PATH = os.path.join(MODELS_DIR,"random_forrest.pk1")

LABEL_ENCODER_PATH = os.path.join(MODELS_DIR,"label_encoder.pk1")
SYMPTOMS_COLUMNS_PATH = os.path.join(MODELS_DIR,"symptom_columns.pk1")

#loading MODEL
#dnn
dnn_model = tf.saved_model.load(DNN_MODEL_PATH)

#xgboost
#xgb_model = XGBClassifier()
#xgb_model.load_model(XGB_MODEL_PATH)

#LR
lr_model = joblib.load(LR_MODEL_PATH)

#rf
#rf_model = joblib.load(RF_MODEL_PATH)

#label_encoder
label_encoder = joblib.load(LABEL_ENCODER_PATH)

#symptoms col
symptoms_columns = joblib.load(SYMPTOMS_COLUMNS_PATH)

print("All models Loaded succesfully")