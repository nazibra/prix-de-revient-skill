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
        self.register_intent_file('stock.intent', self.handle_stock)

    #@intent_file_handler('revient.de.prix.intent')
    def handle_stock(self, message):
        article=message.data.get('articles')
        types=message.data.get('typeStock')
        print(article+'-'+types)
        if article is not None and len(article)>2:
            if types is not None :
                getdata={'intent':'stock','val':article,'s2':types}
            else : 
                getdata={'intent':'stock','val':article}
            #getdata={'intent':'stock','val':article}
            resp=requests.get('http://360.topnegoce.com:8000/new/admin/R_Banc_ass/php/Mycroft_ASSET/response.php',params=getdata)
            rep=resp.text
            self.speak(rep)
        else:
            self.speak_dialog('no.art.pr')
            
            
    def handle_prix_revient(self, message):
        article=message.data.get('articles')
        
        if article is not None and len(article)>2:
            
            getdata={'intent':'pr','val':article}
            resp=requests.get('http://360.topnegoce.com:8000/new/admin/R_Banc_ass/php/Mycroft_ASSET/response.php',params=getdata)
            rep=resp.text
            
            if "||" in rep :
                replist=rep.split("||")
                data = {'articles': replist[1],'pr':replist[0]}
                self.speak_dialog('found.pr',data)
                #self.speak(rep)
            elif rep[0:2] == 'no':
                self.speak_dialog(rep)
            else : 
                data = {'arts': article}
                self.speak_dialog('not.found.pr',data)
                
            #resplist=rep.split("||")
            #if len(replist)>1 :
            #    data = {'articles': replist[0],'pr':replist[1]}
            #    #self.speak(rep)
            #    self.speak_dialog('found.pr',data)
            #elif :    
            #    self.speak('cet article est introuvable.')
            
        else:
            self.speak_dialog('no.art.pr')
            #self.speak('cet article est introuvable.')
            


def create_skill():
    return PrixDeRevient()
