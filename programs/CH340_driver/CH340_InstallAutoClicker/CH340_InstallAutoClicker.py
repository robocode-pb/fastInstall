# pip install pyinstaller pywin32
# pyinstaller --onefile CH340_InstallAutoClicker.py

from time import sleep
from win32gui import FindWindow, GetWindowText, EnumChildWindows, GetWindowRect
from win32api import SendMessage, SetCursorPos, mouse_event
from win32con import BM_CLICK, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP

def search_element(window_name:str, element_title:str) -> str|bool: 
    sleep(3)
    print('\n'*2)
    hwnd = FindWindow(None, window_name)
    if not hwnd:
        print(f"Failed to find the '{window_name}' window.")
        return None
    element_hwnd = None
    def callback(child_hwnd, _):
        nonlocal element_hwnd
        window_text = GetWindowText(child_hwnd)
        print(f"Found child window: {window_text}")
        if window_text == element_title:
            element_hwnd = child_hwnd
    EnumChildWindows(hwnd, callback, None)
    if not element_hwnd:
        print(f"Failed to find the '{element_title}' in '{window_name}' window.")
        return False
    return element_hwnd

def click_button(window_name:str, button_title:str) -> bool:
    button_hwnd = search_element(window_name, button_title)
    if not button_hwnd: return False
    SendMessage(button_hwnd, BM_CLICK, 0, 0)
    print(f"{button_title} button clicked successfully")
    return True

def click_checkbox(window_name:str, checkbox_title:str) -> bool:
    checkbox_hwnd = search_element(window_name, checkbox_title)
    if not checkbox_hwnd: return False
    left, top, right, bottom = GetWindowRect(checkbox_hwnd)
    x = (left + right) // 2
    y = (top + bottom) // 2
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    print(f"Checkbox '{checkbox_title}' clicked successfully")
    return True

print(f'{"!"*10}Start auto click install S4A{"!"*10}')

sleep(5)
click_button('DriverSetup(X64)', 'INSTALL')


# from win32com import BM_SETCHECK, BST_CHECKED, BST_UNCHECKED,
# def check_checkbox(window_name, checkbox_title, check=True):
#     checkbox_hwnd = search_element(window_name, checkbox_title)
#     if checkbox_hwnd:
#         SendMessage(checkbox_hwnd, BM_SETCHECK, BST_CHECKED if check else BST_UNCHECKED, 0)
#         print(f"Checkbox '{checkbox_title}' {'checked' if check else 'unchecked'} successfully")
#     else:
#         print(f"Failed to find the checkbox '{checkbox_title}' in '{window_name}' window.")
# Not Work :( F@ck win32api
# check_checkbox('Setup - S4A', 'I &do not accept the agreement', False)
# check_checkbox('Setup - S4A', 'I &accept the agreement')