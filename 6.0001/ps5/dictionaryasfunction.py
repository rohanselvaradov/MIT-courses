# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:48:37 2020

@author: Rohan
"""


class Age(object):
    def __init__(self, age):
        self.age = int(age)
    def age_in_a_year(self):
        self.new_age = self.age + 1
        print(self.new_age)
    def evaluate(self, other_age):
        return self.age == int(other_age)
    
class Name(object):
    def __init__(self, forename):
        self.forename = forename
    def initials(self):
        return self.forename[0]
    def evaluate(self, other_initials):
        return self.initials() == other_initials

def text_to_function(text):
    dictionary = {"AGE":Age, "NAME":Name} 
    text = text.split(",")
    print(dictionary[text[1]](text[2]).evaluate(text[3]))
    
text_to_function("")



{'t1': <__main__.TitleTrigger object at 0x000001C86E52A408>, 't2': <__main__.DescriptionTrigger object at 0x000001C86E52A388>, 't3': <__main__.DescriptionTrigger object at 0x000001C86E52A4C8>, 't4': <__main__.AfterTrigger object at 0x000001C86E52A588>, 't5': <__main__.AndTrigger object at 0x000001C86E52A648>, 't6': <__main__.AndTrigger object at 0x000001C86E535708>}