from library.stigma.helper import eventAttach
from application.controller.resources.Scenario import Scenario
from application.controller.resources.Option import Option


class Scenario(object):
    _script = Scenario()
    _option = Option()
    
    def conversation(self, part, line):
        if isinstance(part, str) and isinstance(line, int):
            conversation = getattr(self._script, part)
            return conversation[line]
        
    def option(self, option, bound):
        if isinstance(option, basestring):
            decision = {}
            dialog   = tuple()
            opt_button = getattr(self._option, option)

            if option == 'ask0':
                dialog = (lambda parameter : bound(['approach', -1], 'option'),
                          lambda parameter : bound(['ignore'  , -1], 'option'))

            elif option == 'ask1':
                dialog = (lambda parameter : bound(['place' , -1], 'option'),
                          lambda parameter : bound(['stigma', -1], 'option'),
                          lambda parameter : bound(['enough', -1], 'option'))

            elif option == 'ask2':
                dialog = (lambda parameter : bound(['framework', -1], 'option'),
                          lambda parameter : bound(['demo'     , -1], 'option'),
                          lambda parameter : bound(['escape'   , -1], 'option'))

            elif option == 'ask3':
                dialog = (lambda parameter : bound(['okay'  , -1], 'option'),
                          lambda parameter : bound(['cannot', -1], 'option'))

            if opt_button is not None:
                for k, v in enumerate(opt_button):
                    decision.update({v.replace(' ' , '_').lower() : eventAttach(dialog[k])})

                return decision