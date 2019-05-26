day=3
>>> mon=2
>>> year=2019
>>> print "exam begins in %i /%i /%i"%(day,mon,year)
exam begins in 3 /2 /2019
>>> mon=june
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'june' is not defined
>>> mon="june"
>>> print "exam begins in %i /%s /%i"%(day,mon,year)
exam begins in 3 /june /2019

