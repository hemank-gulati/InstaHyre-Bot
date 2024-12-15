# Automated Job Application Bot

This project is an automated bot built using Python and Selenium to apply for jobs on Instahyre. The bot logs into an Instahyre account, applies filters for specific job functions, and automates the application process by repeatedly clicking the "Apply" button on listed jobs.

## Features

- **Automated Login**: Logs into the user's Instahyre account using email and password.
- **Job Filters**: Filters jobs based on specified job functions and experience level.
- **Automated Applications**: Applies to jobs by automatically clicking the "Apply" button for available positions.
- **Scalability**: The bot can be run in a loop to apply for a large number of jobs (up to 1000 in this case).
- **Notifications Disabled**: Chrome notifications are disabled for a seamless experience.

## Prerequisites

- Python 3.x
- Selenium (`pip install selenium`)
- Chrome WebDriver (compatible with your Chrome browser version)

## Installation

1. Clone the repository or download the source code.
    ```bash
    git clone https://github.com/your-username/job-application-bot.git
    cd job-application-bot
    ```

2. Install the required Python packages.
    ```bash
    pip install selenium
    ```

3. Download the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) and ensure it matches your Chrome browser version.

4. Place the `chromedriver.exe` in the project directory or add its path to your system's environment variables.
5. Run the command:
   ```bash
   python3 apply.py
    ```
**Note**: If you are using older version of python: `python apply.py`

## Configuration

Before running the bot, make sure to update the following details in the code:

- **Email and Password**: Replace the email and password in the script with your Instahyre credentials.
  ```python
  email_input.send_keys("your-email@example.com")
  password_input.send_keys("your-password")

