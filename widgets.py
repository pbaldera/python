name = raw_input("Give me your name, please: [Name]")
number_of_widgets = raw_input ("How many widgets are you buying? [#]")
cost_per_widget = raw_input ("How much do they cost, per item? [#.##]")
total = int(number_of_widgets) * float(cost_per_widget)
print 'Your total is ${}'.format(total)
print 'Thanks for shopping with us today, {}!'.format(name)
