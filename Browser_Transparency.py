import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("--cmd", type=str, default='start chrome', help='command line')
    parser.add_argument("--time", type=int, default=5, help='waiting time')
    parser.add_argument("--title", type=str, default='新分頁 - Google Chrome', help='pagination title')
    parser.add_argument("--transparency", type=int, default=30, help='browser transparency')
    args = parser.parse_args()

    ## 開啟chrome網頁(執行 "start chrome" 命令)
    subprocess.Popen(args.cmd, shell=True)
    ## 這邊讓程式等個五秒，才能抓到下面顯示的頁簽內容
    time.sleep(args.time) 
    ## 搜尋標籤為 "新分頁 - Google Chrome" 的網頁, return 視窗 或 None
    hwnd = win32gui.FindWindow(None, args.title)  

    win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
    ## 中間的30是透明度，數字越小越淺
    winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), args.transparency, win32con.LWA_ALPHA)

if __name__ == "__main__":
    main()