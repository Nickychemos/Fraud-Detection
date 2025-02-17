import joblib
import streamlit as st
import numpy as np



@st.cache_resource

def load_model():
    return joblib.load('xg_model.pkl')

st.cache_resource.clear()


st.title('Model to Detect if a Transaction is Fraudulent')
st.subheader('This model will help detect if a transaction is fraudulent or not to help prevent theft')


model = load_model()

if model:
    st.header('Please input the following details')

Age = st.number_input('Age', min_value=0, max_value=120, value=0)
Transaction_Amount = st.number_input('Transaction Amount', min_value=0.00, value=0.00)
Account_Balance = st.number_input('Account Balance', min_value=0.00, value=0.00)
Transaction_Type = st.selectbox('What is the transaction type?', options=[(0, 'Bill Payment'), (1, 'Credit'), (2, 'Debit'), (3, 'Transfer'), (4, 'Withdrawl')], format_func=lambda x:x[1])
Transaction_type_value = Transaction_Type[0]
Merchant_Category = st.selectbox('What is the merchant category?', options=[(0, 'Clothing'), (1, 'Electronics'), (2, 'Entertainment'), (3, 'Groceries'), (4, 'Health'), (5, 'Restaurant')], format_func = lambda y:y[1])
Merchant_category_values = Merchant_Category[0]

user_input = np.array([Age, Transaction_Amount, Account_Balance, Transaction_type_value, Merchant_category_values])

if st.button('Predict'):
    prediction = model.predict(user_input.reshape(1,-1))
    transaction_status = 'fraudulent' if prediction[0] == 1 else 'non-fraudulent'
    st.subheader(f'The transaction is {transaction_status}')