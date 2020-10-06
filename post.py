from datetime import datetime, date


class Post:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.fecha = date

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'date': self.fecha
        }

    def __repr__(self):
        return '{} by {} the {}'.format(self.title, self.content, datetime.strptime(self.fecha, '%Y-%m-%d %H:%M:%S'), 'ok' if(datetime.strptime(self.fecha, '%Y-%m-%d %H:%M:%S') == '%Y-%m-%d %H:%M:%S') else 'error')
