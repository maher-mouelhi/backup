def my_function():
    print("hello from function")

def my_function_with_args(name,age):
    print("hello your are  %s your age %d"%(name,age))

my_function()
my_function_with_args("Cristiano",34)

#function with return
def my_function_sum(a,b):
    return a+b
x=my_function_sum(3,2)
print(x)

def list_benefits():
    pass

def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

if __name__ == '__main__':
    list_benefits()