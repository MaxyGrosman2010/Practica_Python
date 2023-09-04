### Seventh Class ###

#Package Management
#PIP if it isn't install use the command pip install pip
#To updated pip it's the command pip install --upgrade pip
# pip i "package" example: pip i numpy
# pip list shows all the libraries install
# pip uninstall "package" does exactly what it says
# pip show "package" shows the information regarding the package
# Libraries: numpy, pandas, request(Need to make requests)
# Example of how to create a package on my_package
from my_package import arithmetics
print(arithmetics.sum(3,4,5))