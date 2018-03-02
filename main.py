#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, os, FileParser, ViewHandler, FavoritesHandler
from google.appengine.ext.webapp import template


class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'public/index.html')
        self.response.write(template.render(path,{'message':''}))


routes = [('/', MainHandler),('/upload',FileParser.FileParser) ,('/view',ViewHandler.ViewHandler),('/editFav',FavoritesHandler.FavoritesHandler),('/favorites',FavoritesHandler.FavoritesHandler)]
app = webapp2.WSGIApplication(routes=routes, debug=True)
