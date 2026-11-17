"""My first OpenVoiceOS skill.

Say "hello from my skill" and Emkay answers. Change the sentences in
locale/<language>/hello.intent, the answer in hello.dialog, and the code
below - save, and Emkay (in the Emkay panel in VS Code) runs the new
version right away.
"""
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill


class HelloSkill(OVOSSkill):

    @intent_handler("hello.intent")
    def handle_hello(self, message):
        """Someone said one of the sentences in hello.intent."""
        self.speak_dialog("hello")
