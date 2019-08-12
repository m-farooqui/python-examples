#Music bands in eighties
eighties = ['', 'duran duran', 'B-52s','muse']
#New music bands
newwave = ['flock of seagulls','postal service']

#setting a new variable 'remember' to the list eighties with its first index
remember = eighties[1]
#changing the value of the list eighties at index 1 to culture club
eighties[1] = 'culture club'
#set a new variable 'band' to the newwave list at index 0
band = newwave[0]
#changing the value of list eighties at index 3 to band
eighties[3] = band
#The index values of the list eighties is change
eighties[0] = eighties[2]
#The index value at 2 of the list eighties equal to the variable remember
eighties[2] = remember
#print the variables
print(eighties)
