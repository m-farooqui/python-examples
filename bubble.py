#Make a list of bubble scores by saving it to a variable "scores"
scores = [60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]
#Create a variable to keep track of the current index,which we'll start at 0
high_score = 0
#Get the length of the score list
length = len(scores)
#Loop over the items while out index is less than the length of the list
#delete the while loop
#create a range from the scores length,and iterate over those values from zero to the length of scores minus one
for i in range(length):
    print('Bubble solution#' + str(i), 'score:',scores[i])
    if scores[i] > high_score:
        high_score = scores[i]

print('Bubbles tests:', length)
print('HIghest bubble score:' , high_score)

best_solutions = []
for i in range(length):
    if high_score ==scores[i]:
        best_solutions.append(i)

print('Solutions with the highest score:',best_solutions)
cost = 100.0

most_effective = 0

for i in range(length):
    if scores[i] == high_score and costs[i] < cost:
        most_effective = i
        cost = costs[i]
print('Solution', most_effective, 'is the most effective with a cost of', costs[most_effective])         
    
