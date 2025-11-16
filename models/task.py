
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
            'create_at': self.created_at,
            'updated_at': self.updated_at
        }
