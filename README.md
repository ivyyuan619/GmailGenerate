# GmailGenerate

This project is a Streamlit web application that uses OpenAI's GPT-3.5-turbo model to generate email content based on user input.

## Features
1. Generate professional emails using AI.
2. Simple and interactive web interface built with Streamlit.
3. Visualization of word clouds based on generated email content.

## Installation
### Prerequisites

- Python 3.7 or higher
- Pip package manager
  
### Step
1. **Clone the repository:**

   ```sh
   git clone https://github.com/ivyyuan619/GmailGenerate.git
   cd completed_code_7_24.py

2. **Install the required packages:**
   ```sh
   pip install -r requirements.txt

3. **If requirements.txt is not available, you can install the dependencies manually:**
   ```sh
   pip install openai streamlit pandas wordcloud matplotlib langchain langchain_community

4. **Set up the OpenAI API key:**
   ```sh
   Replace "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" with your actual OpenAI API key in the script.

### Usage
1. **Navigate to the project directory:**
   ```sh
   cd completed_code_7_24.py
2. **Run the Streamlit application:**
   ```sh
   streamlit run completed_code_7_24.py
3. **Access the web application:**
   ```sh
   Open your web browser and go to http://localhost:8501.
   

## Homepage
On the homepage, you can choose two services: using the prompt to generate the email or using data of email to get the analysis and improve the quality (Optimizing Email by example)

### Prompt: 
There are six industries you can choose. Every session, we trained the model to be more professional in special industry

### Optimizing Email by Example: 
I. **Analytical tools:** 
   1. Summary: Help you check the structure of the email
   2. Wordcloud: Help you find the keyword
   3. Scoring: Help you score the quality of your email

II. **Click the "Generate " button and view the generated email content. You can also use the history function to see the previous answer**

III. **Use the attachment to upload your file. But now there is no further usage of this function**

### Roadmap:

The following features are on our roadmap:

- Feature 1 Add more standards to improve the stability and accuracy of scoring
- Feature 2 Add the new function to count the similarity of input and output
- Feature 3 Expand the Excel tool to categorize data into various major categories, providing a more structured analysis.

## Contact
- If you have any questions or suggestions, feel free to contact me.
- Email: bu.ju@northeastern.edu OR ivyyuan.zhou@gmail.com
- GitHub: ivyyuan619



