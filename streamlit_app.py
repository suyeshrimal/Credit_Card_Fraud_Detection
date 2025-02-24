import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import joblib

model=joblib.load("best_model_decision_tree.pkl")
scaler=joblib.load("scaler.pkl")
type_oh=joblib.load("type.pkl")

st.image("creditcard.png",width=300)
st.title("Credit Card Fraud Detection")

Step=st.slider('step',1,1000)
Type=st.selectbox('type',['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER'])
Amount=st.number_input('amount')
OldbalanceOrg=st.number_input('oldbalanceOrg')
NewbalanceOrig=st.number_input('newbalanceOrig')
OldbalanceDest=st.number_input('oldbalanceDest')
NewbalanceDest= st.number_input('newbalanceDest')
IsFlaggedFraud=st.selectbox('isFlaggedFraud',[0,1])

# Prepare Input Data
input_data=pd.DataFrame({
    'step':[Step],
    'amount':[Amount],
    'oldbalanceOrg':[OldbalanceOrg],
    'newbalanceOrig':[NewbalanceOrig],
    'oldbalanceDest':[OldbalanceDest],
    'newbalanceDest':[NewbalanceDest],
    'isFlaggedFraud':[IsFlaggedFraud]
})

# One hot encode Type of payment

type_encoded=type_oh.transform(pd.DataFrame([Type], columns=['type'])).toarray()
type_encoded_df = pd.DataFrame(type_encoded,columns=['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER'])

input_data=pd.concat([input_data.reset_index(drop=True),type_encoded_df],axis=1)

# Scale input Data

input_data_scaled=scaler.transform(input_data)

#Prediction
if st.button("Predict Fraud"):
    prediction_proba = model.predict_proba(input_data_scaled)
    prediction_probability = prediction_proba[0][1]
    st.write(f"Fraud Probability: {prediction_probability:.2f}")

    if prediction_probability > 0.5:
        st.write("It is fraud")
    else:
        st.write("It is not fraud")


# prediction_proba = model.predict_proba(input_data_scaled)
# prediction_probability = prediction_proba[0][1]  # Probability of the fraud class (class 1)


# st.write(f"Fraud Probability: {prediction_probability:.2f}")

# if prediction_probability > 0.5:
#     st.write("It is fraud")
# else:
#     st.write("It is not fraud")