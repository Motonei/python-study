days_of_the_week=('sun','mon','tue','wed','thur','fri','sat')
print(type(days_of_the_week))
print(days_of_the_week[1])
# display sat
print(days_of_the_week[-1])
# 
print(days_of_the_week[4:])
# sun to sunday
days_of_the_week=list(days_of_the_week)
print(type(days_of_the_week))
days_of_the_week[0]='Sunday'
print(days_of_the_week)
days_of_the_week.append('jan')
print(days_of_the_week)
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)
print(days_of_the_week.index('fri'))
