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
from google.appengine.api import mail

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
        if path == "/about":
            self.response.write(template.render({'title': 'ABOUT'}))
        if path == "/work":
            self.response.write(template.render({'title': 'WORK'}))
        if path == "/personal":
            self.response.write(template.render({'title': 'PERSONAL'}))

# class emailHandler(webapp2.RequestHandler):
#     def get(self):
#         logging.info("-----------Hello GET-------------") 
#         template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
#         self.response.write(template.render({'title': 'CONTACT'}))
#     def post(self):

class emailHandler(webapp2.RequestHandler):
    def get(self):
      logging.info("-----------Hello GET-------------")          #logging GET request
      template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
      self.response.write(template.render({'title': 'CONTACT'}))
    def post(self):
      logging.info("-----------Hello POST------------")          #logging POST request
      nameIN = self.request.get('name')  
      emailIN = self.request.get('email')     
      messageIN = self.request.get('message')  
      message = mail.EmailMessage()
      message.sender = emailIN
      message.to = "So Yun <syjin@umich.edu>"
      message.body = messageIN
      message.send()
      template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
      self.response.write(template.render({'title': 'CONTACT', 'sentmessage':'Your message has been sent. Thank you!'}))


app = webapp2.WSGIApplication([
    ('/contact', emailHandler),
    ('/index', firstHandler),
    ('/.*', firstHandler)
], debug=True)
