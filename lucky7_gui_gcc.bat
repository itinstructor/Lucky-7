cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --enable-plugin=tk-inter ^
    --windows-console-mode=disable ^
    --windows-icon-from-ico=slot_machine.ico ^
    lucky7.py
pause