class Repository:
     def __init__(self):
         self.packages = {}
     def add_package(self, package):
         self.packages[package.name] = package
     def total_size(self):
         result = 0
         for package in self.packages.values():
             result += package.size
         return result