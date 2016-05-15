#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

"""
*Disregarding a few changes, the ExtremeScores_helper() function and the
ExtremeScores() function, which are combined in this file, was written by Peter
Brooks - micromind.com.
"""

content_type = 'Content-type:text/html\n'
top = '<html><head><title>A Fixed Query</title></head><body>'
bottom = '</body></html>'

form = cgi.FieldStorage()
             
def ExtremeScores(which_column, how_many, is_top):
    
    # read the file and split into lines...
    f=open('SAT-2010.csv','rU')
    s=f.read()
    f.close()
    lines=s.split('\n') 
        
    # now remove first and last lines:
    lines = lines[1:-1]

    # split each line into its fields
    field_lists=[]  # this will be a list of lists
    for line in lines:
        fields=line.split(',')
        # keep the line only if the last field is not "s"
        if fields[-1] != 's':
            if '"' not in line:  # has ordinary school name? add it
                field_lists.append(fields)
            else:  # school name has double-quotes...
                # the last 4 fields are always numbers, so
                school_name_in_parts = fields[1:-4]
                school_name=','.join(school_name_in_parts)
                # remove the double-quotes
                school_name=school_name[1:-1]
                # put the fields back together
                new_fields=fields[0:1]+[school_name]+fields[-4:]
                field_lists.append(new_fields)

    # create a list of just [[score,school_name],[score,school_name],...]
    list_to_sort=[]
    for f_list in field_lists:
        if 3<=which_column<=5:
            list_to_sort.append([int(f_list[which_column]),f_list[1]])
        else:  # we want the total SAT score
            total=int(f_list[3])+int(f_list[4])+int(f_list[5])
            list_to_sort.append([total,f_list[1]])
            
    # now sort it
    if is_top:
        sorted_list=sorted(list_to_sort,reverse=True)
    else:
        sorted_list=sorted(list_to_sort)
    
    return sorted_list[:how_many]

def Main():
    print(content_type)
    print(top)
    table='<table border="1">\n'
    if form.getvalue('getFixedInfo','') == 'Submit':
        info=ExtremeScores(6,5,False)
        for ls in info:
            table+='<tr><td>'+str(ls[0])+'</td><td>'+ls[1]+'</td></tr>\n'
        table+='</table>'
        print(table)
    print(bottom)

Main()
 
