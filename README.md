# Automated Coursera Course Bot

This Python script automates interactions with Coursera courses, including marking videos and readings as completed, and navigating through course content. It supports **Remote Desktop Protocol (RDP)** usage on GitHub and uses Selenium for browser automation.

---

## Features
- **Automated Login**: Login manually once and save cookies for future sessions.
- **Course Navigation**: Automatically navigate through course modules and mark items as completed.
- **Multi-course Support**: Process multiple courses simultaneously by inputting an array of course links.
- **Hotkey Integration**: Use `Ctrl + Alt + D` to stop the automation loop.

---

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
