
class Task:
    def __init__(self,task_id,description, status, created_at, updated_at = 'pending'):

        self.task_id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return\
        {
            'id': self.task_id,
            'description': self.description,
            'status': self.status,

             #convert dates to string format
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
