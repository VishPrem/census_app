# Import necessary modules.
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.title('Visualise Data')
  st.subheader('Visualisation Selector')
  # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
  # Store the current value of this widget in a variable 'plot_list'.
  plot_list = st.multiselect('Select the Charts/Plots', ('Count Plot', 'Pie Plot', 'Box Plot'))
  # Display count plot using seaborn module and 'st.pyplot()' 
  if 'Count Plot' in plot_list:
    plt.figure(figsize = (20,8))
    st.subheader('Count plot for distribution of records for unique workclass groups')
    sns.countplot(data = census_df, x = 'workclass')
    st.pyplot()
  # Display pie plot using matplotlib module and 'st.pyplot()'
  if 'Pie Plot' in plot_list:
    st.subheader('Pie Chart')
    plots = st.multiselect('Select the column for pie chart', ('Income', 'Gender'))
    if 'Income' in plots:
      plt.figure(figsize = (20,8))
      plt.title('Distribution of records for different income groups')
      values = census_df['income'].value_counts()
      plt.pie(values, labels = values.index, autopct = '%.2f%%')
      st.pyplot()
    if 'Gender' in plots:
      plt.figure(figsize = (20,8))
      plt.title('Distribution of records for different genders')
      values = census_df['gender'].value_counts()
      plt.pie(values, labels = values.index, autopct = '%.2f%%')
      st.pyplot()
  # Display box plot using matplotlib module and 'st.pyplot()'
  if 'Box Plot' in plot_list:
    st.subheader('Box Plot for the Hours Worked Per Week')
    plots = st.multiselect('Select the columns for boxplot', ('Income', 'Gender'))
    if 'Income' in plots:
      plt.figure(figsize = (20,8))
      plt.title('Distribution of Hours Worked Per Week for different income groups')
      sns.boxplot(y = census_df['income'], x = census_df['hours-per-week'])
      st.pyplot()
    if 'Gender' in plots:
      plt.figure(figsize = (20,8))
      plt.title('Distribution of Hours Worked Per Week for different genders')
      sns.boxplot(y = census_df['gender'], x = census_df['hours-per-week'])
      st.pyplot()