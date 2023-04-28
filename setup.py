import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app


setup(
    name="Space Shooter Online",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["img", "sound"]}},
    executables = [Executable("Main.pyw", base = "Win32GUI" if sys.platform == "win32" else None)]

    )



