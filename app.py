import streamlit as st
import pandas as pd
import numpy as np

st.title("인공지능 시인 만들기")

st.header("목차")

st.subheader("1.LLM 이란")
st.write("대형 언어보델 ")
st.subheader("2.LLM 실습")

# st.button("test")

if st.button("여기 눌러보세요"):
    st.write("Data Loading")
    #데이터 로딩 함수는 여기에 입력
    

st.write("당신의 성별은?")

checkbox_btn1 = st.checkbox('female')
checkbox_btn2 = st.checkbox('male')

if checkbox_btn1:
    st.write("male")

if checkbox_btn2:
    st.write("famale")

selected_item = st.radio("Radio Part",("A","B","O","AB"))

if selected_item == "A":
    st.write("A형")
elif selected_item == "B":
    st.write("B형")
elif selected_item == "O":
    st.write("O형")
elif selected_item == "AB":
    st.write("AB형")
else:
    st.write("?")


option = st.selectbox('please select i  selectbox',('1학년','2학년','3학년'))

st.write('you selected: ',option)

multi_select = st.multiselect('please select something in multi sekectbox',("경제","컴공","경영"))

st.write('you selected: ',multi_select)

#height=np.array([172,187,167,188])
#{"height":['172','187','168','188']})
df=pd.DataFrame({"name":['arial','bryan','cymon','dominic']})
                
st.table(df)