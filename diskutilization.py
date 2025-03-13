import os
import time
import smtplib
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.message import EmailMessage

# AWS Credentials (Use environment variables for security)
AWS_USERNAME = "selvapriya"
AWS_PASSWORD = "S3l^@Pr!y@aW$25"
S3_BUCKET_NAME = "vendorlists3"
ACCOUNT_ID = "378524233787"

# Chrome options (Headless mode for automation)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Remove this for debugging
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open AWS Login Page
    driver.get("https://s3.console.aws.amazon.com/s3/home")
    wait = WebDriverWait(driver, 30)

    # Step 2: Enter Account ID (if required)
    account_id_input = wait.until(EC.presence_of_element_located((By.ID, "account")))
    account_id_input.send_keys(ACCOUNT_ID)
    account_id_input.send_keys(Keys.RETURN)
    time.sleep(3)

    # Step 3: Enter IAM Username
    email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_input.send_keys(AWS_USERNAME)
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    # Step 4: Enter IAM Password
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(AWS_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Step 5: Navigate to Specific S3 Bucket
    bucket_url = f"https://s3.console.aws.amazon.com/s3/buckets/{S3_BUCKET_NAME}?region=ap-south-1&tab=objects"
    driver.get(bucket_url)
    time.sleep(5)

    # Step 6: Capture Screenshot of File List
    screenshot_path = "s3_file_list.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

finally:
    driver.quit()  # Close browser

# Step 6: Send Screenshot via Email
def send_email(screenshot_path):
    sender_email = "selvapriyaselvaraj2025@gmail.com"
    receiver_email = "selvapriyaselvaraj2025@gmail.com"
    subject = "AWS S3 File List Screenshot"
    body = "Please find the attached screenshot of the S3 bucket files."

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach the screenshot
    with open(screenshot_path, "rb") as file:
        msg.add_attachment(file.read(), maintype="image", subtype="png", filename="s3_file_list.png")

    # Send the email via SMTP (Use environment variable for password)
    EMAIL_PASSWORD = "kbng zzxf njtr lrgt"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email sent successfully.")

# Call email function
send_email(screenshot_path)
