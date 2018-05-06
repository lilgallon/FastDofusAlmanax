RMDIR /S /Q deployed\
pyinstaller --onefile src\main.py
RMDIR /S /Q build\
DEL main.spec
RENAME dist deployed
xcopy LICENSE deployed\
xcopy README.md deployed\
RENAME deployed\main.exe FAST_ALMANAX_DOFUS.exe