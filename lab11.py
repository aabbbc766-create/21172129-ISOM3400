# Import
import streamlit as st
import pandas as pd

grading = {
    "Labs": 5,
    "In-class Exercises": 10,
    "Assignment": 15,
    "Midterm Exam": 20,
    "Final Exam": 50
}

# 1: SETUP
# Task 1.1: Give the page a title (and optionally an icon) using st.set_page_config().
st.set_page_config()

# Task 1.2: Display a title on the app using st.title(). 
#   You can also put more text/descriptions on the screen using st.write().
st.title()



# 2. INPUT FORM 
#   Create a form to group the input together.
#   You can choose to use the 'with' notation (given), or directly call methods onto the form object.

with st.form("Score form"):
    # Task 2: Ask for user input by creating number inputs/sliders. 
    #   Define min/max values to restrict user's input.
    #   Assign the values to the corresponding variables. (Please remove the "None" values!)
    #   

    labs_attended = None
    inclass_score = None
    asm_score = None
    midterm_score = None
    final_score = None
    
    # Don't forget the submit button! You can change the displayed text.
    click_submit = st.form_submit_button("Calculate my expected score!")

#3. Calculate scores
#   When the click_submit button is clicked, all obtained values will be sent to the Streamlit server.
#   We can tell that the button is clicked by checking if it is True. (True == clicked)
if click_submit:
#   Task 3.1: Process the obtained values and calculate the total (weighted) score!
#   (You can refer to the grading dictionary at the top for the weights.)









#   You should then display the calculated score on the web app (e.g. with st. write()/st.markdown()...).
#   If you like, you can also display the score breakdown using a DataFrame.

#   Task 3.2: Once the total score has been calculated, let the user know if they are likely to pass the course or not by writing another message.
#   Write an if/else case to show the message!
#   Note that we stay within the indented blcok under if click_submit.
#   We do not want anything to be displayed if the user has not submitted the form yet.
    
    pass #Placeholder. Please remove this pass statement when you finish Task 3.