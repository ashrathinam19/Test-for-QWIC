from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import logging
path ="C:\\Users\lkundurt\Desktop\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://localhost:3000/")
driver.maximize_window()


# Create and configure logger
logging.basicConfig(filename="QA.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
driver.find_element_by_name("T").send_keys("Testing")
# Function to test the alert box whether any values are empty or all the values has selected
def test_alerts_list(alert):
        #Get the text from alert box
        alerttext = alert.text
        alert_text = eval(alerttext)
        # Checks below condition, in case the brand and model values are empty
        if alert_text['model'] == "" and alert_text['brand'] == "":
                alert.accept()
                logger.warning("Warn: No Brand name and No Model name in the alert and text in alert:{0}".format(alert_text))
        # Checks below condition, in case only model values are empty
        elif alert_text['model'] == "":
                alert.accept()
                logger.warning("Warn: No Model name in the alert and text in the alert:{0}".format(alert_text))
        # Checks below condition, in case only brand values are empty
        elif alert_text['brand'] == "":
                alert.accept()
                logger.warning("Warn: No Brand name in the alert and text in alert: {0}".format(alert_text))
        # Checks below condition, in case all the input values are selected and are not empty
        else:
                alert.accept()
                print (alert_text)
                logger.warning("Info: Text in alert:{0} ".format(alert_text))


#Function to enter the keyword text value
def keyword_text():
        # Send the test string to Keyword input text field
        driver.find_element_by_name("T").send_keys("Testing")


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
        obj.select_by_value(models)


# Function to click on Search Cars button
def test_click_on_search_cars():
        driver.find_element_by_id("B").click()

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
                        logger.warning("Warn: No Brand name listed")
                    # Assign all the model names to model_names list
                    model_names=get_models_list_by_each_brand()
                    #Loop through all the model names for each brand
                    for models in model_names:
                            # Check the condition if the model name is not empty, then select the model name
                            if not models == '':
                                    select_the_model_name(models)
                                    test_click_on_search_cars()
                                    alert = driver.switch_to.alert
                                    if alert:
                                            test_alerts_list(alert)
                                    else:
                                        logger.warning("Warn: No Alert window popup")
                            else:
                                    logger.info("Warn: No Model name listed")
                                    test_click_on_search_cars()
                                    alert = driver.switch_to.alert
                                    if alert:
                                            test_alerts_list(alert)
                                    else:
                                            logger.warning("Warn: No Alert window popup")


if __name__ == '__main__':
        test_main()