import json

from application.controller.serialization import Files


class Serialize(Files.Directory):
    def __init__(self):
        #TODO CHANGES : FIXED, COMPLETED
        '''
        this class is used to manage the serialization state for the application game.
        '''
        super(Serialize, self).__init__()

    @property
    def list(self):
        #TODO CHANGES : FIXED, COMPLETED
        '''
        this property will show the list about the serialization data has been stored.
        '''
        data_save = self.listFiles()
        save_list = []
        character = {}
        for k, v in data_save.items():
            try:
                open_save  = open(v)
                data       = json.load(open_save)
                data       = data['save_%s' %k]
                background = str(data['background'])
                character  = {}

                if data['character'] != 'None':
                    for y, z in data['character'].items():
                        character.update({str(y) : z})
                else:
                    character = None

                if data['background'] == 'None':
                    background = None
            except IOError as E:
                raise E
            else:
                open_save.close()

            save_list.append((k, str(data['part']), int(data['line']), background, character))

        return save_list

    def save(self, **kwargs):
        #TODO CHANGES : FIXED, COMPLETED
        '''
        this method is used to store serialize for application game state, after it stored
        user can open any state based on it.
        '''

        name  = '{}.json'.format(kwargs['slot'])
        key   = 'save_%s' %kwargs['slot']
        write = {key : {}}

        for k, v in kwargs['write'][key].items():
            if k == 'part' or k == 'line':
                write[key].update({k : str(v)})

            elif k == 'background' or k == 'character':
                if v is None:
                    write[key].update({k : 'None'})

                else:
                    write[key].update({k : v})

        write = str(write).replace('\'', '"')

        return self.dumpFiles(write, name)