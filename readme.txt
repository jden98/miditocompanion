DEV SETUP:
  pip install python-rtmidi
  pip install mido 
  pip install pyinstaller


Commandline to create EXE: 
  pyinstaller.exe --runtime-tmpdir=. --onefile --hidden-import win32timezone miditocompanion.py

  miditocompanion.exe will be in the dist directory.

To install service:
  miditocompanion install
  net start miditocompanion  (perhaps go to service manager and set to automatic startup)

To remove service:
  net stop miditocompanion
  miditocompanion remove

Update to new version:
  miditocompanion Update

