import webapp2,os, json
from Models import Opportunity
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), 'public/view.html')
error_path = os.path.join(os.path.dirname(__file__), 'public/error.html')
opportunity = Opportunity.Opportunity


class ViewHandler(webapp2.RequestHandler):
    #Handles the /view request, by returning all the opportunities in the datastore
    def get(self):
        query = opportunity.query()
        query.order(opportunity.name)
        result = query.fetch()
        #creates a collection of json objects
        collection = '['
        for row in result:
            obj = {
                "id":row.key.id(),
                "name":row.name,
                "url":row.url,
                "description":row.description,
                "deadline":row.deadline,
                "date":row.date,
                "tags":row.tags
            }
            collection = collection+json.dumps(obj)+','
        collection = collection[:-1]+']'
        res = json.loads(collection)
        #webapp2 allows rendering dynamic content at the server side, which is more efficient and simple than sending json object to client and then build in a table dynamically using javascript
        self.response.write(template.render(path, {'rows': res}))