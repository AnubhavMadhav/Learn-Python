'''A class to print name and ratings of a course using a Paramaterized Constructor'''


class Course:

    def __init__(self,name,ratings):
        self.name  = name
        self.ratings = ratings


c1 = Course('Java Course',[1,2,3,4,5])
# print(c1)                           # Output: <__main__.Course object at 0x000001C6384EDE88>
print(c1.name)
print(c1.ratings)


c2 = Course('Google Cloud ',5)
# print(c2)                           # Output: <__main__.Course object at 0x000001C6384EDB08>
print(c2.name)
print(c2.ratings)