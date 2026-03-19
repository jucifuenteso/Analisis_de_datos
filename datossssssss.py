import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="centered",
                    page_title="talento_tech",
                    page_icon="bar_chart")
st.title("analisis_de_datos")
st.markdown("hola mundo")

t1, t2 =st.columns((0.7,6.3))
t1.image("45.jpg", width=500)
t2.title("Analisis de datos con python")
t2.markdown("**tel: ** 3000000000")
steps = st.tabs(["pestaña 1"," pestaña 2",r'Pestaña $\sqrt{9}$'])
with steps[0]:
    st.write("contenido de la pestaña 1")
with steps[1]:
    st.title("pestaña2")
with steps[2]:
    df=pd.DataFrame({
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]})
    st.dataframe(df)#
    fig, ax= plt.subplots()
    ax=sns.barplot(x=['A','B','C'], y=[1,2,3],ax=ax)
    st.pyplot(fig)