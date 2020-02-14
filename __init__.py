from mycroft import MycroftSkill, intent_file_handler


class PrixDeRevient(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('revient.de.prix.intent')
    def handle_revient_de_prix(self, message):
        self.speak_dialog('revient.de.prix')


def create_skill():
    return PrixDeRevient()

