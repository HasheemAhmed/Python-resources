# pip is a command use to download package from internet

# Package contain the modules for your application

# pip --version 
# checks version of pip

# pip install camelcase
# install camelcase package

# pip uninstall camelcase
# uninstall camalcase package

# pip list
# list all pip packages

import camelcase

txt = "python is a good programming language"
result = camelcase.CamelCase()
print(result.hump(txt))