
#  Functions and Widgets in Streamlit
"""
        Basic Functions in Streamlit:
--> title
--> header
--> caption
--> code
--> latex
--> markdown
                            
        Input Widgets in Strealit
    Widgets are the user interface compents that allow us to add interactivity directly into the app.
--> checkbox()
--> button()
--> slider()
--> radio()
--> selectbox()
--> time_input()
--> date_input()
"""

import streamlit as st
import time as t;
import pandas as pd
import numpy as np


# st.spinner() works with time, 
# with st.spinner("Just wait"):
#         t.sleep(2)
       
# st.progress()
st.snow()

# st.image(image_file) : You can use to add add image to your app. 
# Doesn't change bacground color though
st.image("back.png")

# st.title(string_name): is use to add title to the web app
st.title('Welcome to this Example Streamlit App')

# st.header(string_name): is used to set the header of any section
st.header('This is a header')

# st.subheader(string_name)
st.subheader('This is a subheader')

# st.info("information to a user")
st.info("""This is st.info: 
        used to give information""")

# st.warning(warning_msg_String): used to display warning
st.warning("This is a warning message")

# st.write(some_string): is used to write text and codes on the web app.
# It is also used for displaying code
st.write("This is a simple text")
st.write("range(50)") # is a text
st.write(range(50)) # is a code
st.write(range(0,50,5))

# st.error(error_msgString): used to display error message
st.error("This is an error message: Wrong password")

# st.success(success_msgString): used to display a success message
st.success('This is a success message')

# st.markdown(string_msg): is used to set the markdown of a function.
st.markdown('# This is a markdown')
st.markdown('## This is a markdown')
st.markdown('### This is a markdown')
st.markdown('*This is an italicized markdown*')
st.markdown('**This is a bolded markdown**')
st.markdown("This is a markdown with :coffee: emoji.")
st.markdown(":moon:")

# st.text(some_string) : is reserved for texts
st.text("Nice to finally see actual text, yes?")

#st.caption(some_string): displays a caption text
st.caption("This is some caption text")

# st.latex(): To display a mathematical equation
st.latex(r'Equation: a + b x^3 = c')

"""
WIDGETS
"""
#st.checkbox(checkbox_msg, value=True):
#       value checks the checkbox by default
#       st.checkbox returns true when the box is checked.
checked = st.checkbox("Uncheck me", value=True)
if checked:
        st.write("st.checkbox when checked returns True.")
else:
        st.write("st.checkbox returns false when unchecked")

# st.button()
clicked = st.button('Click this button', type='primary')
if clicked:
        st.write('You clicked the button')
        reset = st.button('Click This to Reset', type='secondary')

#st.radio(): to create a radio widget  
st.radio("Pick your gender", ["Male", "Female", "Other"], index=None)

# st.selectbox(): is used to create a dropdown button
result = st.selectbox("Select a box from the dropdown", 
             ["ML", "Cloud", "AI"],
             index=None)
if result:
        st.write("You selected: ", result)

result = st.selectbox("Select a box from the dropdown", 
             ["R", "Python", "SASS"], index=1)

result = st.selectbox("Select a box from the dropdown", 
             ["R", "Python", "SASS"], 
             index=None, 
             placeholder="Select an option")
if result:
        st.write(f"You selected {result}")

# st.multiselect(string_msg, )
st.multiselect("Where would you like to work in Texas?",
               ['Houston', 'Dallas', 'San Antonio', 
                'Missouri City', 'Katy'],
               placeholder="Choose all that Apply")

# st.select_slider()
slider_options = ['Text Slider', 'Range Slider', 'Other']
text_slider = ["Excellent", "Very Good", "Medium", "Poor", "Very Poor"]
range_slider = range(1, 11, 1)

zipped_options = list(zip(slider_options, [text_slider, range_slider]))

slid = st.radio("How would you like to rate this project?: ",
          slider_options, index=None)
st.write("You chose: ", slid)

if slid is not None and slid != slider_options[2]:
        options = zipped_options[slider_options.index(slid)]
        st.select_slider("Feel free to move the slider: ",
                  options=options[1])
elif slid == slider_options[2]:
        # st.slider(msg, start_num, end_num, step-size)
        st.slider("Use the slider below if you would prefer a percentage range : ", 1, 100, 1)
           
# st.number_input():
st.number_input("Using the number input. Pick a number :smile: ", 0, 100)
   
# st.text_input()
st.text_input('Enter your email address: ')
st.text_input('Send me a message: ')

# st.date_input():
user_date = st.date_input('Text the date input. Pick a date:')
st.write("You chose: ", user_date)

#st.time_input()
st.time_input("Here's the time. Select any: ")

# st.text_area(): used to print multiline text
st.text_area("Paste a long text here: ")
        

#st.file_uploader() : used to 
st.file_uploader("Upload your file (up to 200MB): ")


# st.color_picker(msg, color)
st.color_picker("Select any color: ", value='#00ABAA')

# st.balloons()
# st.balloons()

# st.progress()
st.progress(50)


with st.sidebar:
        st.title("Example App Here!")
        st.text('This is the sidebar')
        st.button('Click me!')
        st.text_input('Enter your email: ')
        st.text_input('Create a password')
        st.button('Submit')
        st.radio("Are you a student?: ",
                 ["Yes", "No"])


# DATA VISUALIZATION:

# BAR CHART
st.title("A bar chart")
df = pd.DataFrame(np.random.randn(50,2), columns=["x", "y"])
st.bar_chart(df)

# LINE CHART
st.title("A line chart")
df = pd.DataFrame(np.random.randn(50,2), columns=["x", "y"])
st.line_chart(df)


# AREA CHART
st.title("A line chart")
df = pd.DataFrame(np.random.randn(50,2), columns=["x", "y"])
st.area_chart(df)
