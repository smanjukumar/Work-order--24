#Title name
import streamlit as st
st.title("EDI-42 Work order sheet")


#Login page
username = st.text_input('Username')
password =st.text_input('password',type='password')


#Login button
if st.button("Login"):

 if username == 'z606215' and password == 'Manju':
     st.write('loged in as {}'.format(username))
 else:
     st.write("Invalid Username or Password")

#create data frame
import pandas as pd
Name= st.text_input("Enter your name")
Monday = st.number_input(" enter your Monday hours")
Tuesday = st.number_input(" enter your Tuesday hours")
wednesday = st.number_input(" enter your wednesady hours")
Thursday = st.number_input(" enter your Thursday hours")
Friday = st.number_input("enter your friday hours")

df = pd.DataFrame({ 
        "Name": [Name],
        "Monday": [Monday],
        "Tuesday": [Tuesday],
        "wednesday": [wednesday],
        "Thurday": [Thursday],
        "Friday" : [Friday]
})
df

from PIL import Image
logo = Image.open('logo.png')
st.sidebar.image(logo, width=200)

#Read the data 
import pandas as pd
df = pd.read_csv('work order.csv')
df

#side bar
st.sidebar.title("Filters")
Name= st.sidebar.selectbox("Name",['Manjukumar','Ganesh ','Sai Teja','Veerababu','Yuvraja Sekar','Mohammad Ameer','Prasad Boga','Afzal Khan','Charan']
                           )
#Filter the data 
filtered_df=df[df["Name"] == Name]
filtered_df

#Search box
import pandas as pd
st.header("Serach box")
search_term= st.text_input('Enter the project Name')
searched_df= df[df['project Name'].str.contains(search_term, case= False)]
searched_df

#serahed box 2
st.header("search name")
find=st.text_input("Enter the employe name")
find_df=df[df["Name"].str.contains(find,case=False)]
find_df

Monday_hours= st.number_input('Enter Monday hours')
st.write("You have Enter the hours:",Monday_hours)
if Monday_hours<9:
    st.write("work is requied")
else:
    st.write("work load is ok")

#Footer 
st.sidebar.title('AI App Developer  ')
st.sidebar.info("Manjukumar.s")

#pie chart
st.header('Pie chart')
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax= plt.subplots()
sns.countplot(df['Name'],ax=ax)
st.pyplot(fig)

#pie chart
st.header('Pie chart')
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax= plt.subplots()
sns.countplot(df['Name'],ax=ax)
st.pyplot(fig)

#simple chart 

st.header('simple pie chart')
st.write(df['Name'].value_counts())
total_count=df['Name'].value_counts()

fig, ax = plt.subplots()
ax.pie(total_count,labels=total_count.index,autopct='%1.1f%%')
st.pyplot()

#Read the data 
import pandas as pd
csv_file=st.text_input( "enter csv file")
df=pd.read_csv(csv_file)
df


