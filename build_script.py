import sys, os
from cx_Freeze import setup, Executable

build_exe_options = {"icon":"ressources/icon.ico",
                     "optimize":2,
                     "compressed":True,
                     "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "PromoConnect",
        version = "0.2",
        description = "Connect to the Promo network",
        options = {"build_exe": build_exe_options},
        executables = [Executable("PromoConnect.py",
                                  shortcutName="PromoConnect",
                                  shortcutDir="DesktopFolder",
                                  base=base,
                                  compress=True)])
