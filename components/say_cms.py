# -*- coding: utf-8 -*-
from meya import Component


class HelloWorld(Component):

    def start(self):
        value, entity = self.cms.get("general", "about")
        message = self.create_message(text=value)
        return self.respond(message=message, action="next")
