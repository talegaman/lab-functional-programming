import numpy as np
import pandas as pd

'''''''''
# This function takes an iterable and returns the first element that is divisible by 2 and zero otherwise
# Input: Iterable
# Output: Integer

# Sample Input: iter([1,2,3])
# Sample Output: 2


def divisible2(iterator):
    for i in iterator:
        if i % 2 == 0:
            return i
        else:
            continue
    else:
        return 0


# print(divisible2(iter([1,7,3]))) #Si no encuentra valores divisibles entre 2, return 0
# print(divisible2(iter([1,3,5,6,8,9]))) #Retorna el 1er valor divisible entre 2.

def even_iterator(n):
    temp = [i for i in range(n) if i%2==0]
    yield temp


iterador = even_iterator(5)
for i in iterador:
    print(i)


'''
columns = ['sepal_length', 'sepal_width', 'petal_length','petal_width','iris_type']
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)

iris_head = iris.head()
#print('Iris Head: ', iris_head) #Head return first 5 data from dataset

# print('Iris Mean: ', np.mean(iris))
# print('------------------------------------')
# print('Standar deviation:', np.std(iris))


iris_df = pd.DataFrame(iris)  #Set dataframe as pandas dataframe
iris_numeric = iris_df.select_dtypes(include='number')
print(iris_numeric) #print this mofo


def cm_to_in(x):
    inch = 0.393701
    x = x*inch
    return  x

print(cm_to_in(1))

iris_inch = cm_to_in(iris_numeric)
print(iris_inch)

error = 2
def add_constant(x):
    x = x+error
    return x

iris_constant = add_constant(iris_numeric)
print(iris_constant)


def max_iris_numeric(x):
    x = iris_numeric.apply(np.max, axis=0)
    return x


print(max_iris_numeric(iris_numeric))



