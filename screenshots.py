import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Variables
urlA = 'https://pep8ci.herokuapp.com/' # set validation linter
repo = 'YourGitHubUserName/Repo'  # Update this with the repository name
branch = 'main'

# GitHub API URL to get the contents of the repository
# https://docs.github.com/en/rest?apiVersion=2022-11-28
api_url = f'https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1'

# Function to get all Python files from the repository
def get_python_files(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        files = response.json().get('tree', [])
        python_files = [file['path'] for file in files if file['path'].endswith('.py')] # edit as needed
        return python_files
    else:
        print("Error fetching repository contents")
        return []

# Get the list of Python files
python_files = get_python_files(api_url)

# Initialize WebDriver
service = Service('/Users/YOURNAME/Downloads/chromedriver-mac-x64/chromedriver')  # Update this with the path to your ChromeDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Function to take a screenshot of the validation page
def take_screenshot(url, save_path):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load completely
    screenshot = driver.save_screenshot(save_path)
    return screenshot

# Make directory to save screenshots
screenshots_dir = 'screenshots'
os.makedirs(screenshots_dir, exist_ok=True)

# Iterate over each Python file and take screenshots
for python_file in python_files:
    # Construct the validation URL
    raw_url = f'https://raw.githubusercontent.com/{repo}/{branch}/{python_file}'
    validation_url = f'{urlA}{raw_url}' # based on CI pip8 validator

    # Define the save path for the screenshot
    save_path = os.path.join(screenshots_dir, f"{python_file.replace('/', '_')}.png")

    # Take the screenshot
    take_screenshot(validation_url, save_path)
    print(f"Screenshot saved for {python_file}")

# Close the browser
driver.quit()

# Print the location of the screenshots directory when done
print(f"All screenshots are saved in the directory: {os.path.abspath(screenshots_dir)}")
