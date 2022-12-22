# Import necessary modules.
import streamlit as st
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  st.title('View Data')
  # Display dataset within beta_expander.
  with st.beta_expander('View Full Dataset'):
    st.dataframe(census_df)
  # Show dataset summary on click of a checkbox.
  if st.checkbox('Show summary'):
    st.table(census_df.describe())
  col_1, col_2, col_3 = st.beta_columns(3)
  with col_1:
    if st.checkbox('Show all column names'):
      st.table(list(census_df.columns))
  with col_2:
    if st.checkbox('View column datatype'):
      st.table(census_df.dtypes)
  with col_3:
    if st.checkbox('View column data'):
      col = st.selectbox('Select column', tuple(census_df.columns))
      st.write(census_df[col])