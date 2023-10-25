import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rpadb import Mysqldb
from rpainst import DATABASE_CONFIG

# Create a database connection instance
dbconn = Mysqldb()
dbconn.connectdb()


def login_to_naukri():
    # Set the path to the Chrome WebDriver executable
    chrome_driver_path = "C:\\Users\\Aravind\\OneDrive - AM ESI LLP\\Downloads\\chromedriver-win32\\chromedriver.exe"

    # Create Chrome WebDriver options and set the executable path
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--webdriver-path={chrome_driver_path}')
    chrome_options.add_argument("--start-maximized")

    # Create a Chrome WebDriver instance with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com/')

    # sending first response
    message = "process started"
    # status(message)

    # open the URL
    driver.get("https://www.naukri.com/recruit/login")
    timeDelay = random.randrange(2, 8)
    time.sleep(timeDelay)

    # Click on the login
    driver.find_element(
        by=By.XPATH, value="//*[@id='toggleForm']/li[2]").click()

    # Input username
    driver.find_element(by=By.XPATH, value='//*[@id="login-form-revamp"]/div[1]/div/div[1]/input').send_keys(
        "")
    time.sleep(timeDelay)

    # Input password
    driver.find_element(by=By.XPATH, value='//*[@id="login-form-revamp"]/div[2]/div/div[1]/input').send_keys(
        "")
    time.sleep(timeDelay)

    # Clicking on submit
    driver.find_element(
        by=By.XPATH, value='//*[@id="login-form-revamp"]/div[4]/button').submit()
    time.sleep(20)

    return driver


def page2_actions(driver):
    time.sleep(10)

    try:
        driver.find_element(
            by=By.XPATH, value="//*[@id='modalRoot']/div/div/a/div").click()
    except:
        pass

    timeDelay = random.randrange(1, 7)
    time.sleep(timeDelay)

    actions = ActionChains(driver)

    resdex = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[1]")
    search = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/a[1]")

    actions.move_to_element(resdex).move_to_element(search).click().perform()

    time.sleep(4)

    if driver.title == 'Resdex Change Login':
        driver.find_element(by=By.CLASS_NAME, value="tabUnsel").click()
        timeDelay = random.randrange(1, 10)
        time.sleep(timeDelay)
        driver.find_element(
            by=By.XPATH, value="//*[@id='resetLoginRadioBtn']").click()


def page3_actions(driver):
    global keywords
    exclusion = "Tester"
    key_mainskills = "Python"
    min_experience = "2"
    max_experience = "5"
    key_skills = "Python"
    prefloc = "Chennai"
    location = "Mumbai"
    noticeperiod = "15 Days"
    positiontype = "Full Time"
    minlac = "1"
    maxlac = "5"

    # entering search parameters for candidates
    message = "entering search parameters for candidates"
    # status(message)
    # RPA_status(message)
    time.sleep(3)
    # try:
    #     # def utilize():
    #     #     # Add the functionality you want to perform within the "utilize" function here.
    #     #     print("Inside the 'utilize' function")

    #     # utilize()
    #     time.sleep(2)
    # except:
    #     pass
    try:
        driver.find_element(
            by=By.XPATH, value='//*[@id="modalRoot"]/div/div/button').click()
        time.sleep(2)
    except:
        pass
    #
    # driver.find_element(by=By.XPATH, value="//*[@id='quotaltCover']/button").click()
    # time.sleep(2)
    print("value of exclusion", exclusion)
    if exclusion is not None:
        print("exclusion")
    # Exclusion
        wait = WebDriverWait(driver, 10)
        button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-field-link[name='add-exclude-keywords']")))
    # Click on the button
        button.click()
        time.sleep(3)

        exclude_input = driver.find_element(by=By.XPATH,
                                            value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div/input')

        print("into exclusion")
        for key in exclusion.split(", "):
            exclude_input.send_keys(str(key) + ", ")
            time.sleep(3)
        timeDelay = random.randrange(1, 8)
        time.sleep(timeDelay)
    else:
        pass
    time.sleep(2)

    # must have skills

    # main_skills = driver.find_element(by=By.XPATH,value='//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/form/div[1]/div/div[1]/div[2]/div/div/div[1]/div/input')
    # if key_mainskills is not None:
    #     for key in key_mainskills.split(", "):
    #         main_skills.send_keys(str(key) + ", ")
    #         time.sleep(3)
    # timeDelay = random.randrange(1, 8)
    # time.sleep(timeDelay)

    main_skills = driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/input')
    if key_mainskills is not None:
        for key in key_mainskills.split(", "):
            if len(key.split()) >= 2:
                print("inside mainskills", main_skills)
                print('Sending keys: "' + str(key) + '", ')
                main_skills.send_keys('"' + str(key) + '", ')
            else:
                main_skills.send_keys(str(key) + ', ')

            time.sleep(3)
    timeDelay = random.randrange(1, 8)
    time.sleep(timeDelay)

    # must have click
    must_skill = key_mainskills.split(',')

    for i in range(len(must_skill)):
        if i == 0:
            continue
        else:
            xpath = '//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[{}]/span/div/span/i'
            musthave_button = driver.find_element(
                by=By.XPATH, value=xpath.format(i + 1))
            print("value of i", i)
            musthave_button.click()

    # inputing minimum and maximum experience

    driver.find_element(by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[4]/div[1]/div[1]/div/div[1]/div/input').send_keys(
        min_experience)

    timeDelay = random.randrange(1, 5)
    time.sleep(timeDelay)
    driver.find_element(by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[4]/div[1]/div[2]/div/div[1]/div/input').send_keys(
        max_experience)

    timeDelay = random.randrange(1, 5)
    time.sleep(timeDelay)
    time.sleep(2)

    # inputting keywords
    keyword = driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div/input')
    if key_skills is not None:
        print("keyskills value", key_skills)
        for key in key_skills.split(", "):
            keyword.send_keys(str(key) + ", ")
            time.sleep(1)
    else:
        pass
    timeDelay = random.randrange(1, 8)
    time.sleep(timeDelay)

    Preferlocation = driver.find_element(
        by=By.CLASS_NAME, value='pref-loc-checkbox')
    # hidden_submenu = driver.find_element_by_selector("#prefLocCheckbox > i")

    if prefloc != "1":

        driver.execute_script("arguments[0].scrollIntoView();", Preferlocation)
        ActionChains(driver).move_to_element(Preferlocation).click().perform()
    else:
        pass
    # setting current location

    bl = driver.find_element(
        by=By.CSS_SELECTOR, value=".focus-observer .suggestor-input")
    time.sleep(3)

    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", bl)
    # actions.moveToElement(bl).click().perform();
    ActionChains(driver).move_to_element(bl).click().perform()

    time.sleep(3)
    # bl.click();
    print('location', location)
    if (location == 'Anywhere In India'):
        loc = driver.find_element(
            by=By.XPATH, value="//span[normalize-space()='Anywhere in India']")
        time.sleep(2)
        print(loc)
        # ActionChains(driver).move_to_element(loc).click().perform()
        loc.click()
        time.sleep(2)

    else:
        bl.send_keys(location)
        time.sleep(4)
        try:
            le = driver.find_element(
                by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div[2]/div[5]/div/div/div[1]/div[2]/div/div[2]/div[1]/ul/li[1]/div')
            time.sleep(2)
            le.click()
            time.sleep(2)
        except:

            le = driver.find_element(
                by=By.XPATH, value='//form[contains(@name,"v3-adv")]//li[1]//div[1]')
            time.sleep(2)
            le.click()
            time.sleep(2)

    timeDelay = random.randrange(1, 5)
    time.sleep(timeDelay)
    time.sleep(2)

    time.sleep(2)
    # Salary

    driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[6]/div/div[2]/div/div[1]/div/input').send_keys(minlac)
    timeDelay = random.randrange(1, 5)
    time.sleep(timeDelay)
    driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[6]/div/div[3]/div/div[1]/div/input').send_keys(maxlac)
    timeDelay = random.randrange(1, 5)
    time.sleep(timeDelay)
    time.sleep(5)

    # expand empdetails
    print("till here")
    expandempdetail = driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[1]/div/span')

    # expandempdetail.click()

    driver.execute_script("arguments[0].click();", expandempdetail)
    timeDelay: int = random.randrange(1, 7)
    time.sleep(timeDelay)

    if noticeperiod is not None:

        noticep = driver.find_element(
            by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]')
        driver.execute_script("arguments[0].scrollIntoView();", noticep)

        try:

            if noticeperiod == "15 Days":

                noticeA = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[2]/span')
                noticeA.click()
                time.sleep(3)

            elif noticeperiod == "1 month":

                noticeb = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[3]/span')
                noticeb.click()
                time.sleep(3)

            elif noticeperiod == "2 months":

                noticec = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[4]/span')
                noticec.click()
                time.sleep(3)

            elif noticeperiod == "3 months":

                noticed = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[5]/span')
                noticed.click()
                time.sleep(3)

            elif noticeperiod == "more than 3 months":

                noticed = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[6]/span')
                noticed.click()
                time.sleep(3)

            elif noticeperiod == "Currently Serving Noticeperiod":

                noticed = driver.find_element(
                    by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[7]/span')
                noticed.click()
                time.sleep(3)

        except:
            # any

            noticee = driver.find_element(
                by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div/div[1]/span')
            noticee.click()
            time.sleep(3)

    timeDelay: int = random.randrange(1, 7)
    time.sleep(timeDelay)

    # expand display details

    expanddispdetail = driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[1]/div/div[9]/div/div/div[1]/div/span')
    # expanddispdetail.click()
    driver.execute_script("arguments[0].click();", expanddispdetail)
    timeDelay: int = random.randrange(1, 7)
    time.sleep(timeDelay)

    if positiontype is not None:

        # expanddispdetail = driver.find_element_by_xpath("//*[@id='searchAccordion']/a[4]/span")
        # expanddispdetail.click()

        positiontypep = driver.find_element(by=By.XPATH, value='//*[@id="jt"]')
        driver.execute_script("arguments[0].scrollIntoView();", positiontypep)
        timeDelay: int = random.randrange(1, 7)
        time.sleep(timeDelay)

        # entering position type
        positiontypep.send_keys(positiontype)
        ksc = []
        # if entered position type  is in above list(k)
        try:
            if positiontype in ksc:
                # clicking on below xpath
                sc = driver.find_element(
                    by=By.XPATH, value='//*[@id="sa-dd-scrolljt"]/div[1]/ul/li[1]')
                time.sleep(2)
                sc.click()
            else:
                # clicking on below xpath
                sc = driver.find_element(
                    by=By.XPATH, value='//*[@id="sa-dd-scrolljt"]/div[1]/ul/li[2]')
                time.sleep(2)
                sc.click()
        except:
            positiontypep.send_keys('any')
            sc = driver.find_element(
                by=By.XPATH, value='//*[@id="sa-dd-scrolljt"]/div[1]/ul/li[3]')
            time.sleep(2)
            sc.click()

    plus = driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div/div[3]/div/form/div[2]')
    print("submit button")
    # scrolling to submit button
    driver.execute_script("arguments[0].scrollIntoView();", plus)
    timeDelay = random.randrange(1, 7)
    time.sleep(timeDelay)

    # clicking on submit button
    driver.find_element(
        by=By.XPATH, value='//*[@id="adv-search-btn"]').submit()
    print("clicked on submit")
    time.sleep(8)


def page_resumes(driver):
    # err
    key_skills = "Python"
    # result_return
    count = 2
    # resume_no
    pg_no = 1
    # ttl_resume
    # first
    # vary
    l = list()
    # flag
    # industrydomain = "IT"
    key_mainskills = "Python"
    # length_resumes = 0

    # To check that current resume from where relevance is checked on resumed page starts at right number
    # vary = pg_no + 1

    # clicking on next page if number of resumes are greater than 40
    while pg_no > 0:

        # element = driver.find_elements_by_class_name("tupData")[0]
        # driver.find_elements(by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div[3]/div/div[2]/div/div[3]/div[{}]')[0]
        # element = driver.find_elements(
        #     By.CLASS_NAME, "candidate-highlights")[0]

        # print("check element", element)

        # el = driver.find_element(by=By.XPATH,
        #                          value='//*[@id="rdxRoot"]/div/div[1]/div[3]/div/div[2]/div/div[3]/div[{}]/div[1]/div/div[1]/div/div/div[1]/span'.format(1))

        parent_han = driver.current_window_handle

        # # clicking the profile which opens new window
        # timeDelay = random.randrange(1, 10)
        # time.sleep(timeDelay)
        # el.click()
        time.sleep(7)
        all_han = driver.window_handles

        # getting child window handle
        # new_han = [x for x in all_han if x != parent_han][0]
        new_han = [x for x in all_han if x != parent_han][0]
        # print(new_han)
        # giving control to child window
        driver.switch_to.window(new_han)
        try:
            # calling reset function to check if reset subuser window appears or not
            # reset()
            time.sleep(2)
        except:
            pass
        try:
            # robot()
            time.sleep(2)
        except:
            pass

        timeDelay = random.randrange(1, 12)
        time.sleep(timeDelay)
        driver.close()
        driver.switch_to.window(parent_han)
        try:
            # calling reset function to check if reset subuser window appears or not
            # reset()
            time.sleep(4)
        except:
            pass
        try:
            # robot()
            time.sleep(2)
        except:
            pass

        timeDelay = random.randrange(1, 5)
        time.sleep(timeDelay)

        # scrolling to end of page
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(10)

        # clicking on next page
        # timeDelay = random.randrange(1, 12)
        # time.sleep(timeDelay)
        #
        # driver.find_element(by=By.XPATH,
        #                     value='//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[5]/div/div/div[2]/button[3]/i').click()
        pageveiw = driver.find_element(by=By.XPATH,
                                       value='//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[5]')
        driver.execute_script("arguments[0].scrollIntoView();", pageveiw)
        print("pageveiw")
        timeDelay = random.randrange(4, 8)
        time.sleep(timeDelay)
        driver.find_element(
            by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[5]/div/div/div[2]/button[3]/i').click()
        try:
            # calling reset function to check if reset subuser window appears or not
            # reset()
            time.sleep(2)
        except:
            pass
        try:
            # robot()
            time.sleep(2)
        except:
            pass

        time.sleep(2)
        pg_no = pg_no - 1
        time.sleep(2)

    # page down and up
    print("line 1143")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)

    driver.find_element(
        by=By.XPATH, value='//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[4]').click()
    time.sleep(3)
    # length of all profiles in the page
    length = len(driver.find_elements(By.CLASS_NAME, "candidate-highlights"))
    driver.implicitly_wait(10)

    k = 0

    for i in range(k, length):

        timeDelay = random.randrange(1, 5)
        time.sleep(timeDelay)
        if count > 0:
            time.sleep(2)

            # element is each profile in page
            element = driver.find_elements(
                By.CLASS_NAME, "candidate-details")[i]
            # element = driver.find_element(by=By.XPATH, value='//*[contains(@class, "tuple-list")]/div[{}]'.format(i+1))
            time.sleep(2)

            # storing all the text of the profile in str variable
            str = element.text

            # predicting the probability of the profile if val>0.70 it is selected
            timeDelay = random.randrange(1, 5)
            time.sleep(timeDelay)
            # if ttl_resume > 20 and length_resumes < 1:
            #     # return_data = {"key": keys, "status": "Failed",
            #     #                "data": "No Resumes found, Please change search criteria"}
            #     # dumping result_return in pred as json object
            #     # pred = json.dumps(return_data)
            #     # print(pred)
            #     # break
            #     driver.close()
            # Check domain relevancy by Ashu
            # domain_chk = relevant(str, industrydomain)
            domain_chk = 0.40
            ttl_resume = ttl_resume + 1
            if domain_chk > 0.20:
                # All_skills = key_skills + ", " + key_mainskills
                All_skills = key_mainskills + ", " + key_skills

                print("key_skills", key_skills)
                print("key_mainskills", key_mainskills)

                print("all_skill:", All_skills)
                # All_skills = key_skills

                try:
                    # Connect to the MySQL database
                    # db_instance.connectdb()
                    # if not db_instance.mcnx:
                    #     return  # Return or handle appropriately if the database connection fails

                    # Define XPaths as variables for code readability
                    mobile_button_xpath = '//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/button'
                    contact_xpath = '//*[@id="rdxRoot"]/div/div[1]/div/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/button/div[1]'

                    while True:
                        try:
                            # Extract mobile number
                            mobile = driver.find_element(
                                by=By.XPATH, value=mobile_button_xpath)
                            mobile.click()
                            time.sleep(2)
                            contact = driver.find_element(
                                by=By.XPATH, value=contact_xpath).text
                            extracted_mobile = contact.split("(")[0]

                            if dbconn.check_mobnum_in_database(extracted_mobile):
                                print(
                                    f"Candidate's mobile number {extracted_mobile} matches with the database. Leaving the candidate.")
                            else:
                                print(
                                    f"Candidate with mobile {extracted_mobile} not found in the database. Proceeding with other actions.")

                                val = extract_candidates(driver)
                                print("relevant: val", val)

                            # Scroll to the next candidate's mobile button
                            mobile_button = driver.find_element(
                                by=By.XPATH, value=mobile_button_xpath)
                            driver.execute_script(
                                "arguments[0].scrollIntoView(true);", mobile_button)

                        except Exception as e:
                            print("Error occurred:", e)
                            # Handle the error, e.g., move to the next candidate

                except:
                    pass


def extract_candidates(driver):
    try:
        # Your candidate extraction code here, using the driver passed as an argument
        # ...
        pass

    except Exception as e:
        print("Error occurred:", e)
    finally:
        # Ensure you properly close the web driver when you're done
        driver.quit()


# Main script
if __name__ == "__main__":
    # Call the login function to log in to Naukri Recruit
    driver = login_to_naukri()

    # Perform the actions in page2
    page2_actions(driver)

    # Perform the actions from page3
    page3_actions(driver)

    # Perform the actions from page_resume
    page_resumes(driver)

    # Extract candidates
    extract_candidates(driver)
