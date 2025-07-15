#string is store sequence of characters.
a =  "hello friends "
b = 'everyone'
c = """people"""
# concatenation.  
print (a+" "+b+" "+c )
# find length { len (variable)} .
print ("lenght of a ",len(a),"lenght of b",len(b),"lenght of c",len(c)) # not ignore space & special characters
#index 
print (a[0],b[4],c[3])
# slicing str [staring index : ending index] . always start 0,1,2,3 & and so on.
print ( a [0:len(a)] )
print ( b [7:len(b)] )
print ( c [4:len(c)] )
# negative indexing always start -1,-2,-3 & so on.
print (a[-5:len(a)])
# str.endwith ("er") .
print (a.endswith("lo"))
# str.capitalize () .
print (b.capitalize(),a.capitalize(),c.capitalize())
# str.replace(["old":"new"])
d = a.replace ( "hello","asslam-u-aliakum"  )
a = d 
print (a)
# str.find(word) only for time exits . 
print ( b.find(c))
# str.count . 
print (a.count("e"))
print (b.count("y"))
print (c.count("p"))