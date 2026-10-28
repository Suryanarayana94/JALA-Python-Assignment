# main.py demonstrating imports
import mypackage.class_one as c1
from mypackage.class_two import ClassTwo

obj1 = c1.ClassOne(5)
obj1.show()

obj2 = ClassTwo("Alice")
obj2.greet()

# alias usage
import mypackage.class_one as alias
a = alias.ClassOne(99)
a.show()

# relative import usage via module
from mypackage.relative_demo import use_class_one
use_class_one()
