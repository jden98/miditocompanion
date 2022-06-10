import mido
import requests
import time
import mido.backends.rtmidi

import logging
import logging.handlers

import configparser

from pathlib import Path
from SMWinservice import SMWinservice

myLogger = logging.getLogger("MyLogger")

# "http://localhost:8000/press/bank/"

#   Companion url (domain:port)
class MidiToCompanion(SMWinservice):
    _svc_name_ = "MidiToCompanion"
    _svc_display_name_ = "Midi Notes to Companion GET requests"
    _svc_description_ = "Accept Midi note_on commands starting with note 0 where each note is a page and button."

    def start(self):
        myLogger.info("***Starting\n")
        self.isrunning = True

    def stop(self):
        myLogger.info("***Stopping\n")
        self.isrunning = False

    def main(self):
        myLogger.info("in main")
        # check for MidiToCompanion in get_input_names()
        # if there, open it, if not, open it virtual.  Log issues.
        iniFile = "C:\\MidiToCompanion\\MidiToCompanion.ini"
        myLogger.info(iniFile)
        config = configparser.ConfigParser()
        config.read(iniFile)
        COMPANION_URL = config["DEFAULT"]["COMPANION_URL"] + "/press/bank/"

        portName = next(
            (x for x in mido.get_input_names() if x.startswith("MidiToCompanion")), None
        )
        if portName is None:
            setVirtual = True
            portName = "MidiToCompanion"
            myLogger.info(
                "MidiToCompanion Port not found.  Trying Virtual (won't work on Windows)."
            )
        else:
            setVirtual = False
            myLogger.info(f"MidiToCompanion Port: {portName}")

        with mido.open_input(portName, virtual=setVirtual) as inport:
            myLogger.info("port opened")
            while self.isrunning:
                for message in inport.iter_pending():
                    if message.type == "note_on":
                        page = (message.note // 12) + 1
                        button = (message.note % 12) + 1
                        resp = requests.get(f"{COMPANION_URL}{page}/{button}")
                time.sleep(0.1)


if __name__ == "__main__":
    MidiToCompanion.parse_command_line()