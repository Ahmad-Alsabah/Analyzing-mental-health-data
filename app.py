import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 تحليل بيانات الصحة النفسية")

try:
    df = pd.read_csv("Mental Health Dataset.csv")
    st.success("✅ تم تحميل البيانات!")

    st.subheader("👀 معاينة البيانات")
    st.dataframe(df)


   
    def draw_small_plot(fig):
        fig.tight_layout(pad=0.5)
        st.pyplot(fig, use_container_width=False)

  
    st.subheader("👤 توزيع الجنس")
    fig1, ax1 = plt.subplots(figsize=(2, 1.5))
    sns.countplot(x='Gender', data=df, ax=ax1, palette='Set2', width=0.4)
    ax1.set_title("Gender", fontsize=7)
    ax1.set_xlabel("")
    ax1.set_ylabel("")
    ax1.tick_params(axis='x', labelsize=5)
    ax1.tick_params(axis='y', labelsize=5)
    draw_small_plot(fig1)

    
    st.subheader("😓 هل التوتر بازدياد؟")
    fig2, ax2 = plt.subplots(figsize=(2, 1.5))
    sns.countplot(x='Growing_Stress', data=df, ax=ax2, palette='coolwarm', width=0.4)
    ax2.set_title("Stress?", fontsize=7)
    ax2.set_xlabel("")
    ax2.set_ylabel("")
    ax2.tick_params(axis='x', labelsize=5)
    ax2.tick_params(axis='y', labelsize=5)
    draw_small_plot(fig2)

 
    st.subheader("🧠 الدعم النفسي")
    fig3, ax3 = plt.subplots(figsize=(2, 1.5))
    sns.countplot(x='care_options', data=df, ax=ax3, palette='Blues', width=0.4)
    ax3.set_title("Support", fontsize=7)
    ax3.set_xlabel("")
    ax3.set_ylabel("")
    ax3.tick_params(axis='x', labelsize=5, rotation=45)
    ax3.tick_params(axis='y', labelsize=5)
    draw_small_plot(fig3)

   
    st.subheader("🌍 الدول")
    top_countries = df['Country'].value_counts().head(10)
    fig4, ax4 = plt.subplots(figsize=(2, 1.5))
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax4, palette='mako')
    ax4.set_title("Countries", fontsize=7)
    ax4.set_xlabel("")
    ax4.set_ylabel("")
    ax4.tick_params(axis='x', labelsize=5)
    ax4.tick_params(axis='y', labelsize=5)
    draw_small_plot(fig4)

except FileNotFoundError:
    st.error("⚠️ لم يتم العثور على الملف 'Mental Health Dataset.csv' في المسار الحالي.")
