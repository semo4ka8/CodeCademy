from app import db, Book, Reader, Review, Annotation
import app_data

#query all the readers from the Reader model
readers = Reader.query.all()
print(readers)

#get an entry with id = 123
reader = Reader.query.get(123)
print(reader)

#reader with id = 450
reader = Reader.query.get(450)
print("Reader with id = ", reader.id, "is called", reader.name)

#Loop through all the readers and print their e-mails
print("\nPrint all the readers in a loop:")
for reader in readers:
    print(reader.email)


print("\nCheckpoint1: fetching all the reviews")
reviews = Review.query.all()

print("\nCheckpoint2: looping through all the reviews and printing their text")
for review in reviews:
    print(review.text)


print("\nCheckpoint3: fetching a book with id = 13 using the get() function")
book_1 = Book.query.get(12)
print(book_1)


#Fetching 'many' objects
reader = Reader.query.get(123) #fetch a reader with id = 123
reviews_123 = reader.reviews.all() #fetch all reviews made by reader wiith id = 123
[print(review.id) for review in reviews_123]


#fetching 'one' object
review = Review.query.get(111) #fetch a review with id = 111
reviewer_111 = review.reviewer #get the reviewer for review with id = 111. There's only one!
print("The author of [", review, "] is", reviewer_111)


print("\nCheckpoint 4: fetch all the reviews made for a book with id = 13.")
book_13 = Book.query.get(13).reviews.all()
[print(book.id) for book in book_13]

print("\nCheckpoint 5: fetch all the annotations made for a book with id = 19.")
book_19_an = Book.query.get(19).annotations.all()
[print(annotation.id) for annotation in book_19_an]

print("\nCheckpoint 5: fetch the reader who owns the annotation with `id = 331.`")
author_331 = Annotation.query.get(331).author
print(author_331)

#select books from the year 2020
book_2020 = Book.query.filter(Book.year == 2020).all()
print("All the suggested books in the year 2020:")
[print(book) for book in book_2020]

#instead of all books suggested in 2020, fetch only the first one
book_2020_first = Book.query.filter(Book.year == 2020).first()
print("\nThe first book fetched from the year 2020: ", book_2020_first)

#you can specify multiple criteria for filtering
rev_3_boook13 = Review.query.filter(Review.stars <= 3, Review.book_id == 13).all()
print("\nThe review of 3 stars or lower written for a book with id = 13: ", rev_3_boook13)

#Checkpoint 6: fetching all the readers with "Adams" surname
adams = Reader.query.filter(Reader.surname == 'Adams').all()
[print(person) for person in adams]

#Checkpoint 7: fetching the first book dating prior to the year 2019
book_pre2019 = Book.query.filter(Book.year <= 2019).first()
print(book_pre2019)

#retrieve all reader with .edu e-mails
education = Reader.query.filter(Reader.email.endswith('edu')).all()
print(education)

#retrieve all readers with e-mails that contain a . before the @ symbol
emails = Reader.query.filter(Reader.email.like('%.%@%')).all()
print("\nReaders with e-mails having a . before the @ symbol:")
for e in emails:
    print(e.email)

#order all books by year
ordered_books = Book.query.order_by(Book.year).all()
print("\nBooks ordered by year:")
for book in ordered_books:
    print(book.title, book.year)

print("\nCheckpoint 8: your code here below:")
s_names = Reader.query.filter(Reader.surname.endswith("s")).all()
print(s_names)

print("\nCheckpoint 9: your code here below:")
sample_emails = Reader.query.filter(Reader.email.like('%@sample%')).all()
print(sample_emails)

print("\nCheckpoint 10: your code here below:")
ordered_reviews = Review.query.order_by(Review.stars).all()
print(ordered_reviews)

#creating new readers
new_reader1 = Reader(name = "Nova", surname = "Yeni", email = "nova.yeni@sample.com")
new_reader2 = Reader(name = "Nova", surname = "Yuni", email = "nova.yeni@sample.com")
new_reader3 = Reader(name = "Tom", surname = "Grey", email = "tom.grey@example.edu")

print("Before addition: ")
for reader in Reader.query.all():
    print(reader.id, reader.email)

print("\nNote that before committing, the id of the new readers is: ", new_reader1.id, "\n")



#adding the first reader - the commit should succeed
db.session.add(new_reader1)
try:
    db.session.commit()
    print("Commit succeded.", new_reader1, "added to the database permanently. The exception was not raised.\n")
except:
    db.session.rollback()

#adding the second reader - the commit should fail because e-mails should be unique
db.session.add(new_reader2)
try:
    db.session.commit()
except Exception as ex:
    print("The commit of", new_reader2,"didn't succeed. Duplicate primary key values. We will empty the current session.\n")
    print("The error is the following:", ex)
    db.session.rollback()

#adding the third reader - the commit should succeed
db.session.add(new_reader3)
try:
    db.session.commit()
    print("Commit succeded.", new_reader3, "added to the database permanently. The exception was not raised.\n")
except Exception as ex:
    db.session.rollback()

print("\nNote that after committing, the id of the new readers is now: ", new_reader1.id, "\n")

#print all the readers after the addition, and we see nova.yeni@sample.com there, but not twice
for reader in Reader.query.all():
    print(reader.id, reader.email)
print("\nThe new readers Nova Yeni and Tom Grey are in the database. Notice that Nova Yeni doesn't appear twice.\n")

print("\nCheckpoint 11: create a new_reader:")
new_reader = Reader(name = 'Peter', surname = 'Johnson', email = 'peter.johnson@example.com')

print("\nCheckpoint 12: add the new reader to the database:")
db.session.add(new_reader)

print("\nCheckpoint 13: commit and rollback if exception is raised:")
try:
    db.session.commit()
except:
    db.session.rollback()


#fetch the reader with id = 123 and change their e-mail
reader = Reader.query.get(123)
print("Before the change:", reader) #print before the change
reader.email = "new.email@example.com"
db.session.commit()
print("After the commit:", Reader.query.get(123)) #print after the change

#rollback
reader = Reader.query.get(345)
print("Rollback example - before the change: ", reader) #print before the change
reader.email = "new.email@example.edu"
db.session.rollback()
print("Rollback example - after the rollback: ", Reader.query.get(345)) #print after the change

print("\nCheckpoint 14: use get to fetch a book entry:")
book_19 = Book.query.get(19)

print("\nCheckpoint 15: modify the month attribute to June:")
book_19.month = 'June'

print("\nCommit the change:")
db.session.commit()


#let us first print all the readers current in the database
for reader in Reader.query.all():
    print(reader)

#print all the reviews
print("\nAll the current reviews:")
for review in Review.query.all():
    print(review)

#delete reader with id = 753 (Nova Yeni, nova.yeni@example.com)
db.session.delete(Reader.query.get(753))

#print readers again to validate that the reader is indeed deleted
print("\nReaders after deleting a rader with id = 753")
for reader in Reader.query.all():
    print(reader)

#print reviews to see that all the reviews made by reader id = 753 are deleted
#print all the reviews
print("\nAll the current reviews:")
for review in Review.query.all():
    print(review)

#Checkpoint 16:
db.session.delete(Reader.query.get(123))