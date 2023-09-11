import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.header('Värderingsunderlag "VC method"')

float_pre_money = 0
float_pre_money2 = 0
float_pre_money3 = 0 
float_runda1 = 0
float_runda2 = 0
float_runda3 = 0
float_exit = 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header('Runda1')

    pre_money = st.text_input('Knappa in pre-money värdering, msek', )
    if pre_money:  # Check if the input is not empty
        try:
            float_pre_money = float(pre_money)  # Try converting the input to a float
            st.success(f"pre-money: {float_pre_money} msek")
        except ValueError:  # Handle the exception if the conversion fails
            st.error("Please enter a valid number.")


    runda1 = st.text_input('Hur mycket söker bolaget (msek)?')
    if runda1:
        try:
            float_runda1 = float(runda1) # Try converting input to a float
            st.success(f"kapitalbehov {float_runda1} msek")
        except ValueError: # Handle the exception if the conversion fails
            st.error('vänligen fyll i enbart siffror')

    post_money = float_pre_money + float_runda1
    dilution = float_runda1 / post_money * 100 if float_runda1 != 0 else 0
    st.header(f'post-money är {post_money} msek')
    st.write(f'{dilution:.2f} %')

with col2:
    st.header('Runda2')
    pre_money2 = st.text_input('Knappa in pre-money värdering för runda 2, msek', )
    if pre_money2:  # Check if the input is not empty
        try:
            float_pre_money2 = float(pre_money2)  # Try converting the input to a float
            st.success(f"pre-money 2a rundan: {float_pre_money2} msek")
        except ValueError:  # Handle the exception if the conversion fails
            st.error("vänligen fyll i enbart siffror")


    runda2 = st.text_input('Hur mycket söker bolaget i andra rundan (msek)?')
    if runda2:
        try:
            float_runda2 = float(runda2) # Try converting input to a float
            st.success(f"kapitalbehov {float_runda2} msek")
        except ValueError: # Handle the exception if the conversion fails
            st.error('vänligen fyll i enbart siffror')

    post_money2 = float_pre_money2 + float_runda2
    dilution2 = float_runda2 / post_money2 * 100 if float_runda2 != 0 else 0
    st.header(f'post-money är {post_money2} msek')
    st.write(f'{dilution2:.2f} %')


with col3:
    st.header('Runda3')
    pre_money3 = st.text_input('Knappa in pre-money värdering för runda 3, msek', )
    if pre_money3:
        try:
            float_pre_money3 = float(pre_money3) 
            st.success(f'pre-money 3e rundan: {float_pre_money3} msek')
        except ValueError: #handle the exception if
            st.error('vänligen fyll i enbart siffror')
    
    runda3 = st.text_input('Hur mycket söker bolaget i tredje rundan (msek)?')
    if runda3:
        try:
            float_runda3 = float(runda3)
            st.success(f'kapitalbehov {float_runda3} msek')
        except ValueError:
            st.error('vänligen fyll i enbart siffror')
    
    post_money3 = float_pre_money3 + float_runda3
    dilution3 = float_runda3 / post_money3 * 100 if float_runda3 != 0 else 0
    st.header(f'post-money är {post_money3} msek')
    st.write(f'{dilution3:.2f} %')

with col4:
    st.header('Värdering vid Exit')
    exit = st.text_input('fyll i värdering vid exit, msek')

    if exit:
        try:
            float_exit = float(exit)
            st.success(f'exit värdering: {float_exit} msek')
        except ValueError:
            st.error('vänligen fyll i enbart siffror')
    st.write("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.header(f'Värde vid exit är: {float_exit}')

st.write("---")

colA, colB = st.columns(2)

with colA:
    st.header('***' * 15)
    float_post_money3 = float_pre_money3 + float_runda3

    capital_raised= float_runda1 + float_runda2 + float_runda3

    st.write(f'Bolaget behöver {capital_raised}msek i extern equity')
    st.write('Om man bara deltagit i runda 1:')
   
    #variabler för olika beräkningar
    enbart_runda1 = dilution * ((100-dilution2)/100) * ((100-dilution3)/100)
    enbart_runda1_prc = enbart_runda1/100
    likvid_exit = enbart_runda1_prc * float_exit
    first_round_investor_x = (enbart_runda1_prc*float_exit) / float_runda1 if float_runda1 != 0 else 0
    first_round_investor_prc = (first_round_investor_x/ 1 - 1) * 100
    bolags_return_x = float_exit / float_pre_money if float_pre_money != 0 else 0
    
    st.write(f'Likvid vid försäljning: {likvid_exit:.2f} msek')
    st.write(f'Ägarandel från {dilution:.2f}% till {enbart_runda1:.2f}%')

    st.write(f'total utveckling {bolags_return_x:.2f}x')

    st.write(f'total utveckling om man bara deltagit i runda 1: {first_round_investor_x:.2f}x, eller {first_round_investor_prc:.2f}%')  


with colB:
    st.header('***' * 15)
    n_years = st.slider('välj tidshorisont', min_value=1, max_value=12, value=7)
    st.markdown(f"""
    Exitvärde: {float_exit}msek  
    Ägande har gått från {dilution:.2f}% till {enbart_runda1:.2f}%,  
    Investerat belopp från runda 1 är: {float_runda1}msek,  
    Så likvid till runda 1 inveseterare vid exit är: {likvid_exit:.2f} msek
    """)
    
    discount_factor = 1/n_years
    annualiserad_prc = ((likvid_exit/float_runda1) ** discount_factor - 1) *100
    st.write(f'annualiserad avkastning är {annualiserad_prc:.2f}%')

