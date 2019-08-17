# d88888b  .d8b.  .d8888. db    db   .d8888.  .o88b. d8888b. d88888b d88888b d8b   db   d88888b db      d888888b d8888b. d8888b. d88888b d8888b.
# 88'     d8' `8b 88'  YP `8b  d8'   88'  YP d8P  Y8 88  `8D 88'     88'     888o  88   88'     88        `88'   88  `8D 88  `8D 88'     88  `8D
# 88ooooo 88ooo88 `8bo.    `8bd8'    `8bo.   8P      88oobY' 88ooooo 88ooooo 88V8o 88   88ooo   88         88    88oodD' 88oodD' 88ooooo 88oobY'
# 88~~~~~ 88~~~88   `Y8b.    88        `Y8b. 8b      88`8b   88~~~~~ 88~~~~~ 88 V8o88   88~~~   88         88    88~~~   88~~~   88~~~~~ 88`8b
# 88.     88   88 db   8D    88      db   8D Y8b  d8 88 `88. 88.     88.     88  V888   88      88booo.   .88.   88      88      88.     88 `88.
# Y88888P YP   YP `8888Y'    YP      `8888Y'  `Y88P' 88   YD Y88888P Y88888P VP   V8P   YP      Y88888P Y888888P 88      88      Y88888P 88   YD
# d8888b. db    db    .o888b. d8888b.  .d88b.   .d88b.  db      db       .d88b.  db    db d88888b d8888b. d8b   db  .d8b.  d888888b db   db  .d8b.  d8b   db
# 88  `8D `8b  d8'   d8'   Y8 88  `8D .8P  Y8. .8P  Y8. 88      88      .8P  Y8. 88    88 88'     88  `8D 888o  88 d8' `8b `~~88~~' 88   88 d8' `8b 888o  88
# 88oooY'  `8bd8'    8P db dP 88oodD' 88    88 88    88 88      88      88    88 Y8    8P 88ooooo 88oobY' 88V8o 88 88ooo88    88    88ooo88 88ooo88 88V8o 88
# 88~~~b.    88      8b V8o8P 88~~~   88    88 88    88 88      88      88    88 `8b  d8' 88~~~~~ 88`8b   88 V8o88 88~~~88    88    88~~~88 88~~~88 88 V8o88
# 88   8D    88      Y8.    d 88      `8b  d8' `8b  d8' 88booo. 88booo. `8b  d8'  `8bd8'  88.     88 `88. 88  V888 88   88    88    88   88 88   88 88  V888
# Y8888P'    YP       `Y888P' 88       `Y88P'   `Y88P'  Y88888P Y88888P  `Y88P'     YP    Y88888P 88   YD VP   V8P YP   YP    YP    YP   YP YP   YP VP   V8P
from invscr import invscr
from norscr import norscr
from platfrom import system # Platform check
from sys import exit,stderr # Oops, wrong platform
import subprocess as sp
os = system().lower()
if __name__ == "__main__" and os == "linux":
  prompt_process = sp.run("
