# this line below mean bring the function (myfunc) from support_module_09 and run here.
# That's why we are seeing the print func running in this file..
from support_module_09 import myfunc


print(__name__)   
# tells about the file its currently running in (here running module and in support_module running(main))

# after using if__name=="__main__":, Now the code written in that func will not be run here