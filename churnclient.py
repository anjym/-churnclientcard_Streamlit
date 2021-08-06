import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets

import pickle

pickle_in = open('model.pkl', 'rb')
clf = pickle.load(pickle_in)
  

st.write('''
# PREDICTION DU CHURN CLIENT

''')



def pred(Total_Trans_Ct, Total_Revolving_Ba, Total_Relationship_Count, Total_Ct_Chng_Q4_Q1,Total_Trans_Amt,Months_Inactive_12_mon,Total_Amt_Chng_Q4_Q1):

	prediction = clf.predict(np.array([[Total_Trans_Ct, Total_Revolving_Ba, Total_Relationship_Count, 
		Total_Ct_Chng_Q4_Q1,Total_Trans_Amt,Months_Inactive_12_mon,Total_Amt_Chng_Q4_Q1]]).astype(np.float64))
	
	print(prediction)
	return prediction


def main():

	Total_Trans_Ct = st.text_input('Enter Total_Trans_Ct')
	Total_Revolving_Ba = st.text_input('Enter Total_Revolving_Ba')
	Total_Relationship_Count = st.text_input('Enter Total_Relationship_Count')
	Total_Ct_Chng_Q4_Q1 = st.text_input('Enter Total_Ct_Chng_Q4_Q1')
	Total_Trans_Amt = st.text_input('Enter Total_Trans_Amt')
	Months_Inactive_12_mon = st.text_input('Enter Months_Inactive_12_mon')
	Total_Amt_Chng_Q4_Q1 = st.text_input('Enter Total_Amt_Chng_Q4_Q1')
	submit = st.button('VALIDER')



	if submit:
		st.write('''#### Prediction...''')
		result = pred(Total_Trans_Ct, Total_Revolving_Ba, Total_Relationship_Count, Total_Ct_Chng_Q4_Q1,Total_Trans_Amt,Months_Inactive_12_mon,Total_Amt_Chng_Q4_Q1)
		if result==0:
			st.write("Attrited Customer")
		elif result==1:
			st.write("Existing Customer")
	

if __name__ == '__main__':
	main()

