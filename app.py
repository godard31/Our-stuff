import streamlit as st

st.title("Simple Calculator")

# Get user input
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Do the math
result = num1 + num2

# Display the result
st.write(f"Result: {result}")

import pandas as pd

df = pd.DataFrame({
    "Week": [1, 2, 3, 4, 5],
    "Model_ROI": [0.05, 0.08, 0.03, 0.12, 0.10]
})

st.write("Hello world")
st.write(42)
st.write(3.14)
st.write({"name": "John", "age": 30})
st.write(df)  # DataFrames too!

st.metric(label="NFL Spread Prediction", value="-3.5", delta="+0.2")
st.metric(label="Stock Price Target", value="$150", delta="-$5")

st.text("Plain text")
st.header("This is a header")
st.subheader("This is a subheader")

import pandas as pd

df = pd.DataFrame({
    "Team": ["Ravens", "Cowboys", "Chiefs"],
    "Win_Probability": [0.68, 0.55, 0.72]
})

st.dataframe(df)

import pandas as pd

df = pd.DataFrame({
    "Week": [1, 2, 3, 4, 5],
    "Model_ROI": [0.05, 0.08, 0.03, 0.12, 0.10]
})

st.line_chart(df.set_index("Week"))  # Line graph
st.bar_chart(df.set_index("Week"))   # Bar chart


