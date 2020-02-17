import requests
from mycroft import MycroftSkill, intent_file_handler

class PrixDeRevient(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('revient.de.prix.intent')
    def handle_revient_de_prix(self, message):
        self.speak_dialog('revient.de.prix')

    def initialize(self):
        self.register_intent_file('prix.de.revient.intent', self.handle_prix_revient)

    #@intent_file_handler('revient.de.prix.intent')
    def handle_prix_revient(self, message):
        article=message.data.get('articles')
        if article is not None:
            getdata={'intent':'pr','val':article}
            resp=requests.get('http://360.topnegoce.com:8000/new/admin/R_Banc_ass/php/SNIPS_ASSET/response.php',params=getdata)
            rep=resp.text
            self.speak(rep)
        else:
            self.speak('cet article est introuvable.')
        #self.speak_dialog('revient.de.prix')


def create_skill():
    return PrixDeRevient()
