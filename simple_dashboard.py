import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Chart"])
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", columns)

        if st.button("Generate Plot"):
            if plot_type == "Line Chart":
                st.line_chart(df.set_index(x_column)[y_column])
            elif plot_type == "Bar Chart":
                st.bar_chart(df.set_index(x_column)[y_column])
            elif plot_type == "Scatter Chart":
                st.scatter_chart(df.set_index(x_column)[y_column])
    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    st.write("Waiting on file upload...")