
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def casesA(lat, lng, button, driver, latInput, lngInput, errorExp, resultExp, n):
    lat.send_keys(latInput)
    lng.send_keys(lngInput)
    button.click()
    time.sleep(3)

    error = driver.find_element(By.ID, "error")
    result = driver.find_element(By.ID, "country")

    if error.text == errorExp and result.text == resultExp:
        print("\tPassed case", n)
    else:
        print("\tFailed case", n)

    lat.clear()
    lng.clear()


def caseA():
    print("Test Case for A - Beginning")

    driver = webdriver.Chrome()
    driver.get("https://selcenkaya.github.io/proj3")
    driver.maximize_window()
    time.sleep(3)

    lat = driver.find_element(By.ID, "lat")
    lng = driver.find_element(By.ID, "lng")
    button = driver.find_element(By.ID, "getLatLng")

    # Valid - Invalid based on:
    # -90 <= lat <= 90
    # -180 <= lng <= 180

    # 1 - Empty input fields (both) - Expect error message and no country shown
    casesA(lat, lng, button, driver, "", "", "Please enter valid coordinates.", "-", 1)

    # 2 - One input field valid, other empty - Expect error message and no country shown
    casesA(lat, lng, button, driver, 90, "", "Please enter valid coordinates.", "-", 2)

    # 3 - One input field invalid, other empty - Expect error message and no country shown
    casesA(lat, lng, button, driver, 100, "", "Please enter valid coordinates.", "-", 3)

    # 4 - Invalid inputs (both) - Expect error message and no country shown
    casesA(lat, lng, button, driver, -100, 200, "Please enter valid coordinates.", "-", 4)

    # 5 - One field invalid, other valid - Expect error message and no country shown
    casesA(lat, lng, button, driver, 90, 200, "Please enter valid coordinates.", "-", 5)

    # 6 - Valid inputs (both) - Checks the output's correctness (country)
    casesA(lat, lng, button, driver, 40, 32, "", "Turkey", 6)
    casesA(lat, lng, button, driver, 50, 10, "", "Germany", 7)
    casesA(lat, lng, button, driver, 40, 0, "", "Spain", 8)
    casesA(lat, lng, button, driver, -90, 180, "", "Antarctica", 9)
    casesA(lat, lng, button, driver, 70, 0, "", "No Country", 10)  # The sea - No country expected

    driver.close()
    print("Test Case for A - End\n")


def caseBDriver(allow):
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.geolocation": allow}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://selcenkaya.github.io/proj3")
    driver.maximize_window()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    return driver


def caseB():
    print("Test Case for B - Beginning")

    i = 1
    while i <= 2:
        driver = caseBDriver(i)
        button = driver.find_element(By.ID, "getNorth")
        button.click()
        time.sleep(3)

        error = driver.find_element(By.ID, "error2")
        result = driver.find_element(By.ID, "dist")

        if i == 1:
            num = re.findall(r"\d+\.\d+", result.text)
            if error.text == "" and 5570 <= float(num[0]) <= 5572:     # change this value for your location
                print("\tPassed case", i)
            else:
                print("\tFailed case", i)

        else: # i = 2
            if error.text == "Permission was denied." and result.text == "Distance to the North Pole: -":
                print("\tPassed case", i)
            else:
                print("\tFailed case", i)

        driver.close()
        i += 1
    print("Test Case for B - End\n")


def caseCDriver(allow):
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.geolocation": allow}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://selcenkaya.github.io/proj3")
    driver.maximize_window()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    return driver


def casesC(lat, lng, button, driver, latInput, lngInput, errorExp, resultExp, n):
    lat.send_keys(latInput)
    lng.send_keys(lngInput)
    button.click()
    time.sleep(3)

    error = driver.find_element(By.ID, "error4")
    result = driver.find_element(By.ID, "moon")

    if error.text == errorExp and result.text == resultExp:
        print("\tPassed case", n)
    else:
        print("\tFailed case", n)

    lat.clear()
    lng.clear()


def caseC():
    print("Test Case for C - Beginning")

    # 1 - Use location when permission is not given
    driver = caseCDriver(1)
    button = driver.find_element(By.ID, "useLoc")
    button.click()
    time.sleep(3)

    error = driver.find_element(By.ID, "error3")
    result = driver.find_element(By.ID, "moon")

    num = re.findall(r"\d+\.\d+", result.text)
    if error.text == "" and 356000 <= float(num[0]) <= 406000:
        print("\tPassed case 1")
    else:
        print("\tFailed case 1")

    driver.close()

    # 2 - Use location when permission is given
    driver = caseCDriver(2)
    button = driver.find_element(By.ID, "useLoc")
    button.click()
    time.sleep(3)

    error = driver.find_element(By.ID, "error3")

    if error.text != "":
        print("\tPassed case 2")
    else:
        print("\tFailed case 2")

    driver.close()

    # Rest - use one driver
    driver = webdriver.Chrome()
    driver.get("https://selcenkaya.github.io/proj3")
    driver.maximize_window()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    lat = driver.find_element(By.ID, "lat2")
    lng = driver.find_element(By.ID, "lng2")
    button = driver.find_element(By.ID, "useInput")

    # 3 - Empty input fields (both) - Expect error message and no distance shown
    casesC(lat, lng, button, driver, "", "", "Please enter valid coordinates.", "Distance to the Moon's Core: -", 3)

    # 4 - One input field valid, other empty - Expect error message and no distance shown
    casesC(lat, lng, button, driver, "40", "", "Please enter valid coordinates.", "Distance to the Moon's Core: -", 4)

    # 5 - One input field invalid, other empty - Expect error message and no distance shown
    casesC(lat, lng, button, driver, "100", "", "Please enter valid coordinates.", "Distance to the Moon's Core: -", 5)

    # 6 - Invalid inputs (both) - Expect error message and no distance shown
    casesC(lat, lng, button, driver, "-100", "200", "Please enter valid coordinates.", "Distance to the Moon's Core: -", 6)

    # 7 - One field invalid, other valid - Expect error message and no distance shown
    casesC(lat, lng, button, driver, "90", "200", "Please enter valid coordinates.", "Distance to the Moon's Core: -", 7)

    # 8 - Valid inputs (both) - Checks the output's correctness (range)
    lat.send_keys(40)
    lng.send_keys(30)
    button.click()
    time.sleep(3)

    error = driver.find_element(By.ID, "error4")
    result = driver.find_element(By.ID, "moon")

    num = re.findall(r"\d+\.\d+", result.text)
    if error.text == "" and 356000 <= float(num[0]) <= 406000:
        print("\tPassed case 8")
    else:
        print("\tFailed case 8")

    driver.close()
    print("Test Case for C - End\n")


# MAIN

caseA()
caseB()
caseC()

print("THE END")
