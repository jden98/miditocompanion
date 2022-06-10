DEV SETUP:
  pip install python-rtmidi
  pip install mido 
  pip install pyinstaller

Windows does not support virtual Midi ports natively.  On Windows:
  Install loopmidi from http://www.tobias-erichsen.de/wp-content/uploads/2020/01/loopMIDISetup_1_0_16_27.zip
  Create a port named MidiToCompanion
  This must be done for both dev and production on Windows

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

