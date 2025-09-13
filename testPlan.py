from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from selenium import webdriver
import os
from dotenv import load_dotenv
import time

#from Page_sourse import page_source, llm_suggestions

load_dotenv()  # טוען את הקובץ .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm =ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.1,
    max_tokens=500,
    api_key=OPENAI_API_KEY
)

#create function to anaylayz the page using selenium
# def analyz_html_with_llm(html:str)->str:
#     templete=f""" i want to give you a code html for page internet {html} identify the elements"""
#     prompt=ChatPromptTemplate.from_template(templete)
#     chain=prompt|llm
#     response=chain.invoke({'html',html})
#     return response.content
#
# def generate_selenium_script(actions:list)->str:
#
#     """get a llm and you can know selenium"""
#
#     template=f"""you are an expert in qa and generating script with 20 years experience,requerd to test a webpage with selenium return only a valid python script (no explenation and mark)use this url:"file:///C:/Users/Dell/Downloads/ActionChainsEx.Html"
#      locate elemants by their id ,class name or css selector ,etc...,and perform the following actions:{actions} the script must:
#      import selenium moudoles
#      open chrome using driver=webdriver.Chrome()
#      navigate to the url
#      locate the elements correctly
#      perform all the actions"""
#     prompt=ChatPromptTemplate.from_template(template)
#     chain=prompt|llm
#     response=chain.invoke({'html',actions})
#     return response.content


def process_target_data(target_url):
    """
    This function processes the target URL received from main.py.
    """
    print(f"The URL '{target_url}' has been received by the test.py file.")
    # Add your logic here, such as running a test or performing an action with the URL.
    driver = webdriver.Chrome()
    driver.get(target_url)
    driver.maximize_window()
    # driver.sleep(2)
    # page_source=driver.page_source
    driver.quit()

#producion script automation






