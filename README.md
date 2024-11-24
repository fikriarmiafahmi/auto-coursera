# Automated Coursera Course Bot
## [Bot 100% Marked Video and Reading Module]

This Python script automates interactions with Coursera courses, including marking videos and readings as completed, and navigating through course content. It supports **Remote Desktop Protocol (RDP)** usage on GitHub and uses Selenium for browser automation.

---

## Features
- **Automated Login**: Login manually once and save cookies for future sessions.
- **Course Navigation**: Automatically navigate through course modules and mark items as completed.
- **Multi-course Support**: Process multiple courses simultaneously by inputting an array of course links.
- **Hotkey Integration**: Use `Ctrl + C` to stop the automation loop.

---

## CREATE RDP USING GITHUB
### Pakai RDP agar jaringannya fast dan ngga lambat
You can check tutorial on my repository about [Free RDP Github](https://github.com/fikriarmiafahmi/freeRDP).
### And then, run RDP and install requirements on below into the RDP

## Prerequisites
Ensure the following packages are installed:
```bash
pip install webdriver_manager
pip install selenium
pip install pyautogui
pip install keyboard
```

## Required Tools
Firefox Browser: Selenium is configured for Firefox.
Profile Path: Update the Firefox profile path in the script for automatic login.

## Usage Instructions
1. Clone the Repository
   ```bash
   git clone https://github.com/yourusername/coursera-bot.git
   cd coursera-bot
   ```
2. Configure User Credentials
   Update the following variables in the script:
   ```python
   username = "your-email@example.com"
   password = "your-password"
   ```
3. Run the Script
   ```bash
   python coursera-rdp.py
   ```

4. Input Course Links
   When prompted, input the Coursera course links as a space-separated list:
   ```text
   Mau input array link course (pisahkan dengan spasi): link1 link2 link3
   ```
   ## NOTE:
   Pakai link yang ada di awal course/introduction
   contohnya seperti ini:
   <br>https://www.coursera.org/learn/introduction-to-databases/lecture/JUPWU/introduction-to-the-program
   <br>atau yang seperti ini, ada tulisan modulenya
   <br>https://www.coursera.org/learn/introduction-to-databases/home/module/1
   

6. Save Cookies
After logging in manually, press Enter when prompted to save cookies for future sessions.

## Hotkey Usage
Stop Automation: Press Ctrl + C to stop the current process.
## Limitations
Requires manual login for the first run to save cookies.
Configured specifically for Coursera courses; adjust XPath or CSS selectors if UI changes.

# DISCLAIMER!!!
```hash
Disclaimer of Liability:
This script is provided for educational and informational purposes only. 
The author is not responsible for any misuse, damage, or legal consequences 
that may arise from the use of this software. Users are responsible for 
complying with all applicable laws and terms of service of the platforms 
involved.
```
