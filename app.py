import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np

def load_data(file):
    df = pd.read_csv(file)
    return df

def data_checks(df):
    null_values = df.isnull().sum()
    duplicate_values = df.duplicated().sum()
    return null_values, duplicate_values

def visualize_numerical(df):
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    st.subheader("Numerical Columns Visualization:")
    for col in numerical_cols:
        st.subheader(f"{col} Distribution")
        fig = px.histogram(df, x=col, title=f"Distribution of {col}",color_discrete_sequence=["#008000"])
        st.plotly_chart(fig)

def visualize_categorical(df):
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    st.subheader("Categorical Columns Visualization:")
    for col in categorical_cols:
        st.subheader(f"{col} Distribution")
        value_counts = df[col].value_counts().reset_index()
        value_counts.columns = [col, 'count'] 
        fig = px.bar(value_counts, x=col, y='count', 
                     labels={col: col, 'count': 'Count'}, 
                     title=f"Distribution of {col}",color_discrete_sequence=["#1f77b4"])
        st.plotly_chart(fig)

def compare_with_target(df, target_column):
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    
    if target_column in numerical_cols:
        numerical_cols.remove(target_column)
    if target_column in categorical_cols:
        categorical_cols.remove(target_column)

    if len(numerical_cols) > 0:
        st.write(f"Comparing Numerical Columns with Target: {target_column}")
        for col in numerical_cols:
            fig = px.scatter(df, x=col, y=target_column, 
                             title=f"Comparison of {col} with {target_column}",color_discrete_sequence=["#FF1493"])
            st.plotly_chart(fig)

        if df[target_column].dtype in ['int64', 'float64']:  # Check if target column is numerical
            st.subheader(f"Correlation Heatmap between Numerical Columns and {target_column}")
            correlation_matrix = df[numerical_cols + [target_column]].corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            st.pyplot(fig)

    if len(categorical_cols) > 0:
        st.write(f"Comparing Categorical Columns with Target: {target_column}")
        for col in categorical_cols:
            if df[target_column].dtype == 'object':  
                fig = px.histogram(df, x=col, color=target_column, 
                                    title=f"Comparison of {col} with {target_column}")
                st.plotly_chart(fig)
            else:  
                fig = px.box(df, x=col, y=target_column, 
                             title=f"Box Plot of {target_column} by {col}",color_discrete_sequence=["#8A2BE2"])
                st.plotly_chart(fig)


def main():
    st.title("CSV Data Analysis App")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("Dataframe Loaded:")
        st.dataframe(df.head())
        st.subheader("Select Columns to Delete")
        columns_to_delete = st.multiselect("Select columns to delete", df.columns.tolist())
        
        if columns_to_delete:
            df = df.drop(columns=columns_to_delete)
            st.write(f"Updated Dataframe after deleting columns {columns_to_delete}:")
            st.dataframe(df.head())
        
        null_values, duplicate_values = data_checks(df)
        st.write("Null Values in Each Column:")
        st.write(null_values)
        st.write(f"Number of Duplicate Rows: {duplicate_values}")
        st.write(f'Shape of Dataframe: {df.shape}')
        
        visualize_numerical(df)
        visualize_categorical(df)
        
        target_column = st.selectbox("Select Target Column", df.columns.tolist())
        st.write(f"Target Column: {target_column}")
        
        compare_checkbox = st.checkbox("Compare Columns with Target Column")
        
        if compare_checkbox:
            compare_with_target(df, target_column)


if __name__ == "__main__":
    main()
