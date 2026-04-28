import time
import pyperclip
import pyautogui

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

def format_text(text):
    return ' '.join(text.lower().split())

last_text = pyperclip.paste()

print("Monitoring clipboard...")
print("When you copy a lyric, you will have 2 seconds to click the 'lyric' cell.")
print("Then the script will paste the formatted text automatically.")
print("Press Ctrl+C in the terminal to stop.\n")

while True:
    try:
        current_text = pyperclip.paste()

        if current_text and current_text != last_text:
            formatted_text = format_text(current_text)
            pyperclip.copy(formatted_text)

            print("New text detected. Click the target cell now...")
            time.sleep(2)

            pyautogui.hotkey('ctrl', 'v')
            print("Formatted text pasted.")

            last_text = pyperclip.paste()

        time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nClipboard monitor stopped.")
        break