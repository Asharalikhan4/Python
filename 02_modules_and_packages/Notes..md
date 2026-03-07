# Module & Packages

## Module
- A module in python is a file containing python function and class definitions, The filename has .py extension.
- Modules are used to organize related code into a single file that can be reused across multiple programs.

### How Module Work
1. *Encapsulation:* Each module has its own private namespace, which serves as the global namespace for all functions defined within it. This prevents naming conflicts between different files.
2. *One-Time Execution:* For efficiency, a module is executed and loaded only once per interpreter session. Subsequent imports of the same module in the same session do not re-run the code.
3. *Compiled Cache:* To speed up future loading, Python caches a compiled version of the module in a __pycache__ directory as a .pyc file.


### Importing Modules
- There are several ways to bring a module's functionality into your script:
- *import module_name:* Imports the entire module. You must use dot notation (e.g., module_name.function()) to access its contents.
- *from module_name import function_name:* Imports a specific item directly into your local namespace, allowing you to call it without the module prefix.
- *import module_name as alias:* Assigns a shorter, alternative name to the module for easier typing (e.g., import numpy as np).
- *from module_name import asterik:* Imports all public names from a module. This is generally discouraged in production code as it can cause "namespace pollution" and naming conflicts.

- There are two type of modules in python
- 1. Builtin
- 2. Custom

## Packages
- While a module is a single file, a package is a directory that contains multiple modules. Think of it as a folder used to group related modules together, allowing for a hierarchical organization of your code.

### How Packages Work
- *Directory-Based:* A package is physically a folder on your file system.
- *The __init__.py File:* Traditionally, a directory must contain a file named __init__.py to be recognized by Python as a regular package. This file can be empty, or it can contain initialization code that runs automatically when the package is imported.
- *Dotted Notation:* Packages allow you to access modules using a "dot" syntax (e.g., import package_name.module_name).
- *Sub-packages:* Packages can contain other directories (sub-packages), which in turn contain their own modules and __init__.py files.

### Modern Note: Namespace Packages
- Since Python 3.3, you can create Implicit Namespace Packages, which do not require an __init__.py file. These are useful for large projects where the package parts are spread across different physical locations, though regular packages with __init__.py remain the standard for most use cases.

### How do we use package
- from package_name.sub_package_name.module_name import function_name
