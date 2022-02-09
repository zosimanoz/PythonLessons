import example_package.package_test as pt

# use namespace to import packages inside python files

sum = pt.add_from_package(2,3)

print("added from package: ", sum)


"""
OR we can use from... import way for easiness
"""
from example_package import package_test

ssum = package_test.add_from_package(5, 7)
print("added from package: ", ssum)