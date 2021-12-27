''' Program to Deploy ML model using streamlit'''

# MODULES
import streamlit as st 
import pandas as pd
import pickle

## PROGRAM VARIABLES

proj_desc =  '''
    Hey Guys!!!🙋‍♂️ Welcome to my Website 🙌🎆😎. \n 
    This website is used to predict the price💲of used cars 🚗 based on 5 specific features of the car.\n
    This website estimates the price💲 of any car🚙 based on Machine Learning Approach. In the Machine Learning approach, we provide the Machine
    learning algorithm with some data. Then the algorithm creates a Machine Learning model which estimates the selling price of used cars
    based on 5 specific features of the car. The input to the machine learning model would be given by the end user or the 
    client.\n
    The data is collected from kaggle, which was collected by a kaggle user from \'Car Dekho.com\' .\n
    \'CarDekho.com\' is India's leading car search venture that helps users buy cars that are right for them. It's website and app carry rich automotive
    content such as expert reviews, detailed specs & prices, comparisions as well as videos & pictures of all car brands & models available in india.\n
    In the \'Home page\', you would get a brief description about \'CarDekho.com\' and my project. In the \'EDA page\', you would be able to see graphical
    representation of my project data. In the \'Predict Price\' page, you would be able to estimate price of the used car based on 5 specific features of the car.
    '''

sell_image = r'predict_page_img3.jpg'

marketing_image = r'Akshay-Kumar-CarDekho.png'        

logo = r'eda.jpg'

predict_header = 'Predict Selling Price💲 of your car🚗'

website_title = 'Price💲 Prediction of Used Cars🚗🏎️🚙'

with open(r'model.pkl','rb') as model_file:

    model = pickle.load(model_file)

menu_name = "Navigation"

menu_items = ['Home','EDA','Predict Price']

def homePage() :
        
    ''' FUNCTION TO CREATE HOME PAGE'''
    
    # WEB-PAGE TITLE
    st.title(website_title)
    
    # DISPLAYING TEXT
    #st.markdown('** Home Page **')
    
    # DISPLAYING IMAGE
    st.image(marketing_image)
    
    # DISPLAYING SOME TEXT
    st.write(proj_desc)
        
def edaPage() :
        
    ''' FUNCTION TO CREATE EDA PAGE'''    
        
    # DISPLAYING TEXT
    st.header('** Exploratory Data Analysis **')
    
    # DISPLAYING IMAGE
    st.image(logo,width=700) 

       
def predictPage() :
    
    ''' FUNCTION TO CREATE PRICE PREDICTION PAGE'''
    
    # PAGE HEADER
    st.header(predict_header)
    
    # DISPLAYING IMAGE
    st.image(sell_image,width=700)
    
    ## INPUTS FOR OUR MODEL
    inp1 = st.number_input('Enter the total distance travelled with you vehicle : ',min_value=0,max_value=4000000)
    
    inp2 = st.number_input('Enter the engine power of your vehicle in terms of cc : ',min_value=0,max_value=7000)
    
    inp3 = st.number_input('Enter the max power your car can reach : ',min_value=0,max_value=650)
    
    inp4 = st.number_input('Since how many years are you driving your vehicle : ',min_value=0)
    
    inp5 = st.number_input('Enter the mileage of your car : ',min_value=0,max_value=50)
    
    # SUBMIT BUTTON
    submit = st.button('Submit details')
    
    data = [inp1,inp2,inp3,inp4,inp5]
    
    df =  pd.DataFrame(columns=['km_driven','engine','max_power','vehicle_age','mileage'])
    
    df.loc[0] = data 
    
    sell_price = model.predict(df)[0]
    
    if submit :
            
        if all(data) == 0 :
        
            st.warning('Please enter any value. Do not leave the fields empty')

        else :
                
            # DISPLAY OUTPUT
            st.success('The estimated selling price for your car is  :  {0} {1}'.format(round(sell_price,4),'\u20B9'))

def main() :
    
    global  menu_items , menu_items

    # NAVIGATION BAR
    navigation_bar = st.sidebar.radio(menu_name,menu_items)

    # IF 'Home' IS SELECTED IN NAVIGATION BAR
    if navigation_bar == 'Home':
    
        # CALLING 'homePage()' from 'webpages' module
        homePage()
    
    # IF 'EDA' IS SELECTED IN NAVIGATION BAR    
    if navigation_bar == 'EDA':
    
        # CALLING 'edaPage()' from 'webpages' module
        edaPage()
    
    # IF 'Price Predict' IS SELECTED IN NAVIGATION BAR    
    if navigation_bar == 'Predict Price':
    
        predictPage()

if __name__ == '__main__' :
  
    print(st.__version__)
    
    print(pd.__version__)
  
    main()        