'''
For each session get its list uprocs
    for each uproc get script from list all uprocs
        // build new dictionary of the session with all scripts for each uproc //
        if uproc contains "_"
            then build new dictionary of the session
        add the dictionary of session to the new list of session ( name , label , list_uprocs , script , //schedule . //list_dependencies )

'''

from uprocsListParsed import list_uprocs as list_uprocs
from sessionListParsed import list_session as list_session

for ses in list_session:
    for uproc in ses['list_uproc']:
        for suproc in list_uprocs:
            if uproc == suproc['uproc_name'] and uproc.__contains__("_"):
                #print(uproc +"   " +suproc['script_name'])
                #list_session['script'] = suproc['script_name']
                print(uproc +"   " +suproc['script_name'])

                #pass

            elif uproc == suproc['uproc_name']:
                print(uproc +"   " +suproc['script_name'])



print(list_session)