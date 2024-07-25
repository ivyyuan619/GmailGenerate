import openai
import streamlit as st
import pandas as pd
from io import StringIO
import re

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# cloudword graph

from wordcloud import WordCloud
import matplotlib.pyplot as plt



#Function to get the response back

openai.api_key = "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"        # This is API key

def AIemail(question,max_tokens = 100):
    prompt = question
    model_engine = "gpt-3.5-turbo-0125"

    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].message.content
    return message

    # set the page
st.set_page_config(page_title="Generate Emails",
                    page_icon='📧',
                    layout='centered',
                    initial_sidebar_state='collapsed')


# selectbox in the middle
col1, col2, col3 = st.columns([1, 4, 1])  
with col1:
    pass
with col2:
    page = st.selectbox(
        'Tasks',
        [' ','Prompt', 'Optimizing Email by example'])
with col3:
    pass

st.session_state.setdefault('improvements', [])

if page == ' ':
    st.markdown("---") 
    st.write("### Guideline:") 
    st.write("- 'Prompt' is an instruction or command, typically used to request user input or perform a specific task.")
    st.write("- 'Optimizing Email using example' is an example demonstrating how to enhance the content or structure of an email.")

if page == 'Prompt':

    page2 = st.selectbox(
        'Sections',
        ['Retail', 'Resteraunt', 'Law Firm' , 'CPA Firm','Salons','AI','Others']                            
    )

    #1
    if page2 == 'Retail':
        
      st.header("Retail")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',('None','Discount', 'Free shipping', 'Free gifts', 'Product Recommendation'),index=0)
      with col4:
          number = st.text_input('Words',100)
      
      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: sales",int(number))
                    st.write(answer)
                    prompt = answer.strip('"')
                    less_formal_answer = AIemail(f"make it less formal:{prompt}", int(number))
                    st.markdown("---")
                    st.write(f"Less Formal version: \n{less_formal_answer}")
                  
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: sales",int(number))
                    st.write(answer)
                    


    # 2
    if page2 == 'Resteraunt':
        
      st.header("Resteraunt")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',
                                          ('None','Discount', 'new menu', 'Reservation Confirmation','Feedback Request','points redemption'),
                                            index=0)
      with col4:
          number = st.text_input('Words',100)

      if email_style == 'points redemption':
          st.image('p.jpg', caption='points redemption: Pokemon cards',width=200)

      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    st.write("Thanks for using")
                    st.write(AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: resteraunt",int(number)))
          else:
                    st.write("Thanks for using")
                    st.write(AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: resteraunt",int(number)))
    #3
    if page2 == 'Law Firm':
        
      st.header("Law Frim")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',
                                          ('None','Meeting confirmation' , 'court date reminder' , 'document request' , 'new client welcome' , 'event invitation'),
                                            index=0)
      with col4:
          number = st.text_input('Words',100)

      submit = st.button("Generate")


      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: law frim",int(number))
                    st.write(answer)
                    
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: law frim",int(number))
                    st.write(answer)


          
    # 4

    if page2 == 'CPA Firm':
        
      st.header("CPA Frim")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',('None','Market strategies'),index=0)
      with col4:
          number = st.text_input('Words',100)

      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: law frim",int(number))
                    st.write(answer)
                    
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: law frim",int(number))
                    st.write(answer)


    # 5

    if page2 == 'Salons':
        
      st.header("Salons")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',('None','Market strategies'),index=0)
      with col4:
          number = st.text_input('Words',100)

      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: law frim",int(number))
                    st.write(answer)
                    
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: law frim",int(number))
                    st.write(answer)

    # 6

    if page2 == 'AI':
        
      st.header("AI")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',('None','Market strategies'),index=0)
      with col4:
          number = st.text_input('Words',100)

      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: law frim",int(number))
                    st.write(answer)
                    
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: law frim",int(number))
                    st.write(answer)
    # 7

    if page2 == 'Others':
        
      st.header("Others")

      form_input = st.text_area('Enter the :blue[email] topic', height=205)


      #Creating columns for the UI - To receive inputs from user
      col1, col2, col3, col4 = st.columns([8, 8, 4, 4])
      with col1:
          email_sender = st.text_input('Sender Name')
      with col2:
          email_recipient = st.text_input('Recipient Name')
      with col3:
          email_style = st.selectbox('Incentive',('None','Market strategies'),index=0)
      with col4:
          number = st.text_input('Words',100)

      submit = st.button("Generate")

      #When 'Generate' button is clicked, execute the below code
      if submit:
          if email_style == 'None':
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} industry: law frim",int(number))
                    st.write(answer)
                    
          else:
                    answer = AIemail(f"write an email about {form_input} email_sender :{email_sender} email_recipient : {email_recipient} type:{email_style} industry: law frim",int(number))
                    st.write(answer)


#  New

if page == 'Optimizing Email by example':
    
  st.header(" Upload your own example ", divider = 'rainbow')                                      # https://docs.streamlit.io/develop/api-reference/text/st.markdown
  
  st.markdown(" Some Important Event Information includes ***Theme*** , ***Date & Time*** , ***Location*** , ***Requirements*** :balloon:") 
   
  form_input2 = st.text_area('Enter the :blue[example]', height=205)
  
 
  col1, col2, col3 , col4, col5  = st.columns([2,2,4,1,1])

  with col1:
      summary = st.button("1.Summary")
  with col2:
      cloudword = st.button("2.Word Cloud")
  with col3:
      score = st.button("***3. Testing Fuction: Score (0-5)***")
 
  st.markdown("---")

  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
      Generate = st.button("**I. Generate**")
  with col2:
      save = st.button("II. History")

  F2 = st.checkbox("Details")


# 1. summary
  if summary:
        data = {
        "Item": [],
        "Details": []
            }
        understanding = AIemail(f"To summarize the '1.Theme','2.Date & Time','3.Location','4.Requirements','5.Benefits' according {form_input2},End a section with a line wrap.")
        
        pattern_theme = r"1. Theme:\s*(.+)"
        pattern_datetime = r"2. Date & Time:\s*(.+)"
        pattern_location = r"3. Location:\s*(.+)"
        pattern_requirement = r"4. Requirements:\s*(.+)"
        pattern_benefits = r"5. Benefits:\s*(.+)"
        
        for line in understanding.splitlines():

            if re.match(pattern_theme, line):
                      data["Item"].append("Theme")
                      data["Details"].append(re.match(pattern_theme, line).group(1).strip())
            elif re.match(pattern_datetime, line):
                      data["Item"].append("Date & Time")
                      data["Details"].append(re.match(pattern_datetime, line).group(1).strip())
            elif re.match(pattern_location, line):
                      data["Item"].append("Location")
                      data["Details"].append(re.match(pattern_location, line).group(1).strip())
            elif re.match(pattern_requirement, line):
                      data["Item"].append("Requirements")
                      data["Details"].append(re.match(pattern_requirement, line).group(1).strip())
            elif re.match(pattern_benefits, line):
                      data["Item"].append("Benefits")
                      data["Details"].append(re.match(pattern_benefits, line).group(1).strip())

        # create the dataframe
        df = pd.DataFrame(data)

        st.dataframe(df)


# 3. Testing Function
  if score:
      data = {
      "Item": [],
      "Details": []
          }
      understanding = AIemail(f"To summarize the '1.Theme','2.Date & Time','3.Location','4.Requirements','5.Benefits' according {form_input2},End a section with a line wrap. After each part, indicate whether it is present, if yes say yes, if no say no ")
      
      pattern_theme = r"1. Theme:\s*(.+)"
      pattern_datetime = r"2. Date & Time:\s*(.+)"
      pattern_location = r"3. Location:\s*(.+)"
      pattern_requirement = r"4. Requirements:\s*(.+)"
      pattern_benefits = r"5. Benefits:\s*(.+)"
      
      for line in understanding.splitlines():

          if re.match(pattern_theme, line):
                    data["Item"].append("Theme")
                    data["Details"].append(re.match(pattern_theme, line).group(1).strip())
          elif re.match(pattern_datetime, line):
                    data["Item"].append("Date & Time")
                    data["Details"].append(re.match(pattern_datetime, line).group(1).strip())
          elif re.match(pattern_location, line):
                    data["Item"].append("Location")
                    data["Details"].append(re.match(pattern_location, line).group(1).strip())
          elif re.match(pattern_requirement, line):
                    data["Item"].append("Requirements")
                    data["Details"].append(re.match(pattern_requirement, line).group(1).strip())
          elif re.match(pattern_benefits, line):
                    data["Item"].append("Benefits")
                    data["Details"].append(re.match(pattern_benefits, line).group(1).strip())

      # create the dataframe
      df = pd.DataFrame(data)

      score = 0
      total_score = 5
      dic = {'Theme':0.8,'Date & Time':1,'Location':1,'Requirements':0.1,'Benefits':0.3}
      total = sum(dic.values())
      

      for item,value in dic.items():
           percentage = (value/total) * 100
           print(f"{item}:{percentage:.2f}%")

      for index,row in df.iterrows():
           item_value = row['Item']
           if item_value in dic and row['Details'] == 'Yes':
                 score = (dic[item_value] / total)*total_score + score
      
      st.write(f'Score={score:.2f}')

#  Generate & History

  if Generate:
      Improvement = AIemail(f"{form_input2} is example. There are two orders./Subtitle:write a  a really attractive and clear subtitle and line feed. Please keep the same information if example mentions Theme, Date, Location, Requirements and beneits.And the number of word doesn't exceed 10./ Email: write a improved version from example as a formal email.The word could not exceed 300 ",500)           
     
      st.session_state.improvements.append(Improvement)
      
      st.write(Improvement)
    
  if save:
      st.write(st.session_state.improvements)
  
  if F2:

      col1, col2, col3, col4, col5 = st.columns([4,4,4,4,4])
      with col1:
               Theme = st.text_input('Theme')
      with col2:
               Date = st.text_input('Date ')
      with col3:
               Location = st.text_input('Location')
      with col4:
               Requirement = st.text_input ('requirement')
      with col5:
               Benefit = st.text_input ('benefit')

      re = st.button('Improve')    
      if re:          
               answer = AIemail(f"please help me wrtie a similar email according {form_input},the Theme is {Theme}/ the Date is {Date}/the Location is {Location}/the requirement is {Requirement}/the benefit is {Benefit}",500)                                
               st.write(answer)





  # 2. Word Cloud

  if cloudword:
      wordcloud = WordCloud(width=800,height=400).generate(form_input2)
      
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis('off')
      st.pyplot(plt)


  #  attachment
  
  st.markdown("---")
  uploaded_files = st.file_uploader("Choose a txt or csv file", accept_multiple_files=True, type=['txt', 'csv'])
  for uploaded_file in uploaded_files:
      if uploaded_file is not None:
          file_extension = uploaded_file.name.split('.')[-1].lower()
          if file_extension == 'txt':
                    bytes_data = uploaded_file.read()
                    text_data = bytes_data.decode('gbk',errors = 'ignore')             
                    st.write("Filename:", uploaded_file.name)
                    st.write(bytes_data)
  
          elif file_extension == 'csv':  
                    df = pd.read_csv(uploaded_file)  # Read Excel file using Pandas
                    st.write("Filename:", uploaded_file.name)
                    st.write(df)
