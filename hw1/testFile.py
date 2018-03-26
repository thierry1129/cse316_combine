
from array import  array


highest_degree = array('i',"what")

with open("Output.txt", "w") as text_file:
    text_file.write(highest_degree.tostring())

