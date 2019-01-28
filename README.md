# Use flask-sqlalchemy with MySQL
## Connect Database
```py
setting.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:0933822291@localhost:3306/members'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

manage.py
@manager.shell
def make_shell_context():
    return dict(app = app, Role = Role, User = User)
```

## 執行程式
```sh
python manage.py shell
```

## Create All Table
```sh
>>> from setting import db
>>> db.create_all()
```

## Insert
```sh
>>> from setting import db

# Single
>>> db.session.add(Role(name='Admin'))
>>> db.session.commit()
>>> db.session.add(Role(name='Moderator'))
>>> db.session.add(Role(name='User'))
>>> db.session.commit()

# Multi
>>> db.session.add_all([User(username='John', role_id=1), User(username='Susan', role_id=3), User(username='David', role_id=3)])
>>> db.session.commit()
```

## Update
```sh
>>> from setting import db
>>> admin = Role.query.filter_by(name='Admin').first()
>>> admin.name = 'Administrator'
>>> db.session.commit()
```

## Delete
```sh
>>> from setting import db
>>> mod = Role.query.filter_by(name='Moderator').first()
>>> db.session.delete(mod)
>>> db.session.commit()
```

## Query Table
### Import
```sh
>>> from setting import db
```

### All Data
```sh
>>> Role.query.all()
[<Role 'Administrator'>, <Role 'User'>]

>>> User.query.all()
[<User 'john', Role id 1>, <User 'Susan', Role id 3>, <User 'David', Role id 3>]
```

### Single Condition
```sh
>>> Role.query.filter_by(name='Administrator').first()
<Role 'Administrator'>

>>> User.query.filter_by(role_id=3).all()
[<User 'Susan', Role id 3>, <User 'David', Role id 3>]

>>> User.query.filter_by(role_id=3).first()
<User 'Susan', Role id 3>
```

### Multi Condition
```sh
>>> User.query.filter_by(role_id=3,username='Susan').first()
<User 'Susan', Role id 3>

>>> User.query.filter_by(role_id=3,username='Susan').all()
[<User 'Susan',Role id 3>]
```

### AVG()
```sh
>>> from django.db.models import Avg
>>> User.query.aggregate(Avg(User.id))
[(Decimal('2.0000'),)]

>>> User.query.aggregate(Avg(User.role_id))
[(Decimal('2.3333'),)]
```

### SUM()
```sh
>>> from django.db.models import Sum
>>> User.query.aggregate(Sum('User.id'))
[(Decimal('6'),)]

>>> User.query.aggregate(Sum('User.role_id'))
[(Decimal('7'),)]
```

### COUNT()
```sh
>>> User.query.filter_by(role_id=3,username='Susan').count()
1

>>> User.query.filter_by(role_id=3).count()
2

>>> User.query.count()
3
```

### GROUP BY
```sh
>>> User.query.group_by(User.role_id).all()
[<User 'John', Role id 1>, <User 'Susan', Role id 3>]
```

### ORDER BY
```sh
# ASC
>>> User.query.order_by(User.role_id).all()
[<User 'John', Role id 1>, <User 'Susan', Role id 3>, <User 'David', Role id 3>]

# DESC
>>> User.query.order_by(User.role_id.desc()).all()
[<User 'Susan', Role id 3>, <User 'David', Role id 3>, <User 'John', Role id 1>]
```

### LIMIT
```sh
>>> User.query.all()
[<User 'John', Role id 1>, <User 'Susan', Role id 3>, <User 'David', Role id 3>]

# limit 1
>>> User.query.limit(1).all()
[<User 'John', Role id 1>]

# limit 2,1
>>> User.query.limit(1).offset(2).all()
[<User 'David', Role id 3>]

>>> User.query.filter_by(role_id=3).all()
[<User 'Susan', Role id 3>, <User 'David', Role id 3>]

# limit 1
>>> User.query.filter_by(role_id=3).limit(1).all()
[<User 'Susan', Role id 3>]

# limit 1,1
>>> User.query.filter_by(role_id=3).limit(1).offset(1).all()
[<User 'David', Role id 3>]
```

## Flask-SQLAlchemy transfer to SQL
```sh
>>> from setting import db
>>> User.query.all()
[<User 'John', Role id 1>, <User 'Susan', Role id 3>, <User 'David', Role id 3>]

>>> str(User.query)
'SELECT user.id AS user_id, user.username AS user_username, user.role_id AS user_role_id \nFROM user'

>>> User.query.limit(1).all()
[<User 'John', Role id 1>]

>>> str(User.query.limit(1))
'SELECT user.id AS user_id, user.username AS user_username, user.role_id AS user_role_id \nFROM user \n LIMIT %(param_1)s'

>>> User.query.limit(1).offset(2).all()
[<User 'David', Role id 3>]

>>> str(User.query.limit(1).offset(2))
'SELECT user.id AS user_id, user.username AS user_username, user.role_id AS user_role_id \nFROM user \n LIMIT %(param_1)s, %(param_2)s'
```