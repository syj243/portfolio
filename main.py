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
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class firstHandler(webapp2.RequestHandler):
    # def get(self):
    #     template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    #     self.response.write(template.render({'title': 'HOME'}))
    def get(self):      
        path = self.request.path
        logging.info(path)
        if path == "/":
            path = "/index"
        template = JINJA_ENVIRONMENT.get_template('templates' + path + '.html')
        if path == "/index":
            self.response.write(template.render({'title': 'HOME'}))
        if path == "/food":
            self.response.write(template.render({'title': 'FOOD'}))
        if path == "/hobby":
            self.response.write(template.render({'title': 'HOBBY'}))
        if path == "/personal":
            self.response.write(template.render({'title': 'PERSONAL'}))

        
# class FamilyHandler(webapp2.RequestHandler):
#     def get(self):
#     	template = JINJA_ENVIRONMENT.get_template('templates/hobby.html')
#     	self.response.write(template.render({'title': 'HOBBY'}))

# class FoodHandler(webapp2.RequestHandler):
#     def get(self):
#     	template = JINJA_ENVIRONMENT.get_template('templates/food.html')
#     	self.response.write(template.render({'title': 'FOOD'}))

class loginHandler(webapp2.RequestHandler):
    def get(self):
      logging.info("-----------Hello GET-------------")          #logging GET request
      template = JINJA_ENVIRONMENT.get_template('templates/login.html')
      self.response.write(template.render({'title': 'LOGIN'}))
    def post(self):
      logging.info("-----------Hello POST------------")          #logging POST request
      idIN = self.request.get('name')     #get the login name
      passIN = self.request.get('pw')       #get the login password
      if idIN == "Colleen" and passIN == "pass":
        template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
        self.response.write(template.render({'title': 'LOGGED IN'}))
      else:
        logging.info("Incorrect name: " + idIN)
        logging.info("Incorrect password: " + passIN) 
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'LOGIN', 'errormessage':'Bad credentials. Try again.'}))


app = webapp2.WSGIApplication([
    ('/login', loginHandler),
    ('/index', firstHandler),
    ('/.*', firstHandler)
    # ('/hobby', FamilyHandler),
    # ('/food' , FoodHandler)
], debug=True)
