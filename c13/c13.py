#!/usr/bin/env python3

# # In this challenge source code you can find this line: phone that <remote /> evil. And 
# # also when you click the number 5 it appears some xml with 105 error.
# # From these two pieces you have to guess that this is referring to remote procedure call 
# # over xml, and after a quick search python has an implementation in the stl, so here we go.
import xmlrpc.client
s = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
s.system.listMethods()
# # Let's see what does phone do...
s.system.methodHelp('phone')
# # So maybe we try calling the infamous Bert...
s.phone('Bert')