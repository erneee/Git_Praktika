from git_model import Klientas, Produktai, engine, sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_user(f_name, l_name, email):
    new_user = Klientas(f_name=f_name, l_name=l_name, email=email)
    session.add(new_user)
    session.commit()
    print("User added successfully.")

def view_users():
    users = session.query(Klientas).all()
    for user in users:
        print(f"User ID: {user.id}, Name: {user.f_name} {user.l_name}, Email: {user.email}")