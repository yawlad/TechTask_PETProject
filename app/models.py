import peewee
from db import *

class Vacancy(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    salary = peewee.IntegerField()
    work_type = peewee.CharField()
    
    class Meta:
        database = DATABASE_OBJ
    
class Skill(peewee.Model):
    name = peewee.CharField()
    owner = peewee.ForeignKeyField(Vacancy)
    
    class Meta:
        database = DATABASE_OBJ
