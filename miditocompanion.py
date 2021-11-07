import mido
import requests
import time
import mido.backends.rtmidi

import logging
import logging.handlers

from SMWinservice import SMWinservice

COMPANION_URL = "http://localhost:8000/press/bank/"
myLogger = logging.getLogger("MyLogger")


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
        with mido.open_input() as inport:
            myLogger.info("port opened")
            while self.isrunning:
                for message in inport.iter_pending():
                    if message.type == "note_on":
                        page = (message.note // 12) + 1
                        button = (message.note % 12) + 1
                        resp = requests.get(f"{COMPANION_URL}{page}/{button}")
                time.sleep(0.25)


if __name__ == "__main__":
    MidiToCompanion.parse_command_line()