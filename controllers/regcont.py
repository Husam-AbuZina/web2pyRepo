



@auth.requires_login()
def add_user():
    auth.settings.expiration=1800
    name  = request.vars['name']
    email = request.vars['email']
    return locals()



@auth.requires_login()
def list_students():
    auth.settings.expiration=1800

    students = db.executesql("SELECT * FROM students", as_dict=True)

    return dict(students=students)

@auth.requires_login()
def addStudents():
    auth.settings.expiration=1800

    if request.vars['firstName']:
        first_name = request.vars['firstName']
        last_name = request.vars['lastName']
        email = request.vars['email']

        db.executesql("INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)", placeholders=(first_name,last_name, email))
    else:
        redirect(URL('addStudents'))

    return locals()



# @auth.requires_login()
# def details():
#     if request.vars['id']:
#         id = request.vars['id']
#         students = db.executesql("SELECT * FROM students WHERE id=" + id, as_dict=True)
#     return dict(students=students[0], students=students)


@auth.requires_login()
def details():
    auth.settings.expiration=1800
    students = None
    if 'id' in request.vars:
        id = request.vars['id']
        students = db.executesql("SELECT * FROM students WHERE id = %s" % id, as_dict=True)
    return dict(students=students[0] if students else None)


@auth.requires_login()
def delete():

    if request.vars['id']:
        id = request.vars['id']

        db.executesql("DELETE FROM students WHERE id=" + id)
    
    redirect(URL('list_students'))

@auth.requires_login()
def schedules():
    auth.settings.expiration=1800

    grid = SQLFORM.grid(db.courseschedules, csv=False)

    return dict(grid=grid)


@auth.requires_login()
def coursesList():
    auth.settings.expiration=900 #form web2py
    return locals()

@auth.requires_login()
def addSchedule():
    auth.settings.expiration=1800
    form = SQLFORM.grid(db.courseschedules)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

@auth.requires_login()
def rooms():
    auth.settings.expiration=1800
    form = SQLFORM.grid(db.courseschedules)

    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

@auth.requires_login()
def courses():
    auth.settings.expiration=1800
    grid = SQLFORM.grid(db.courses)
    return dict(grid=grid)

@auth.requires_login()
def addCourse():

    form = SQLFORM.grid(db.courses)

    if form.process().accepted:
        response.flash = ' the form accepted'
    elif form.errors:
        response.flash = ' the form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

@auth.requires_login()
def showCourse():
    auth.settings.expiration=1800
    courses=db(db.courses).select()
    if request.post_vars:   
        courseCode=int(request.post_vars.CourseId)
        db.studentsreg.insert(Courseid=courseCode,Studentid=auth.user.id)
    # grid = db(db.courses.scheduled == db.courseschedules.id).select(db.courses.code,
    # db.courses.name, db.courses.instructor, db.courses.capacity, db.courseschedules.days,
    # db.courseschedules.startTime, db.courseschedules.endTime, db.courseschedules.RoomNo)
    # SQLFORM.grid(grid)
    grid=SQLFORM.grid(db.courses,
    editable=True,
    exportclasses = None,
    csv=False,
    create=False
)
    return locals()

@auth.requires_login()
def courseSchedules():
    auth.settings.expiration=1800  #***********  For Security Reasons, The Bank for Example *******************************
    grid = SQLFORM.grid(db.courses.scheduled==db.courseschedules.id,
    fields=[db.courses.name,db.courses.code,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
    db.courseschedules.days,db.courseschedules.startTime,db.courseschedules.endTime,
    db.courseschedules.RoomNo],
    csv=False,editable= False,deletable = False,details=False, create= False,
    selectable = lambda ids: redirect(URL('regcont','courseSchedules',vars=dict(id=ids))))
    return dict(grid = grid)






@auth.requires_login()
def studentSchedules():
    auth.settings.expiration=1800
    grid = SQLFORM.grid((db.courses.code==db.studentsreg.courseid) and (db.students.id==db.studentsreg.studentid),
    fields=[db.students.id,db.courses.code,db.courses.name,db.courses.instructor,db.courses.prerequisites,db.courses.capacity,
    db.courseschedules.days,db.courseschedules.startTime,db.courseschedules.endTime,db.courseschedules.RoomNo],
    csv=False,editable= False,deletable=False,details=False, create= False)
    selectable = lambda ids: redirect(URL('regcont','studentSchedules',vars=dict(id=ids)))
    return dict(grid=grid)

           
auth.settings.expiration=1800
@auth.requires_login()
def coursesList():
    auth.settings.expiration=1800
    return locals()

def get_session():
    session.auth_user.name=auth_user.name
    return locals()