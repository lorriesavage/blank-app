import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

# for displaying images
from PIL import Image


st.title("🎈 Data Science App")

image_path = Image.open("Dark red aesthetic.jpeg")
st.image(image_path, width=400)

df = pd.read_csv("wine_quality_red.csv")
df.head(3)

st.dataframe(df.head(5))

st.subheader("01 Description of the Dataset")
st.dataframe(df.describe())

st.subheader("02 Missing values")
dfnull = df.isnull()/len(df)*100
totalMissing = dfnull.sum().round(2)
st.write(totalMissing)
st.write(dfnull)

if totalMissing[0] == 0.0:
    st.success("Congrats you have no missing values!")

st.subheader("03 Data Visualization")
listCols = df.columns
values = st.multiselect("Select two variables: ", listCols, ["quality", "citric acid"])


# creation of line chart
st.line_chart(df, x=values[0], y=values[1])

# bar chart
st.bar_chart(df, x=values[0], y=values[1])

# pairplot
PPvalues = st.multiselect("Select four variables: ", listCols, ["quality", "citric acid", "alcohol", "chlorides"])
df2 = df[[PPvalues[0], PPvalues[1], PPvalues[2], PPvalues[3]]]
pair = sns.pairplot(df2)
st.pyplot(pair)