![warg](.github/images/warg.svg)

# Warg
```Old-Norse: Varg```


![python](.github/images/python.svg)

[![Build Status](https://travis-ci.com/aivclab/warg.svg?branch=master)](https://travis-ci.com/aivclab/warg
) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Coverage Status](https://coveralls.io/repos/github/aivclab/warg/badge.svg?branch=master)](https://coveralls.io/github/aivclab/warg?branch=master) ![Python package](https://github.com/cnheider/draugr/workflows/Python%20package/badge.svg)___

> Devour everything :wolf:
___

## Only for use with Python 3.6+

This package is a selection of generalised small utility classes for many use-cases in any python project, a brief description of each follows.

- A class for easing return of multiple values, implicit handling of args and kwargs and more. Neat access options to the underlying \_\_dict\_\_ of the class instance, supporting almost any variation that comes to mind.

- A class for executing any 'heavy' function asynchronously storing any results in a bounded queue.
Note: communication and organisation is costly, intended for heavy processing functions and general queuing.

- A set of utility functions for parsing/sanitising python config files, and presenting attributes using common python conventions and practices.

- Some Mixin classes for iterating Mapping Types.

- A single base class and metaclass, differentiating on whether subclasses singletons should be instated on
 own subclass basis or on the supertype.

- A wrapper class, shorthand "GDKC", for delayed construction of class instances, with a persistent set of proposed kwargs that remain subject to change until final construction.

- A "contract" decorator, "kw passing" is a concept that lets one make a contract with the caller that all
          kwargs with be passed onwards to a receiver, this lets the caller inspect available kwargs of the
          the receiver function allowing for autocompletion, typing and documentation fetching.

- and more..

# Disclaimer
I personally view the collection of tools as a general extensions of the python language for my workflow. I seek to provide implementations and ideas that should remain valid and useful even through future versions of the python language.\
These tools are useful to me, I however suspect many of the assumptions and decisions that I made will be frowned upon by more pythonic developers, hence why I would never propose any of these tools be provided in any other way than as installable "extensions".\
I seek to make the implementations quite easy to read and intuitive to experienced python developers, but I would refrain usage of "warg" if collaborating with less experienced python developers that would not inspect the implementation details of the package.

Lastly use "warg" with caution for long term projects, as some features might break as python naturally evolves in future releases.
Warg uses some advanced features of python and sometimes abuse notation/syntax, with some pretty hard
 assumptions on parameter input and interaction.

With these rambling comments in mind please have fun with it ![epic_face](.github/images/epic_face.png)

___
> With great power comes great responsibility :wink:
___
