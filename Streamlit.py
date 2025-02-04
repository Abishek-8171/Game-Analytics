import streamlit as st
import pandas as pd
import psycopg2

#Changing backround color of a webpage
bg_color = '#565251' # This color code taken from HTML color codes 
st.markdown(f"""<style>.stApp {{background-color: {bg_color};}}</style>""",unsafe_allow_html=True)
#Creating logo & Name for the page
logo,name=st.columns([2,5],gap="large")
logo.image(r"E:\tennis images\22656791.jpg")
name.title("**Tennis Explorer**")
st.subheader("Stay updated with the latest tennis tournaments, player rankings, and match points.Dive into the world of tennis all in one place! 🚀")
#Creating a sidebar to explore the details
user=st.sidebar.radio("Explorer",["Home","Compeditions","Players Info","Points Table","Rank"],index=0) 
if user ==  "Compeditions":
    st.header("""All Tournment Details :tennis:""")
    connection = psycopg2.connect(
    host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
    cursor = connection.cursor()
    cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments") 
    comp = cursor.fetchall() 
    comp1=pd.DataFrame(comp)
    comp1.columns=['competition_name','type','gender','category_name','level']
    st.dataframe(comp1)  
    user_s=st.sidebar.selectbox('Gender',['Select','Men','Women','Mixed'],index=0)
    if user_s=='Men':
        st.subheader("Men's competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where gender='men'") 
        men = cursor.fetchall() 
        men_df=pd.DataFrame(men)
        men_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(men_df)  
    if user_s=='Women':
        st.subheader("Women's competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where gender='women'") 
        women = cursor.fetchall() 
        women_df=pd.DataFrame(women)
        women_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(women_df)   
    if  user_s=='Mixed':
        st.subheader("Mixed competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where gender='mixed'") 
        mixed = cursor.fetchall() 
        mixed_df=pd.DataFrame(mixed)
        mixed_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(mixed_df)      
    user_s1=st.sidebar.selectbox('Type',['Select','Doubles','Mixed','Mixed_Doubles','Singles'],index=0)
    if   user_s1=='Doubles':
        st.subheader("Filterded type competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where type='doubles'") 
        Doubles = cursor.fetchall() 
        Doubles_df=pd.DataFrame(Doubles)
        Doubles_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(Doubles_df) 
    if  user_s1=='Mixed':
        st.subheader("Filterded type competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where type='mixed'") 
        Mixed = cursor.fetchall() 
        Mixed_df=pd.DataFrame(Mixed)
        Mixed_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(Mixed_df)
    if   user_s1=='Mixed_Doubles':
        st.subheader("Filterded type competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where type='mixed_doubles'") 
        md = cursor.fetchall() 
        md_df=pd.DataFrame(md)
        md_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(md_df)
    if   user_s1=='Singles':
        st.subheader("Filterded type competitions")
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select competition_name,type,gender,category_name,level from tennis_tournaments where type='singles'") 
        Singles = cursor.fetchall() 
        Singles_df=pd.DataFrame(Singles)
        Singles_df.columns=['competition_name','type','gender','category_name','level']
        st.dataframe(Singles_df)


if user ==  "Players Info":
    name1,logo1=st.columns([5,2],gap="small")
    name1.header("""Players details :man: :woman:""")
    logo1.image(r"E:\tennis images\view-tennis-player-with-digital-art-style-effect.jpg")
    connection = psycopg2.connect(
    host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
    cursor = connection.cursor()
    cursor.execute("select name,country,country_code from points_details") 
    ply_info = cursor.fetchall()
    ply_info_df=pd.DataFrame(ply_info)
    ply_info_df.columns=['name','country','country_code']
    st.dataframe(ply_info_df)  
if user ==  "Points Table":    
    logo2,name2=st.columns([1,5],gap="small")
    logo2.image(r"E:\tennis images\20757533.jpg")
    name2.header("""Top players""")
    connection = psycopg2.connect(
    host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
    cursor = connection.cursor()
    cursor.execute("select name,competitions_played,points,country from points_details order by points desc") 
    points = cursor.fetchall()
    points_df=pd.DataFrame(points)
    points_df.columns=['name','competitions_played','points','country']
    st.dataframe(points_df)  
if user ==  "Rank":
    name3,logo3=st.columns([5,2],gap="small")
    name3.header("""Players Rank""")
    logo3.image(r"E:\tennis images\1000093142.jpg")
    connection = psycopg2.connect(
    host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
    cursor = connection.cursor()
    cursor.execute("select rank_id,rank,name,points,country from points_details order by rank asc") 
    rank = cursor.fetchall()
    rank_df=pd.DataFrame(rank)
    rank_df.columns=['rank_id','rank','name','points','country']
    st.dataframe(rank_df)
    user_s2=st.sidebar.selectbox("",['Rank','Top 5','Top 10'],index=0)
    if user_s2=='Top 5':
        st.subheader('Top 5 Rank holders')
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select rank,name,points,country from points_details where rank <= 5 order by rank asc") 
        t5 = cursor.fetchall()
        t5_df=pd.DataFrame(t5)
        t5_df.columns=['rank','name','points','country']
        st.dataframe(t5_df)
    if user_s2=='Top 10':
        st.subheader('Top 10 Rank holders')
        connection = psycopg2.connect(
        host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
        cursor = connection.cursor()
        cursor.execute("select rank,name,points,country from points_details where rank <= 10 order by rank asc") 
        t10 = cursor.fetchall()
        t10_df=pd.DataFrame(t10)
        t10_df.columns=['rank','name','points','country']
        st.dataframe(t10_df)   


#Venues and complex details
name4,logo4=st.columns([5,2],gap="small")
name4.header("""Venues & Complexes""")
logo4.image(r"E:\tennis images\wp7274426-tennis-court-wallpapers.jpg")
connection = psycopg2.connect(
host = "localhost",user = "postgres" , password = "begin25",database = "game_analytics")
cursor = connection.cursor()
cursor.execute("select complex_name,venue_name,city_name,country_name,timezone from tennis_courts") 
venues = cursor.fetchall()
venues_df=pd.DataFrame(venues)
venues_df.columns=['complex_name','venue_name','city_name','country_name','timezone']
st.table(venues_df) 
st.image(r"E:\tennis images\tennis-ball-move1.gif")