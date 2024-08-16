import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle


#load the trained model:

model=tf.keras.models.load_model('model.h5')


#load the encoder and scaler:;


with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender=pickle.load(file)


with open ('ohe.pkl','rb') as file:
    onehot_encoder_geo=pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

## streamlit app:
st.title('Customer churn prediction')


#user inputs:

geography=st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender=st.selectbox('Gender',label_encoder_gender.classes_)
age=st.slider('Age',18,92)
balance=st.number_input('Balance')
credit_Score=st.number_input('Credit Score')
estimated_Salary=st.number_input('Estimated salary')
tenure=st.slider('Tenure',0,10)
num_of_products=st.slider('Number of products',1,4)
has_cr_card=st.selectbox('Has Credit card',[0,1])
is_Active_member=st.selectbox('Is active member',[0,1])

#prepare the input data:

input_data=pd.DataFrame({
    'CreditScore':[credit_Score],
    'Gender':[label_encoder_gender.transform([gender])[0]],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_Active_member],
    'EstimatedSalary':[estimated_Salary]
})



#one hot encoder:
geo_encoded=onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df=pd.DataFrame(geo_encoded,columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

#combine one-hot encoded columns with input data:

input_data=pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)

#scale the input data:

input_scaled=scaler.transform(input_data)

#prediction churn

prediction=model.predict(input_scaled)
prediction_proba=prediction[0][0]

st.write(f'Churn probablity:{prediction_proba: .2f}')



if prediction_proba >0.5:
    st.write('the customer is likely to churn')
else:
    st.write('the customer is not likely to churn')
