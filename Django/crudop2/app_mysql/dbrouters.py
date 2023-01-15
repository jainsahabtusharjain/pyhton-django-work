from .models import Student1


# class Student1DBRouter:
#     route_app_labels = {'app_mysql'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'Student1'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'Student1'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#            return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'Student1'
#         return None

class Student1DBRouter:
    def db_for_read (self, model, **hints):
        if (model == Student1):
            # your model name as in settings.py/DATABASES
            return 'Student1'
        return None
    
    def db_for_write (self, model, **hints):
        if (model == Student1):
            # your model name as in settings.py/DATABASES
            return 'Student1'
        return None