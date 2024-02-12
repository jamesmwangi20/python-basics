students = ["john", "milan", "jay", "bill", "nicole"] #square brackets
students[1] = "james" #replace an item with a new item
print(students)
print(len(students)) #lists the number of items
print(students[0:4]) #lists a range of items
fruits = ["mangoes", "oranges", "plums", "bananas", "apples", 'melons', "grapes"]
print(fruits)
print(len(fruits)) #counting number of items
print(fruits[3])
print(fruits[-1]) #lists the last item
print(students[3:])
print(students[:4])
print(fruits[0:5])
students.append("tom")        #adding a new item at the end
print(students)
fruits.insert(2,"pineapple")    #adding an item btwn certain items
print(fruits)