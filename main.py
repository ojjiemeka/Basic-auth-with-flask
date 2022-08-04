from website import create_app

app = create_app()

ENV = 'dev'

# This is a conditional statement that checks if the environment is set to development. If it is, then
# it will run the app in debug mode and set the database URI to the local database. If it is not, then
# it will run the app in production mode and set the database URI to the production database.
if ENV == 'dev':
    app.run(debug = True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgress:root@localhost/sample'
    
else:
    app.run(debug = False)
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating a database object.
db= SQLAlchemy(app)


# Running the app.
if __name__ == '__main__':
    # app.run(debug = True)
    app.run()