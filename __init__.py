import requests
from mycroft import MycroftSkill, intent_file_handler

class PrixDeRevient(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #@intent_file_handler('revient.de.prix.intent')
    #def handle_revient_de_prix(self, message):
    #    self.speak_dialog('revient.de.prix')

    def initialize(self):
        self.register_intent_file('prix.de.revient.intent', self.handle_prix_revient)

    #@intent_file_handler('revient.de.prix.intent')
    def handle_prix_revient(self, message):
        article=message.data.get('articles')
        
        if article is not None:
            
            getdata={'intent':'pr','val':article}
            resp=requests.get('http://360.topnegoce.com:8000/new/admin/R_Banc_ass/php/Mycroft_ASSET/response.php',params=getdata)
            rep=resp.text
            
            if "||" in rep :
                self.speak(rep)
            else : 
                self.speak_dialog('not.found.pr')
                
            #resplist=rep.split("||")
            #if len(replist)>1 :
            #    data = {'articles': replist[0],'pr':replist[1]}
            #    #self.speak(rep)
            #    self.speak_dialog('found.pr',data)
            #elif :    
            #    self.speak('cet article est introuvable.')
            
        else:
            data = {'arts': article}
            self.speak_dialog('cet article est introuvable.',data)
        #self.speak_dialog('revient.de.prix')


def create_skill():
    return PrixDeRevient()
