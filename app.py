import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


def load_csv():
    file = st.file_uploader("Upload your CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write(f"### Dataframe Shape: {df.shape}")
        st.write(f"### Duplicates Count: {df.duplicated().sum()}")
        st.dataframe(df.head())
        return df
    return None

def preprocess_data(df):
    
    st.sidebar.header("Data Preprocessing")
    columns_to_delete = st.sidebar.multiselect("Select columns to delete", df.columns.tolist())   
    if columns_to_delete:
        df = df.drop(columns=columns_to_delete)
    
    remove_dups = st.sidebar.checkbox("Remove Duplicates", value=True)
    if remove_dups:
        df = df.drop_duplicates()

    
    st.write("Data after Preprocessing:")
    st.dataframe(df.head())
    return df

def visualize_data(df):
    st.sidebar.header("Visualizations")
    visualize_option = st.sidebar.selectbox("Choose Visualization", ["Feature Distributions", "Target vs Features"])

    if visualize_option == "Feature Distributions":
        col = st.sidebar.selectbox("Select Feature for Distribution", df.columns)
        fig = px.histogram(df, x=col)
        st.plotly_chart(fig)
    
    elif visualize_option == "Target vs Features":
        target_column = st.sidebar.selectbox("Select Target Column", df.columns)
        feature_column = st.sidebar.selectbox("Select Feature to Compare with Target", df.columns)
        if df[feature_column].dtype == 'object':
            if (df[target_column].dtype == 'object'): 
                fig = px.histogram(df, x=feature_column, color=target_column, 
                                    title=f"Comparison of {feature_column} with {target_column}")
                st.plotly_chart(fig)
            else:  
                fig = px.box(df, x=feature_column, y=target_column, 
                             title=f"Box Plot of {target_column} by {feature_column}",color_discrete_sequence=["#8A2BE2"])
                st.plotly_chart(fig)

        elif df[feature_column].dtype in ['int64', 'float64']:
            if (df[target_column].dtype == 'object'): 
                fig = px.box(df, x=feature_column, y=target_column, 
                             title=f"Box Plot of {target_column} by {feature_column}",color_discrete_sequence=["#8A2BE2"])
                st.plotly_chart(fig)
            else:  
                fig = px.scatter(df, x=feature_column, y=target_column, 
                             title=f"Comparison of {feature_column} with {target_column}",color_discrete_sequence=["#FF1493"])
                st.plotly_chart(fig)


def main():
    st.title("Data Preprocessing and Model Building App")
    
    df = load_csv()
    
    if df is not None:
        df = preprocess_data(df)
        visualize_data(df)
    
if __name__ == "__main__":
    main()

