# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('course Schedules'), False, URL('regcont', 'courseSchedules'), []),
    (T('student Schedules'), False, URL('regcont', 'studentSchedules'), []),
    (T('showCourse'), False, URL('regcont', 'showCourse'), [])

    



]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
    ]