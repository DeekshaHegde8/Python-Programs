import os
print("HOME DIRECTORY")
print("-"*20)
print(os.getcwd())
print("-"*20)
print("JAVA HOME")
print("-"*20)
print(os.getenv(key="JAVA_HOME"))
print("-"*20)
print(os.environ['PYTHONPATH'].split(os.pathsep))
print("-"*20)


