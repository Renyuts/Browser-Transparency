import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time

def main():
    subprocess.Popen("start chrome", shell=True) ## 開啟chrome網頁
    time.sleep(5) ## 這邊讓程式等個五秒，才能抓到下面顯示的頁簽內容
    hwnd = win32gui.FindWindow(None, "新分頁 - Google Chrome")  ## 後面的新分頁 - Google Chrome要填入頁簽顯示的名字喔

    win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
    winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 30, win32con.LWA_ALPHA) ## 中間的30是透明度，數字越小越淺，可以自由更改

if __name__ == "__main__":
    main()