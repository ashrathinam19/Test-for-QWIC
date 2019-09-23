from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import logging
import time
from selenium.common.exceptions import NoSuchElementException
path ="C:\\Users\lkundurt\Desktop\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://localhost:3000/")
driver.maximize_window()


# Create and configure logger
logging.basicConfig(filename='QA.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
logger=logging.getLogger()

# Function to get the alert text
def test_alerts_list(alert):
        #Get the text from alert box
        alerttext = alert.text
        alert_text = eval(alerttext)
        alert_text_validation(alert,alert_text)
        # Checks below condition, in case the brand and model values are empty

# Function to validate the alert text whether any values are empty or all the values has selected
def alert_text_validation(alert,alert_text):
    if alert_text['model'] == "" and alert_text['brand'] == "":
        alert.accept()
        logger.info("Warn: Fail: None of the Brand, Model, and Keyword names in the alert and text in alert:{0}".format(
            alert_text))
    # Checks below condition, in case only model values are empty
    elif alert_text['model'] == "" and alert_text['keyword'] == "":
        alert.accept()
        logger.info("Warn: Fail: Only Brand name in the alert and text in the alert:{0}".format(alert_text))
    # Checks below condition, in case only brand values are empty
    elif alert_text['brand'] == "" and alert_text['keyword'] == "":
        alert.accept()
        logger.info("Warn: Fail: Only Model name in the alert and text in alert: {0}".format(alert_text))
    # Checks below condition, in case all the input values are selected and are not empty
    else:
        alert.accept()
        logger.info("Info: Pass: Text in alert:{0} ".format(alert_text))

## Function to get the alert text without a keyword
def test_alerts_no_keyword(alert):
    alerttext = alert.text
    alert_text = eval(alerttext)
    alert_text['keyword'] = ""
    alert_text_validation(alert, alert_text)


keywords=['', 'Testing']
#Function to enter the keyword text value
def keyword_text(keywords):
        # Send the test string to Keyword input text field
        for keyword in keywords:
            key_word = driver.find_element_by_name("T")
            if keyword =='':
                            key_word.clear()
                            key_word.send_keys("")
                            key_word.clear()
                            test_click_on_search_cars_no_keyword()
            else:
                            key_word.send_keys(keyword)
                            test_click_on_search_cars()



# Function to get all the Brand names from the drop down options list
def  get_brands_list():

        # Find brand Selectbox field
        b1= driver.find_element_by_name("S1")
        # Get all the Brand element names from the drop down options list
        b_options= [y for y in b1.find_elements_by_tag_name("option")]
        brands = []
        for bnames in b_options:
                # Get the Brand value/name from the Brand elements and append them to the list
                brands.append(bnames.get_attribute("value"))
        return brands


# Function to get all the Model names for each brand from the drop down options list
def get_models_list_by_each_brand():
        # Find model Selectbox field
        m1 = driver.find_element_by_name("S2")
        # Get all the Model element names from the drop down options list for each brand
        m_options = [x for x in m1.find_elements_by_tag_name("option")]
        models = []
        for mnames in m_options:
                # Get the Model value/name from the Model elements and append them to the list
                models.append(mnames.get_attribute("value"))
        return models


# Function to select the Brand names
def select_the_brand_name(brands):
        obj = Select(driver.find_element_by_name("S1"))
        obj.select_by_value(brands)


# function to select the Model names for each Brand
def select_the_model_name(models):
        obj = Select(driver.find_element_by_name("S2"))
        return obj.select_by_value(models)


# Function to click on Search Cars button
def test_click_on_search_cars():
            if driver.find_element_by_id("B").is_enabled():
                driver.find_element_by_id("B").click()
                alert_details()
            else:
                print (" no search")
                logger.info("Warn: Search cars button is not enabled")

# Function to click on Search Cars button without a keyword
def test_click_on_search_cars_no_keyword():
    if driver.find_element_by_id("B").is_enabled():
        driver.find_element_by_id("B").click()
        alert_details_no_keyword()
    else:
        print(" no search")
        logger.info("Warn: Search cars button is not enabled")

def alert_details_no_keyword():
        alert = driver.switch_to.alert
        if alert:
            test_alerts_no_keyword(alert)
        else:
            logger.info("Warn: Fail: No Alert window popup")



def alert_details():
         alert = driver.switch_to.alert
         if alert:
            test_alerts_list(alert)
         else:
            logger.info("Warn: Fail: No Alert window popup")

#Main function
def test_main():
        # Assign all the Brand names to brand_names list
        brand_names= get_brands_list()
        # Loop through all the brand names
        for brands in brand_names:
                    # Check the condition if the brand name is not empty, then select the brand name
                    if not brands == '':
                        select_the_brand_name(brands)
                    # if the brand name is empty
                    else:
                        logger.info("Warn: Fail: No Brand name listed")
                    # Assign all the model names to model_names list
                    model_names=get_models_list_by_each_brand()
                    #Loop through all the model names for each brand
                    for models in model_names:
                            # Check the condition if the model name is not empty, then select the model name
                            if not models == '':
                                    select_the_model_name(models)
                                    keyword_text(keywords)
                            else:
                                    logger.info("Warn: Fail: No Model name listed")
                                    keyword_text(keywords)



if __name__ == '__main__':
        test_main()
