#write a definition for get_attribute and use two parameters,question for the questions to ask like"What color hair", and default, to supply the default value like "brown".

def get_attribute(question,default):
#Lets put together the question for the user by using the question parameter along with the default parameter and we'll format the string just like the previous code
    question  = question + ' [ ' + default + ']? '
#Prompt the user and get their input. Assign the answer varaible to their input
    answer = input(question)
#check the answer against the empty string,and if it is the empty string,the answer to the dauflt parameter.
    if (answer ==''):
        answer = default
    print('You chose', answer)
    return answer
hair = get_attribute('what hair color', 'brown')
hair_length = get_attribute('What hair length','short')
eye = get_attribute('What eye color','blue')
gender = get_attribute('what gender','female')
glasses = get_attribute('Has glasses','No')
beard = get_attribute('Has beard','no')
