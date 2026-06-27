#seed.py --> jaee k shoam question haro tarahi mikonid

from database import Base, engine, get_db

#tabe shoamtooye crud minevsii inja improt mishe
from crud import create_user, create_question, add_choice, list_questions

questions=[
    {
         'text': 'Is python a case-sensitive language?',
         'choice': ['yes', 'No', 'Maybe' ] 
    }
    ,
    {
         'text': 'When was Python created?',
         'choice': ['1998', '1985', '1991' ] 
    }
    ,
    {
         'text': 'How many numeric data types does python have?',
         'choice':['5', '3', '7' ] 
    }
    ,
    {
         'text': 'Where is python headquarters?',
         'choice':['USA', 'Germany', 'Switzerland' ] 
    }
]


print('Creating tables...')
#Create tables --> 
Base.metadata.create_all(engine)


print('Tables created successfully')
#database shoam toye yek zarfe
db = get_db()

print('Creating questions...')
#question1 --
#javdalamo por mikonam
q1 = create_question(db, text='manie fahmidan chis?')

add_choice(db,q1, text='fahmidan',is_correct=True)
add_choice(db,q1,text='shenidan', is_correct=False)
add_choice(db,q1,text='khordan', is_correct=False)


#daste toe harchi mikhay besaz bara khodet
q2 = create_question(db, text='cheghadr in mozo ro fahmidim?')

#3 ta gozine
add_choice(db,q2, text='hichi',is_correct=False)
add_choice(db,q2, text='hamasho',is_correct=False)
add_choice(db,q2, text='hododan',is_correct=True)


#python seed.py
print('Questions created successfully')
print('finalizing...')
