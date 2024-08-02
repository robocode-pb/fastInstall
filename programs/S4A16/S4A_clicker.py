from time import sleep
from win32gui import FindWindow, GetWindowText, EnumChildWindows, GetWindowRect
from win32api import SendMessage, SetCursorPos, mouse_event
from win32con import BM_CLICK, BM_SETCHECK, BST_CHECKED, BST_UNCHECKED, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP

def click_button(window_name, button_title):
    sleep(3)
    hwnd = FindWindow(None, window_name)
    if not hwnd:
        print(f"Failed to find the '{window_name}' window.")
        return None
    
    button_hwnd = None
    def callback(child_hwnd, _):
        nonlocal button_hwnd
        window_text = GetWindowText(child_hwnd)
        print(f"Found child window: {window_text}")  # Debugging line
        if window_text == button_title:
            button_hwnd = child_hwnd
    EnumChildWindows(hwnd, callback, None)

    if button_hwnd:
        SendMessage(button_hwnd, BM_CLICK, 0, 0)
        print(f"{button_title} button clicked successfully")
    else:
        print(f"Failed to find the '{button_title}' button in '{window_name}' window.")

def click_checkbox(window_name, checkbox_title):
    sleep(3)
    hwnd = FindWindow(None, window_name)
    if not hwnd:
        print(f"Failed to find the '{window_name}' window.")
        return None
    
    checkbox_hwnd = None
    def callback(child_hwnd, _):
        nonlocal checkbox_hwnd
        window_text = GetWindowText(child_hwnd)
        print(f"Found child window: {window_text}")  # Debugging line
        if window_text == checkbox_title:
            checkbox_hwnd = child_hwnd
    EnumChildWindows(hwnd, callback, None)

    if checkbox_hwnd:
        left, top, right, bottom = GetWindowRect(checkbox_hwnd)
        x = (left + right) // 2
        y = (top + bottom) // 2
        SetCursorPos((x, y))
        mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        print(f"Checkbox '{checkbox_title}' clicked successfully")
    else:
        print(f"Failed to find the checkbox '{checkbox_title}' in '{window_name}' window.")


click_button('Select Setup Language', 'OK')
click_button('Setup - S4A', '&Next >')
click_checkbox('Setup - S4A', 'I &accept the agreement')
for _ in range(4):
    click_button('Setup - S4A', '&Next >')
click_button('Setup - S4A', '&Install')



# def check_checkbox(window_name, checkbox_title, check=True):
#     hwnd = FindWindow(None, window_name)
#     if not hwnd:
#         print(f"Failed to find the '{window_name}' window.")
#         return None
    
#     checkbox_hwnd = None
#     def callback(child_hwnd, _):
#         nonlocal checkbox_hwnd
#         window_text = GetWindowText(child_hwnd)
#         print(f"Found child window: {window_text}")  # Debugging line
#         if window_text == checkbox_title:
#             checkbox_hwnd = child_hwnd
#     EnumChildWindows(hwnd, callback, None)

#     if checkbox_hwnd:
#         SendMessage(checkbox_hwnd, BM_SETCHECK, BST_CHECKED if check else BST_UNCHECKED, 0)
#         print(f"Checkbox '{checkbox_title}' {'checked' if check else 'unchecked'} successfully")
#     else:
#         print(f"Failed to find the checkbox '{checkbox_title}' in '{window_name}' window.")

# Not Work :( F@ck win32api
# check_checkbox('Setup - S4A', 'I &do not accept the agreement', False)
# check_checkbox('Setup - S4A', 'I &accept the agreement')