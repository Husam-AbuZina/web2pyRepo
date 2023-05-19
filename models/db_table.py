import datetime 

db.define_table('courses' ,
    Field('code' , 'integer' , required= True , notnull=True) , 
    Field('name' ,'string' ) ,
    Field('description', 'string') , 
    Field('prerequisites','references courses' , requires= IS_IN_DB(db, 'courses.code','%(name)s')) , # fixed closing parenthesis
    Field('instructor', 'string'), 
    Field('capacity', 'string'), 
    Field('scheduled' , 'integer' ,'references courseschedules' , requires=IS_IN_DB(db,'courseschedules.id' ,'%(days)s-%(startTime)s-%(endTime)s')) ,
    primarykey=['code'], 
) 

db.define_table("rooms" ,
    Field("code" ,"string" ,required= True , notnull=True ) , 
    primarykey=['code']
)

db.define_table("courseschedules" ,
    Field("id" , "integer" , required= True , notnull= True) , 
    Field("days","string"),
    Field("startTime", "date"),
    Field("endTime", "date"), 
    Field("RoomNo","reference rooms" , requires =IS_IN_DB(db, "rooms.code",'%(code)s')) ,
    primarykey=['id']
)
db.define_table("students" ,
    Field("id" , "integer" , required= True , notnull= True) , 
    Field("last_name","string"),
    Field("first_name", "string"),
    Field("email", "string"), 
    Field("password","string") ,
    Field("registration_key", "string"),
    Field("rest_registration_key", "string"),
    Field("registration_id", "string"),
    primarykey=['id']
)

db.define_table("studentsreg" ,
    Field("id" , "integer" , required= True , notnull= True) , 
    Field("courseid","integer", requires =IS_IN_DB(db, "courses.code",'%(code)s')),
    Field("studentid", "integer", requires =IS_IN_DB(db, "students.id",'%(id)s')),
    primarykey=['id']

)


