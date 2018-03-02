import webapp2,os,csv
from Models import Opportunity
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), 'public/index.html')
error_path = os.path.join(os.path.dirname(__file__), 'public/error.html')


class FileParser(webapp2.RequestHandler):
    def post(self):
        #get file uploaded by the client
        input_file = self.request.POST.get('inputfile')
        if input_file.filename.endswith('.csv'):
            #Read the contents of the file
            file_data = csv.reader(input_file.file,delimiter=',')
            headings = next(file_data)
            #If the format of the file is as expected then proceed to store it
            #If not, then alert the client that the file is in invalid format
            if headings[0]=='UID' and headings[1]=='Name' and headings[2]=='URL' and headings[3]=='Description' and headings[4]=='Deadline' and headings[5]=="Date" and headings[6]=="Tags":
                 #Create a new entity object for each row and store the data in respective fields
                 for row in file_data:
                   try:
                       #Search if the same opportunity already exists
                        query = Opportunity.Opportunity.query(Opportunity.Opportunity.name==row[1],Opportunity.Opportunity.url==row[2],Opportunity.Opportunity.deadline==row[4],Opportunity.Opportunity.date==row[5],Opportunity.Opportunity.tags==row[6])
                        result = query.get()
                        print result
                        print "----------------------1"
                        if result is None:
                            opportunity = Opportunity.Opportunity()
                            opportunity.name = row[1]
                            opportunity.url = row[2]
                            opportunity.description = row[3]
                            opportunity.deadline = row[4]
                            opportunity.date = row[5]
                            opportunity.tags = row[6]
                            opportunity.put()
                   except Exception as e:
                            print(type(e))
                            print(e.args)
                            print(e)
                            self.response.write(template.render(error_path, {}))
                            return
                 self.response.write(template.render(path, {'good_message': 'Opportunities were added Successfully!'}))
            else:
                self.response.write(template.render(path, {'bad_message': 'Invalid table format! Required: UID,Name,URL,Description,Deadline,Date,Tags'}))