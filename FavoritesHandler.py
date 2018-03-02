import webapp2,os, json
from Models import Opportunity,User
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), 'public/favorites.html')
error_path = os.path.join(os.path.dirname(__file__), 'public/error.html')
opportunity = Opportunity.Opportunity


class FavoritesHandler(webapp2.RequestHandler):
    # Handles /favorites requesst, returning all the favorite opportunities by a particular user
    def get(self):
        user = User.User
        query = user.query()
        query.filter(user.id == 1)      # Assuming user has user id as 1
        user_obj = query.get()
        res = ''
        #Check if the user exists
        if user_obj is not None:
            collection = '['
            #Check if the user has a favorites list
            if user_obj.favorites != None:
                for key in user_obj.favorites:
                    opp = opportunity.get_by_id(key)
                    obj = {
                        "id":opp.key.id(),
                        "name":opp.name,
                        "url":opp.url,
                        "description":opp.description,
                        "deadline":opp.deadline,
                        "date":opp.date,
                        "tags":opp.tags
                    }
                    collection = collection+json.dumps(obj)+','
                if len(collection) > 1:
                    collection = collection[:-1]+']'
                    res = json.loads(collection)
            # Passing the list of favorites along with template to DJango's templating engine
        self.response.write(template.render(path, {'rows': res}))

    # Handles /editFav request, either Adds or removes the opportunity form favorites
    def post(self):
        user = User.User
        try:
            # A single user with id 1 and name Paurav
            user_id = 1
            user_name = 'Paurav'
            opportunity_id = self.request.get('id')
            function_mode = self.request.get('type')
            query = user.query(user.id == 1)
            result = query.get()
            # Check if user doesnt already exists
            if(result == None):
                #Create user and add the opportunity to favorites
                if(function_mode == "add"):
                    user_obj = user()
                    user_obj.name = user_name
                    user_obj.id = user_id
                    user_obj.favorites = [int(opportunity_id)]
                    user_obj.put()
            #If user already exists
            else:
                user_obj = result
                fav_list = user_obj.favorites
                #Add the opportunity to favorites
                if (function_mode == "add"):
                    if int(opportunity_id) not in fav_list:
                        fav_list.extend([int(opportunity_id)])
                #Remove the opportunity from favorites
                if (function_mode == "remove"):
                    if int(opportunity_id) in fav_list:
                        fav_list.remove(int(opportunity_id))
                user_obj.favorites = fav_list
                user_obj.put()
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            self.response.write(template.render(error_path, {}))
            return
        self.response.out.write("Success")
