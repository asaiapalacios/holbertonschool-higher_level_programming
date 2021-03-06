'''Script for managing the database'''

from models import *

#Import module to use sys.argv (list of command-line args passed to script)
import sys

#If script is not executed with arguments, print the following in console
if (len(sys.argv) < 2):
    print "Please enter an action"

#'''First argument is the action'''

#Create tables for all models via peewee if first arg is 'create'
else:
    if (sys.argv[1] == 'create'):
        try:
            School.create_table()
        except peewee.OperationalError:
            pass

        try:
            Batch.create_table()
        except peewee.OperationalError:
            pass

        try:
            User.create_table()
        except peewee.OperationalError:
            pass

        try:
            Student.create_table()
        except peewee.OperationalError:
            pass

    #Implement print action
    elif(sys.argv[1] == 'print'):
        if sys.argv[2] == "school":
            for record in School.select():
                print record
        elif sys.argv[2] == "batch":
            for record in Batch.select():
                print record
        elif sys.argv[2] == "user":
            for record in User.select():
                print record
        elif sys.argv[2] == "student":
            for record in Student.select():
                print record

    #Implement insert action
    elif sys.argv[1] == 'insert':
        if sys.argv[2] == "school":
            school_row = School.create(name=sys.argv[3]) #Arguments=values for creating an object
            print "New school: " + str(school_row)
        elif sys.argv[2] == "batch":
            batch_row = Batch.create(school=sys.argv[3], name=sys.argv[4])
            print "New batch: " + str(batch_row)
        elif sys.argv[2] == "user":
            user_row = User.create(first_name=sys.argv[3], last_name=sys.argv[4], age=sys.argv[5])
            #Should I include a print statement for user?
        elif sys.argv[2] == "student":
            if (len(sys.argv) == 6):
                student_row = Student.create(batch=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5])
            if (len(sys.argv) == 7):
                student_row = Student.create(batch=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6])
            print "New student: " + str(student_row)
        else:
            print "hi"

    #Implement delete action
    elif sys.argv[1] == 'delete':
        if sys.argv[2] == "school":
            try:
                school_user = School.get(School.id == sys.argv[3])
                print "Delete: " + str(school_user)
                school_user.delete_instance()
            except:
                print "Nothing to delete"

        elif sys.argv[2] == "batch":
            try:
                batch_user = Batch.get(Batch.id == sys.argv[3])
                print "Delete: " + str(batch_user)
                batch_user.delete_instance()
            except:
                print "Nothing to delete"

        elif sys.argv[2] == "user":
            try:
                user = User.get(User.id == sys.argv[3])
                print "Delete: " + str(user)
                user.delete_instance()
            except:
                print "Nothing to delete"

        elif sys.argv[2] == "student":
            try:
                student_user = Student.get(Student.id == sys.argv[3])
                print "Delete: " + str(student_user)
                student_user.delete_instance()
            except:
                print "Nothing to delete"

'''First argument is the action: Task 0'''
#if sys.argv[1] == 'create':
#    print 'create'
#elif sys.argv[1] == 'print':
#    print 'print'
#elif sys.argv[1] == 'insert':
#    print 'insert'
#elif sys.argv[1] == 'delete':
#    print 'delete'

#If first argument is not part of the list
#else:
#    print "Undefined action", sys.argv[1]
