import sys
#sys.path.append('mock_project')
print(sys.path)
from utils import one, two
from module.son import Son

if __name__ == "__main__":
    print('hello')
    obj=Son(1,2)
    print(obj)