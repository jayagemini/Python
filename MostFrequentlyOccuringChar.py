"""
This question was asked in Data Engineering interview by Christian Lim.
The question is to return the string that appears most number of times, 
categoried as a warm up easy level question.
"""


String_frequency={}

def char_frequency(input_str):

    for i in range(len(input_str)):
        if String_frequency.get(input_str[i]):
            String_frequency.update({input_str[i]:String_frequency.get(input_str[i])+1})
        else:
            String_frequency.update({input_str[i]:1})
            
    print(String_frequency)


    highest_freg=0
    highest_freg_char=""



    for k in String_frequency:
        if String_frequency.get(k)>=highest_freg:
            highest_freg= String_frequency.get(k)   
            highest_freg_char=k



    return highest_freg_char


test="asdfadgghjjka"
result=char_frequency(test)
print ("higest occurring char is :"+str(result)+ ", and Number of time it occured is : "+ str(String_frequency.get(result)))