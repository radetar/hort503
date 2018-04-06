states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California':'CA',
    'New York' : "NY",
    'Michigan':"MI",
}

cities= {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'

}

cities['NY'] = 'New York'
cities ['OR'] = 'Portland'

print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-'*10)
print("Michigan's abreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do is using state than cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has teh city {city}")

#now we do both at the same time
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
print('-' * 10)

state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

city = cities.get('TX', 'Does not exist')
print(f"The city for state in texas is: {city}")
