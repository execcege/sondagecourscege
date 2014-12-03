import webapp2
import json
from entities import Response, Respondant


class Answer(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

    def post(self):
        received_dictionary = json.loads(self.request.body)
        print received_dictionary
        respondant = Respondant()
        respondant.matricule = received_dictionary['matricule']
        for reponse in received_dictionary['responses']:
            to_add = Response()
            to_add.no1 = reponse['no1']
            to_add.no2 = reponse['no2']
            to_add.no3 = reponse['no3']
            to_add.no4 = reponse['no4']
            to_add.no5 = reponse['no5']
            to_add.no6 = reponse['no6']
            to_add.no7 = reponse['no7']
            to_add.no8 = reponse['no8']
            to_add.no9 = reponse['no9']
            to_add.no10 = reponse['no10']
            to_add.no11 = reponse['no11']
            to_add.no12 = reponse['no12']
            to_add.no13 = reponse['no13']
            to_add.no14 = reponse['no14']
            to_add.no15 = reponse['no15']
            to_add.no16 = reponse['no16']
            to_add.no17 = reponse['no17']
            to_add.no18 = reponse['no18']
            to_add.no19 = reponse['no19']
            to_add.no20 = reponse['no20']
            to_add.no21 = reponse['no21']
            to_add.no22 = reponse['no22']
            to_add.no23 = reponse['no23']
            to_add.no24 = reponse['no24']
            to_add.no25 = reponse['no25']
            to_add.no26 = reponse['no26']
            to_add.no27 = reponse['no27']
            to_add.no28 = reponse['no28']
            to_add.no29 = reponse['no29']
            to_add.no30 = reponse['no30']
            to_add.sigle = reponse['sigle']
            respondant.responses.append(to_add)
        respondant.put()

application = webapp2.WSGIApplication([
    ('/api/Answer', Answer),
], debug=True)
