import os
import jinja2
import json
import urllib2
import endpoints
import webapp2
from webapp2_extras import sessions
from protorpc import message_types, remote
from google.appengine.api import mail, users



###################################################################################################
class BaseHandler(webapp2.RequestHandler):

    #----------------------------------------------------------------------------------------------
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)


    @webapp2.cached_property
    #----------------------------------------------------------------------------------------------
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()



###################################################################################################
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



###################################################################################################
class MainPage(BaseHandler):

    #----------------------------------------------------------------------------------------------
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.jinja2')
        self.response.write(template.render({}))

