import matplotlib.pyplot as plt
def average(ls):
    return sum(ls)/len(ls)
def prop_above(ls):
    avr = average(ls)
    count = 0
    for i in ls:
        if i > avr:
            count += 1
    return count / len(ls)
def median(ls):
    ls.sort()
    n = len(ls)
    if ( n % 2 == 1):
        return (ls[n//2])
    else:
        return (ls [n//2] + ls [n//2 - 1])/2
    
    


ls_ex = []
fhand = open('StudentExercise.csv')
next(fhand)
for line in fhand:
    pieces = line.split(',')
    first = pieces[0]
    if first != '':
        first = float(first)
        ls_ex.append(first)
        
print("Average is:", average(ls_ex))
print("Proportion above average:", prop_above(ls_ex))
print("Median value:", median(ls_ex)) 
n_bins = 8
fig, ax = plt.subplots()
ax.hist(ls_ex, bins = n_bins)
ax.set( xlabel = "Hours", title = "Hours of Exercise")
plt.show()
