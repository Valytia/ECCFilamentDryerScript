## Environment variables
IP = "192.168.X.X"
TEMP = 50
INTERVAL = 30 * 60 - 10 # 30 minutes in seconds, with 10 seconds offset to avoid moments without bed heating


# Elegoo™ Centauri Carbon Filament Dryer Script
# Copyright (C) 2025 Valytia
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import datetime
import signal
import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


## Driver variables (don't touch)
driver = None
driver_options = Options()
driver_options.add_argument("-headless")


def main():
    global IP, TEMP, INTERVAL, driver    

    # Set up graceful exit that closes browser session properly
    signal.signal(signal.SIGINT, signal_handler)

    print(f"\tProgram for setting Elegoo™ Centauri Carbon's Bed Temp has started.")
    print(f"\tIP: {IP}, Temperature: {TEMP}°C, Interval: {INTERVAL}s")
    print(f"\tExit by using Ctrl+C")

    # Set printer temp in a loop
    while True:
        # Open up a browser with printer's website (+ Error handling)
        if not setup_driver(IP): 
            log("Retrying in 30 seconds")
            sleep(30)
            continue

        # Set the temp
        set_printer_temp(driver, TEMP)
        # Close driver
        driver.quit()
        driver = None
        # Wait until another temp setting.
        log(f"Next temperature set will occur on {(datetime.datetime.now() + datetime.timedelta(seconds=INTERVAL)).strftime("%X")}")
        sleep(INTERVAL)
    


def setup_driver(IP: str):
    global driver, driver_options
    try:
        log("Starting browser/Selenium driver")
        # Turn on the driver
        driver = webdriver.Firefox(options=driver_options)
        driver.set_window_size(1600, 900)

        # Download the website
        driver.get(f"http://{IP}/network-device-manager/network/control")

        # Check for Whether the website has loaded
        if "ELEGOO-Create The Future" not in driver.title:
            raise Exception("The website has been loaded, but it's not a printer's page!")
        
        # Allow the website to load fully
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex-1 .status-icon")))

        log(f"Successfully loaded printer's website at {IP}.")
        return True
    except Exception as e:
        log(f"Failed to load printer's website at IP: {IP}.")
        log(f"Exception: {e}")
        driver.quit()
        driver = None
        return False


def set_printer_temp(driver, TEMP: int):
    while True:
        try:
            log(f"Setting printer's bed temperature to {TEMP}°C.")
            # Remove the current temperature and set the desired one
            bed_temp_element = driver.find_element(By.XPATH, r"(//input[@type='text'])[2]")
            bed_temp_element.send_keys(Keys.CONTROL, "a")
            bed_temp_element.send_keys(Keys.DELETE)
            bed_temp_element.send_keys(str(TEMP))
            bed_temp_element.send_keys(Keys.RETURN)

            # Confirm the change in the pop up
            driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary > .ng-star-inserted").click()

            # Check whether the change worked, if yes, stop trying to change it
            #if bed_temp_element.text != str(TEMP):
            #    raise Exception("Failed to change printer's temperature.")
            log(f"Successfully set printer's temp.")
            break
        except Exception as e:
            log(f"Exception: {e}")


def signal_handler(sig, frame):
    log("Gracefully shutting down...")
    if driver:
        driver.quit()
    sys.exit(0)

def log(message: str):
    current_time = datetime.datetime.now().strftime("%Y %B %d, %X")
    print("[" + str(current_time) + "]", str(message))

if __name__ == "__main__":
    main()
