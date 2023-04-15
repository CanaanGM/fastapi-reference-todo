> an ORM 


# how to use

### installl
```bash
pip install alembic
```

### use

```bash
alembic init 
```
> this will create 2 files:

1. alembic 
- ![[Pasted image 20230415041125.png]]
- ![[Pasted image 20230415041137.png]]

the folder has all the migrations in the versions

in the `ini` file, u need to give it the connection string(s) for teh DB

- ![[Pasted image 20230415041256.png]]
- in the `env.py` inside the folder:
	- add this and customize it so it can access ur models
```python
import sys
sys.path.append("howver many up it takes")
example = sys.path.append("..")
```

- ![[Pasted image 20230415041614.png]]
### create a revision (migration)
```bash
alembic revision -m <name>
alembic revision -m "create revisions" <-- example
```
- this will create an empty revision
	- ![[Pasted image 20230415041813.png]]
- inside it will be 2 methods 
	- upgrade -> update's thy model
	- downgrade -> the opposite, rolls back the update
- modify the `upgrade` method:
	- ![[Pasted image 20230415041958.png]]
```bash
alembic upgrade <revision>
alembic upgrade  6a614d204c53 <-- example

alembic downgrade -1 <-- will roll back
```


#### create table
- create a new revision
	- `alembic revision -m "name"`
add the code for creating 
```python
def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=True),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False),
    )
 def downgrade() -> None:
    op.drop_table('address')
```

- apply the migration
	- `alembic upgrade <rev id>`

#### alter with a constraint
```python
def upgrade() -> None:
    op.add_column(
    'users',
     sa.Column(
     'address_id', 
     sa.Integer(), 
     nullable=True
     ))
    op.create_foreign_key(
    'address_users_fk', 
    'users', 
    'address', 
    ['address_id'], 
    ['id'], 
    ondelete="CASCADE"
    )

def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
```

### dont forget to alter ur models!
```python
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name= Column(String)
    last_name= Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    phone_number = Column(Integer)
    todos = relationship("Todo", back_populates="owner")
    address_id = Column(Integer,ForeignKey('address_id'), nullable=True)
    address = relationship("Address", back_populates='user_address')

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, index=True)
    address1 = Column('address1', String(), nullable=False)
    address2 = Column('address2', String(), nullable=False)
    city = Column('city', String(), nullable=False)
    state = Column('state', String(), nullable=True)
    country = Column('country', String(), nullable=False)
    postalcode = Column('postalcode', String(), nullable=False)
    user_address = relationship("User", back_populates='address')
```

#python-orm