# Requests
# All right! Let's see if you can make that request to http://placekitten.com/ all on your lonesome.
#
# Instructions
# You need to do two things:
#
# On line 4, create a variable called website and set it equal to calling the urlopen method on "http://placekitten.com/" (no need for the "www"!)
# On line 5, call the read method on website and save the result in a new variable called kittens.
# The last line will then take the full kittens response you saved and display part of it.


from urllib2 import urlopen

# Add your code here!
website = urlopen('http://placekitten.com')
kittens = website.read()

print kittens[559:1000]	
