# Book review app project

In this project I've learned how to:

- query all entries with query.all(), or fetch an entry based on the value of its primary key with query.get(id). 
- retrieve related objects by using the attributes instantiated with db.relationship() in your model (Reader.query.get(123).reviews.all()).
- use filter and filter_by to select database entries based on some criterion (for example, Book.query.filter(Book.year = 2020).all()).
- filter database entries by analyzing the patterns in their column values (for example, emails = Reader.query.filter(Reader.email.like('%.%@%')).all()).
- add new entries to a database, or how to rollback in case the transaction had erroneous entries.
- update existing entries in the database (for example, Reader.query.get(3).email = “new_email@example.com”).
- remove database entries (for example, db.session.delete(Reader.query.get(753))).
- combine databases with your web application’s templates (views).

To accomplish this I created:
- `app.py` using Flask-SQLAlchemy created model representing a table schema that by declaring classes. 
- `app_data.py` created database entries as instances of the declared Flask-SQLAlchemy classes. 
- `routes.py` the routes for the Flask app are declared.
- `playground.py` I tried different reading, updating and deleting queries, that can be performed on the database. 