from .models import Student2

class Student2DBRouter:
    def db_for_read (self, model, **hints):
        if (model == Student2):
            # your model name as in settings.py/DATABASES
            return 'Student2'
        return None
    
    def db_for_write (self, model, **hints):
        if (model == Student2):
            # your model name as in settings.py/DATABASES
            return 'Student2'
        return None