#!/usr/bin/python
#coding=utf-8

from model import Person
import view

def showAll():
	person_in_db = Person.getAll()
	return view.showAllView(person_in_db)
	
def start():
	view.startView()
	
	input = raw_input()
	if input == 'y':
		return showAll()
	else:
		return view.endView()
		
if __name__ == '__main__':
	start()
