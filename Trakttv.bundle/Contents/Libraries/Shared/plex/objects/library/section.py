from plex.core.idict import idict
from plex.objects.core.base import Property
from plex.objects.directory import Directory


class Section(Directory):
    id = Property
    uuid = Property
    path = Property('key')

    filters = Property(type=bool)
    refreshing = Property(type=bool)

    agent = Property
    scanner = Property
    language = Property

    composite = Property

    created_at = Property('createdAt', int)

    def __transform__(self):
        self.path = '/library/sections/%s' % self.key

    def all(self):
        response = self.http.get('all')

        return self.parse(response, idict({
            'MediaContainer': ('MediaContainer', idict({
                'Directory': {
                    'artist':   'Artist',
                    'show':     'Show'
                },
                'Photo': {
                    'photo':    'Photo'
                },
                'Video': {
                    'movie':    'Movie'
                }
            }))
        }))
