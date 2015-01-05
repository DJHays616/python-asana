# This file is automatically generated by generate.py using api.json

class _Attachments:
    def __init__(self, session=None):
        self.session = session

    def find_by_task(self, task_id, params={}):
        path = '/tasks/%d/attachments' % (task_id)
        return self.session.get(path, params)

    def find_by_task_iterator(self, task_id, params={}):
        path = '/tasks/%d/attachments' % (task_id)
        return self.session.get_iterator(path, params)

    def find_by_id(self, attachment_id, params={}):
        path = '/attachments/%d' % (attachment_id)
        return self.session.get(path, params)