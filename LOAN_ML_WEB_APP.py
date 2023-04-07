import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model=pickle.load(open("C:/Users/princ/ML_DEPLOY PROJECT/Loan_trained_model_wellpre.sav",'rb'))

def loan_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped) # Here model will predict whether the person has parkinson or not.
    print(prediction)
    if (prediction[0]==1):
      return "THE PERSON WILL BE ELIGIBLE FOR THE LOAN"
    else:
      return "THE PERSON WILL NOT BE ELIGIBLE FOR THE LOAN"
  
def main():
    # giving the title
    st.title("LOAN STATUS PREDICTION WEB APP")
    Gender=st.text_input('Enter the gender of person')
    if(Gender=='Male'):
        Gender=1
    else:
        Gender=0
    Married=st.text_input('Enter the marital status of person')
    if(Married=='Yes'):
        Married=1
    else:
        Married=0
    Dependents=st.text_input('Enter the number of dependents')
    Education=st.text_input('Enter the educational qualification')
    if(Education=='Graduate'):
        Education=1
    else:
        Education=0
    Self_Employed=st.text_input('Enter the self employment status')
    if(Self_Employed=='Yes'):
        Self_Employed=1
    else:
        Self_Employed=0
    ApplicantIncome=st.text_input('Enter the income of applicant')
    CoapplicantIncome=st.text_input('Enter the income of coapplicant')
    LoanAmount=st.text_input('Enter the amount of Loan')
    Loan_Amount_Term=st.text_input('Enter the term of Loan')
    Credit_History=st.text_input('Enter the history of credit')
    Property_Area=st.text_input('enter the type of place of property owned')
    if(Property_Area=='Urban'):
        Property_Area=2
    elif(Property_Area=='Semiurban'):
        Property_Area=1
    else:
        Property_Area=0
    
    # code for prediction
    Eligibility=''
    
    # creating a Button for Prediction
    if st.button('Loan prediction result'):
        Eligibility=loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
    
    st.success(Eligibility)
    
    
    
    
if __name__ =='__main__':
    main()