import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# Create a connection object.
if st.button("Načítať dáta z dotazníka"):
    st.cache_data.clear()
from streamlit_gsheets import GSheetsConnection
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()



#df = pd.read_csv('data/data.csv')

column_name_mapping = {
    'Kde bývaš? ': 'Location',
    'Pohlavie ' : 'Pohlavie',
    'Z akého okresu pochádzaš?\n(napr. Pezinok)' : 'Bydlisko(okres)',
    'Názov školy \n(napríklad: ZŠ Vajanského Modra)' : 'Škola',
    'Ktorý ročník ZŠ navštevuješ?': 'Grade',
    'Čo najradšej robíš vo svojom voľnom čase?': 'Free Time Activity',
    'Aký je tvoj obľúbený predmet v škole?': 'Favorite School Subject',
    'Ktorá hra ťa baví najviac?': 'Favorite Game',
    'Ktorý film ťa baví najviac?': 'Favorite Movie',
    'Kam by si najradšej cestoval/-a?': 'Dream Travel Destination',
    'Ktorú aktivitu alebo hru hráš veľmi dobre?': 'Skilled Activity/Game',
    'Kedy si bol/-a hrdý/-á na niečo, čo si dokázal/-a urobiť?': 'Proud Achievement',
    'Čo je podľa teba najdôležitejšie na svete?': 'Top World Priority',
    'Prečo je dôležité pomáhať iným?': 'Importance of Helping Others',
    'Čo by si chcel/-a dosiahnuť, aby svet bol lepším miestom?': 'Contribution to a Better World',
    'Ktorá oblasť povolaní sa ti páči?': 'Preferred Career Field',
    'Máš nejaké vysnívané povolanie?\nak áno, napíš, ktoré povolanie je tvoje vysnívané a prečo?': 'Dream Job',
}
#rename columns in DataFrame using dictionary
df.rename(columns=column_name_mapping, inplace=True)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df['Preferred Career Field Short'] = df['Preferred Career Field'].str.split('(').str[0].str.strip()
df.drop("Časová pečiatka",axis=1, inplace=True)
df = df.dropna(how='all')





tab1, tab2, tab3, tab4, tab5 = st.tabs(["Spolu", "Ročník", "Mesto/dedina","Bydlisko(okres)","Škola"])

with tab1:
    
    grouped_df = df.groupby(['Pohlavie', 'Preferred Career Field Short']).size().reset_index(name='Count')

    pohlavie_rozdelit = st.toggle(label ='rozdeliť podľa pohlavia?', value=False)
    if pohlavie_rozdelit == False :
        fig = go.Figure()
        for gender in grouped_df['Pohlavie'].unique():
            
            color = ''
            if gender =='dievča':
                color = 'pink'
            else:
                color = 'green'
            data = grouped_df[grouped_df['Pohlavie'] == gender]
            fig.add_trace(go.Bar(
                x=data['Preferred Career Field Short'],
                y=data['Count'],
                name=gender,
                marker_color= color
            ))

        # Update layout
        fig.update_layout(
            barmode='group',
            title='Oblasť povolaní podľa pohlavia',
            xaxis=dict(title='Oblasť povolaní', tickangle=45),
            yaxis=dict(title='Žiaci spolu'),
            legend=dict(title='Pohlavie')
        )

        
        st.write(fig)
    else:
        genders = df['Pohlavie'].unique()

    # Create a bar graph for each gender
        for gender in genders:
            # Filter DataFrame for the current gender
            filtered_df = df[df['Pohlavie'] == gender]
            
            color = ''
            if gender =='dievča':
                color = 'pink'
            else:
                color = 'green'
            # Group the filtered DataFrame by 'Preferred Career Field Short' and count the occurrences
            grouped_df = filtered_df['Preferred Career Field Short'].value_counts().reset_index()
            grouped_df.columns = ['Preferred Career Field Short', 'Count']
            
            # Create bar graph
            fig = go.Figure(go.Bar(
                x=grouped_df['Preferred Career Field Short'],
                y=grouped_df['Count'],
                name=gender,
                marker_color= color
            ))
            
            # Update layout
            fig.update_layout(
                title=f'Oblasť povolaní {gender}',
                xaxis=dict(title='Oblasť povolaní', tickangle=45),
                yaxis=dict(title='Spolu')
            )
            
            # Show the plot
            st.write(fig)

with tab2:
    
    pohlavie_rozdelit_rocnik = st.toggle(label ='rozdeliť podľa pohlavia?', value=False, key = 144155) 
    
    if pohlavie_rozdelit_rocnik == False:
        grouped_df = df.groupby(['Grade', 'Pohlavie', 'Preferred Career Field Short']).size().reset_index(name='Count')

        # Get unique grades
        grades = df['Grade'].unique()
        grades = sorted(grades)
        # Create separate graphs for each unique value in the 'Grade' column
        for grade in grades:
            # Create a filtered DataFrame for the current grade
            filtered_df = grouped_df[grouped_df['Grade'] == grade]
            color = ''
            
            # Create a new figure for each grade
            fig = go.Figure()
            
            # Add traces for each gender
            for gender in filtered_df['Pohlavie'].unique():
                # Filter DataFrame for the current gender
                gender_df = filtered_df[filtered_df['Pohlavie'] == gender]
                if gender =='dievča':
                    color = 'pink'
                else:
                    color = 'green'
                
                fig.add_trace(go.Bar(
                    x=gender_df['Preferred Career Field Short'],
                    y=gender_df['Count'],
                    name=gender,
                    marker_color = color
                ))

            # Update layout
            fig.update_layout(
                barmode='group',
                title=f'Oblasť povolania podľa pohlavia {grade}',
                xaxis=dict(title='Oblasť povolaní', tickangle=45),
                yaxis=dict(title='Žiaci spolu'),
                legend=dict(title='Pohlavie')
            )
            
            # Show the plot
            st.write(fig)
    
    else:
        grouped_df = df.groupby(['Grade', 'Pohlavie', 'Preferred Career Field Short']).size().reset_index(name='Count')

# Get unique grades
        grades = df['Grade'].unique()
        grades = sorted(grades)
        # Create separate graphs for each unique value in the 'Grade' column
        for grade in grades:
            # Create a filtered DataFrame for the current grade
            filtered_df = grouped_df[grouped_df['Grade'] == grade]
            
            # Create separate graphs for boys and girls
            for gender in filtered_df['Pohlavie'].unique():
                if gender =='dievča':
                    color = 'pink'
                else:
                    color = 'green'
                
                # Filter DataFrame for the current gender
                gender_df = filtered_df[filtered_df['Pohlavie'] == gender]
                
                # Create a new figure for each grade, gender combination
                fig = go.Figure()
                
                # Add trace for the current gender
                fig.add_trace(go.Bar(
                    x=gender_df['Preferred Career Field Short'],
                    y=gender_df['Count'],
                    name=gender,
                    marker_color = color
                ))
                
                # Update layout
                fig.update_layout(
                    title=f'Oblasť povolania {gender} - {grade}',
                    xaxis=dict(title='Oblasť povolaní', tickangle=45),
                    yaxis=dict(title='Spolu')
                )
                
                # Show the plot
                st.write(fig)
                
with tab3:
    
    grouped_df = df.groupby(['Location', 'Pohlavie', 'Preferred Career Field Short']).size().reset_index(name='Count')
    
    pohlavie_rozdelit_bydlisko = st.toggle(label ='rozdeliť podľa pohlavia?', value=False, key = 14532633) 

# Get unique locations
    locations = df['Location'].unique()

# Create separate graphs for each unique value in the 'Location' column
    if pohlavie_rozdelit_bydlisko == False:
        for location in locations:
            # Create a filtered DataFrame for the current location
            filtered_df = grouped_df[grouped_df['Location'] == location]
            
            # Create a new figure for each location
            fig = go.Figure()
            
            # Add traces for each gender
            for gender in filtered_df['Pohlavie'].unique():
                if gender =='dievča':
                    color = 'pink'
                else:
                    color = 'green'
                # Filter DataFrame for the current gender
                gender_df = filtered_df[filtered_df['Pohlavie'] == gender]
                
                fig.add_trace(go.Bar(
                    x=gender_df['Preferred Career Field Short'],
                    y=gender_df['Count'],
                    name=gender,
                    marker_color = color
                ))

            # Update layout
            fig.update_layout(
                barmode='group',
                title=f'Oblasť povolania podľa pohlavia - {location}',
                xaxis=dict(title='Oblasť povolaní', tickangle=45),
                yaxis=dict(title='Spolu'),
                legend=dict(title='Pohlavie')
            )
            
            # Show the plot
            st.write(fig)
    else:
        grouped_df = df.groupby(['Location', 'Pohlavie', 'Preferred Career Field Short']).size().reset_index(name='Count')

# Get unique locations
        locations = df['Location'].unique()

        # Create separate graphs for each unique value in the 'Location' column
        for location in locations:
            # Create a filtered DataFrame for the current location
            filtered_df = grouped_df[grouped_df['Location'] == location]
            
            # Create separate graphs for each gender
            for gender in filtered_df['Pohlavie'].unique():
                # Filter DataFrame for the current gender
                gender_df = filtered_df[filtered_df['Pohlavie'] == gender]
                
                if gender =='dievča':
                    color = 'pink'
                else:
                    color = 'green'
                    
                # Create a new figure for each location and gender
                fig = go.Figure()
                
                fig.add_trace(go.Bar(
                    x=gender_df['Preferred Career Field Short'],
                    y=gender_df['Count'],
                    name=gender,
                    marker_color = color
                ))

                # Update layout
                fig.update_layout(
                    barmode='group',
                    title=f'Oblasť povolania {gender} - {location}',
                    xaxis=dict(title='Oblasť povolaní', tickangle=45),
                    yaxis=dict(title='Spolu'),
                    legend=dict(title='Pohlavie')
                )
                
                # Show the plot
                st.write(fig)

import plotly.express as px

with tab4:
    grouped_df = df.groupby(['Bydlisko(okres)', 'Preferred Career Field Short']).size().reset_index(name='Count')

    bydlisko_rozdelit = st.toggle(label='rozdeliť podľa okresu?', value=False)
    if bydlisko_rozdelit == False:
        fig = px.bar(grouped_df, x='Preferred Career Field Short', y='Count', color='Bydlisko(okres)',
                     title='Oblasť povolaní podľa okresu', barmode='group',
                     labels={'Preferred Career Field Short': 'Oblasť povolania', 'Count': 'Spolu', 'Bydlisko(okres)': 'Okres'})
        st.plotly_chart(fig)
    else:
        locations = df['Bydlisko(okres)'].unique()

        for location in locations:
            filtered_df = df[df['Bydlisko(okres)'] == location]
            grouped_df = filtered_df['Preferred Career Field Short'].value_counts().reset_index()
            grouped_df.columns = ['Preferred Career Field Short', 'Count']

            # Get a unique color for each location
            color = px.colors.qualitative.Alphabet[locations.tolist().index(location) % len(px.colors.qualitative.Alphabet)]

            fig = px.bar(grouped_df, x='Preferred Career Field Short', y='Count', color_discrete_sequence=[color],
                         title=f'Oblasť povolania podľa okresu {location}',
                         labels={'Preferred Career Field Short': 'Oblasť povolaní', 'Count': 'Spolu'})
            st.plotly_chart(fig)

import plotly.express as px

with tab5:
    grouped_df = df.groupby(['Škola', 'Preferred Career Field Short']).size().reset_index(name='Count')

    skola_rozdelit = st.toggle(label='rozdeliť podľa školy?', value=False)
    if skola_rozdelit == False:
        fig = px.bar(grouped_df, x='Preferred Career Field Short', y='Count', color='Škola',
                     title='Oblasť povolaní podľa školy', barmode='group',
                     labels={'Preferred Career Field Short': 'Oblasť povolania', 'Count': 'Spolu', 'Škola': 'Škola'})
        st.plotly_chart(fig)
    else:
        schools = df['Škola'].unique()

        for school in schools:
            filtered_df = df[df['Škola'] == school]
            grouped_df = filtered_df['Preferred Career Field Short'].value_counts().reset_index()
            grouped_df.columns = ['Preferred Career Field Short', 'Count']

            # Get a unique color for each school
            color = px.colors.qualitative.Alphabet[schools.tolist().index(school) % len(px.colors.qualitative.Alphabet)]

            fig = px.bar(grouped_df, x='Preferred Career Field Short', y='Count', color_discrete_sequence=[color],
                         title=f'Oblasť povolania podľa školy {school}',
                         labels={'Preferred Career Field Short': 'Oblasť povolaní', 'Count': 'Spolu'})
            st.plotly_chart(fig)
