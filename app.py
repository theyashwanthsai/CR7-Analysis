import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Load the Ronaldo dataset
# df = pd.read_csv('ronaldo_data.csv')
df=pd.read_csv("data.csv")
# Define the Streamlit app
def app():
    # Set the page title and favicon
    st.set_page_config(page_title='Ronaldo Analysis', page_icon=':soccer:')

    # Set the page heading
    st.title('Cristiano Ronaldo Analysis')

    # Add a sidebar with options
    options = ['Overview', 'Career Statistics', 'Performance Metrics']
    selection = st.sidebar.radio('Select an option:', options)

    # Show the overview page
    if selection == 'Overview':
        # Add a brief description
        st.write('This website provides an analysis of Cristiano Ronaldo, one of the greatest football players of all time.')

        # Show a photo of Ronaldo
        st.image('ronaldo.webp', caption='Cristiano Ronaldo')

        # Show some basic stats
        st.write('Here are some basic statistics about Ronaldo:')
        st.write('- Born: February 5, 1985 (age 37 years)')
        st.write('- Height: 1.87m')
        st.write('Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer who plays as a forward for Premier League club Manchester United and captains the Portugal national team...')
        # st.write('- Height: ', df['height_cm'].mean(), 'cm')
        # st.write('- Weight: ', df['weight_kg'].mean(), 'kg')

    # Show the career statistics page
    elif selection == 'Career Statistics':
        # Show some key career stats
        st.write('Here are some key career statistics for Ronaldo:')
        # st.write('- Appearances: ', df['appearances'].sum())
        # st.write('- Goals: ', df['goals'].sum())
        # st.write('- Assists: ', df['assists'].sum())
        # st.write('- Appearances: ')
        # st.write('- Goals: ')
        # st.write('- Assists: ')

        # Show a bar chart of his goals per season
        # goals_per_season = df.groupby('season')['goals'].sum()
        # fig, ax = plt.subplots()
        # ax.bar(goals_per_season.index, goals_per_season.values)
        # ax.set_title('Ronaldo Goals per Season')
        # ax.set_xlabel('Season')
        # ax.set_ylabel('Goals')
        # st.pyplot(fig)
        
        st.plotly_chart(px.histogram(
    df,
    x='Club',
    title="Goals per Clubs",
    log_x=False,
    log_y=False,
    height=500,
    ))
        
        
        goals_per_cp = px.histogram(df, x='Competition', title="Goals per competition", log_x=False, log_y=False, height=500, color='Club', hover_name='Club', hover_data=['Competition','Club'])
        st.plotly_chart(goals_per_cp)
        
        st.plotly_chart(px.histogram(
    df,
    x='Season',
    title="Goals per season",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Competition','Season','Club']))
        
        
    
    # Show the performance metrics page
    else:
        # Show some performance metrics
        st.write('Here are some performance metrics for Ronaldo:')
        # st.write('- Shots per game: ', df['shots_per_game'].mean())
        # st.write('- Dribbles per game: ', df['dribbles_per_game'].mean())
        # st.write('- Pass completion rate: ', df['pass_completion_rate'].mean())
        # st.write('Here are some performance metrics for Ronaldo:')
        # st.write('- Shots per game: ')
        # st.write('- Dribbles per game: ')
        # st.write('- Pass completion rate: ')

        st.plotly_chart(px.histogram(
    df,
    x='Playing_Position',
    title="Goals per playing Position",
    log_x=False,
    log_y=False,
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Playing_Position','Competition','Season','Club']))
        
        
        st.plotly_chart(px.histogram(
    df,
    x='Type',
    title="Goals per Type",
    log_x=False,
    log_y=False,
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Playing_Position','Competition','Season','Club']))
        # Show a scatter plot of shots and goals
        # fig, ax = plt.subplots()
        # ax.scatter(df['shots_per_game'], df['goals'])
        # ax.set_title('Ronaldo Shots vs. Goals')
        # ax.set_xlabel('Shots per game')
        # ax.set_ylabel('Goals')
        # st.pyplot(fig)

# Run the app
if __name__ == '__main__':
    app()
