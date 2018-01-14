# this file contains all the essential functions for creating and manipulating the database.

import sqlite3

def create_table():
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
	conn.commit()
	conn.close()


def add_entry(title, author, year, isbn):
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)',(title,author,year,isbn)) # NULL so that python itself will update the id everytime we make a new entry
	conn.commit()
	conn.close()
	view()


def view_all():
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM book')
	rows=cur.fetchall()
	conn.close()
	return rows


def search_entry(title='', author='', year='', isbn=''): # default '' is passed to all arguments
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?',(title, author, year, isbn)) #remember to give the variables in the same order as mentioned in your query
	rows=cur.fetchall()
	conn.close()
	return rows


def update(id, title, author, year, isbn):
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE id=?',(title, author, year, isbn, id))
	conn.commit()
	conn.close()


def delete(id):
	conn=sqlite3.connect('books.db')
	cur=conn.cursor()
	cur.execute('DELETE FROM book WHERE id=?',(id,))  # don't forget to place a comma after id
	conn.commit()
	conn.close()


create_table()


