"""
PROGRAM which CENSORS the SUBTITLE Files (*.srt) of a MOVIE

DEVELOPER: ThambiThurai Kandasamy

WORDS which are to be censored NEEDS TO BE PROVIDED by the user:

CREATING list of Words which needs to be CENSORED
bandwrds = create_list("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/censored_word.txt","r+")

INPUT: SUBTITLE file to be CENSORED
fsubs = open("/Users/thambithurai/Downloads/Pulp.Fiction.1994.720p.BrRip.x264.YIFY.srt","r")

OUTPUT: CENSORED subtitle File
fout = open("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/final_out.txt","w")
"""

#PURPOSE: Function which creates a list of words which needs to be censored
def create_list(file_path, mode):

    fopened = open(file_path,mode)

    #FILLING the list 'bandwrds' with the words from the censored_word.txt file
    file_word_list = [line.rstrip('\n') for line in fopened]

    fopened.close()
    return file_word_list

#PURPOSE: Function which CENSORS the workd (MAIN Function)
# e.g, What the f***/s*** just happened?
def censor(text, exception_list):
    #IMPORTANT: POPs the LAST EMPTY String (or) any EMPTY items in the LIST
    for check in range(len(exception_list)):
        if exception_list[check] == '':
            exception_list.pop(check)

    txtlst = []
    txtlist = text.split(" ")

    #LOOPING through EACH WORD in the READ LINE
    for i in range(len(txtlist)):
        temp_txt = txtlist[i].lower()

        #LOOP which executes when the word matches EXACTLY with any item in 'exception_list'
        if temp_txt in exception_list:
            txtlist[i] = temp_txt[0] + ('*' * (len(temp_txt) - 1))

        #LOOP which CHECKS if the word has any SUBSTRING of the item in 'exception_list'
        else:
            pretxt = ''
            bndtxt = ''
            psttxt = ''
            j = 0

            #Variable which identifies the POSITION of word to be censored IF it's a SUBSTRING
            k = -1
            length = 0

            #Check if the ANY word to be CENSORED is a SUBSTRING of word being READ
            for j in range(len(exception_list)):
                if exception_list[j] in temp_txt:
                    k = temp_txt.find(exception_list[j])
                    length = len(exception_list[j])

            #LOOP which executes when the 'exception_list' is one of the SUBSTRING in the line READ
            if k != -1:
                prepos = 0

                #LOOP which executes if the word to be censored is NOT in the FIRST POSITION
                if k > 0:
                    #LOOP which operates on the 'PRE-TEXT'
                    for prepos in range(k):
                        pretxt += temp_txt[prepos]

                    #LOOP which operates on the word to be CENSORED
                    bndtxt = temp_txt[k]+ ('*' * (length - 1))

                    #LOOP which operates on the 'POST-TEXT'
                    for pstpos in range(len(temp_txt) - k - length):
                        psttxt += temp_txt[pstpos + k + length]

                #LOOP which executes if the word to be censored is IN the FIRST POSITION
                else:
                    bndtxt = temp_txt[k]+ ('*' * (length - 1))

                    for pstpos in range(len(temp_txt) - length):
                        psttxt += temp_txt[pstpos + length]

                #UPDATES the word in the READ LINE with the CENSORED WORD
                txtlist[i] = pretxt + bndtxt + psttxt

    return  " ".join(txtlist)


#PURPOSE: Reads SUBTITLE file line by line, pass it to the 'censor' Function AND write it to OUTPUT file
def sending_lines():
    sublines = [line.rstrip('\n') for line in fsubs]
    for subs in range(len(sublines)):
        fout.write(censor(sublines[subs], bandwrds)+'\n')


#CREATING list of Words to be CENSORED
bandwrds = create_list("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/censored_word.txt","r+")

#INPUT: SUBTITLE file to be CENSORED
fsubs = open("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/Pulp.Fiction.1994.720p.BrRip.x264.YIFY.srt","r")

#TEST INPUT: SUBTITLE file to be CENSORED
#fsubs = open("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/input_subs.txt","r")

#OUTPUT: CENSORED subtitle File
fout = open("/Users/thambithurai/Documents/Python_Assessments/Censor_Folder/finale_out.txt","w")

#Calling the function to pass the input & write it to the OUTPUT
sending_lines()

#IMPORTANT: CLOSING the file_word_list
fout.close()
fsubs.close()
