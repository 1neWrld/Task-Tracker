import datetime


class Task:
    def __init__(self,task_id,description, status, created_at, updated_at = 'pending'):

        self.task_id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    # (dictionary literal) dict containing mutable key-value pairs(key id : value self.task_id)
    def to_dict(self):
        return\
        {
            'id': self.task_id,
            'description': self.description,
            'status': self.status,

             #convert dates to string format
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }


    @classmethod # a method that belongs to the class and not an instance of the class. Class itself as 1st argument
    def from_dict(cls, data):
        return cls(
            task_id = data['id'],
            description = data['description'],
            status = data['status'],
            #convert back to datetime
            created_at = datetime.datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S'),
            updated_at = datetime.datetime.strptime(data['updated_at'], '%Y-%m-%d %H:%M:%S')
        )