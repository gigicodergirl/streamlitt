import streamlit as st

st.set_page_config (page_title="Gymkhaana", page_icon=":tree:",layout="wide")
st.title("Welcome to Gymkhana Club")
st.header("Est.1958")
st.write("Gymkhana Registration Form")
st.warning("Registrations are full for the year 2026-27")
st.info("Only for premium members")
st.caption("Made by Gigi Sandhu")
#st.latex(r'''a^2+b^2=c^2''')
#st.camera_input("label=Visual verification")
st.checkbox("Are you above 18")
name = st.text_input('Enter your name')
email = st.text_input("Enter your email")
st.radio("Pick your gender",["Male","Female"])
st.number_input("Your age")
st.date_input('Enter your dob')
hobbies = st.multiselect('Select your hobbies',options=['Golf','Reading','Tennis','Pottery'])
st.multiselect("One condition or two to be choosen",["Hold OCI Card","Indian Citizen","Spouse of Indian National"])

agreement = st.checkbox('I agree to the terms and conditions')
btn=st.button("Submit")

if btn:
    if name and agreement:
        st.success(f'You are registered successfully')
        st.info(f'Hi {name}! Welcome on board with us')
        st.balloons()
    else:
        st.error("Enter name and agree with terms and conditions")    

tab1,tab2,tab3=st.tabs(['1','2','3'])
with tab1:
    st.image("btm.png")
#st.image("btm.png")
with tab2:
    st.camera_input("label=camera")
with tab3:   
      
     st.form('form')
     col1,col2=st.columns(2)
     with col1:
         name=st.text_input("Enter your Spouse name")
         age=st.number_input("Enter your age")
         city=st.text_input("Enter your city")
         agree=st.checkbox("Agree to these terms")





