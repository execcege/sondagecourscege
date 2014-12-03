import StringIO
import csv
import webapp2
from entities import Respondant


class data(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Disposition"] = "attachment;filename=reponsesSondage.csv"

        tmp = StringIO.StringIO()
        csv_output = csv.writer(tmp)
        respondants = Respondant.query()
        # Would have to separate view.
        # Write the 'header'
        csv_output.writerow(['matricule', 'sigle', 'no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'no7', 'no8', 'no9', 'no10', 'no11', 'no12', 'no13', 'no14', 'no15', 'no16', 'no17', 'no18', 'no19', 'no20', 'no21', 'no22', 'no23', 'no24', 'no25', 'no26', 'no27', 'no28', 'no29', 'no30'])

        # Write the 'body'
        for respondant in respondants.iter():
            for response in respondant.responses:

                csv_output.writerow([respondant.matricule, response.sigle, response.no1, response.no2, response.no3, response.no4, response.no5, response.no6, response.no7, response.no8, response.no9, response.no10, response.no11, response.no12, response.no13, response.no14, response.no15, response.no16, response.no17, response.no18, response.no19, response.no20, response.no21, response.no22, response.no23, response.no24, response.no25, response.no26, response.no27, response.no28, response.no29, response.no30])

        contents = tmp.getvalue()
        tmp.close()

        self.response.write(contents)


application = webapp2.WSGIApplication([
    ('/api/data', data),
], debug=True)
