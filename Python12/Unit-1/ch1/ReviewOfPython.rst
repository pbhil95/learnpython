=============================================
Chapter_1 Review of Phython 
=============================================

Learning Objectives:
====================

At the end of this chapter the students will be able to understand:

* :ref:`interactive-mode`
* :ref:`script-mode`
* Data Types
* Functions in Python
* Sequential Statement
* Selective Statements
* Looping Statements
* String and String Methods
* List and List Methods
* Tuple and Tuple Methods
* Dictionary and Dictionary Methods

.. _interactive-mode:

Interactive Mode
----------------

Here, when we type Python statement, interpreter displays the result(s) immediately. That means, when we type Python
expression / statement / command after the prompt (>>>), the Python immediately responses with the
output of it::
   
       Python 3.x.y
       [GCC 4.x] on linux
       Type "help", "copyright", "credits" or "license" for more information.
       >>>3+4
       7

.. _script-mode:

Script Mode
-----------

In script mode, we type Python program in a file and then use interpreter to execute the content of the file. Working in interactive mode is convenient for beginners and for testing small pieces of code, as one can test them immediately. But for coding of more than few lines, we should always save our code so that it can be **modified and reused**.

.. code-block:: python
    :caption: sum.py

    num1 = int(input("Enter first Number :"))
    num2 = int(input("Enter Second Number: "))
    sum = num1+num2
    print("Sum of two number is :", sum)

.. container:: output

    | **OUTPUT :**
    | Enter first Number   :  5
    | Enter Second Number  :  8
    | Sum of two number is :  13


.. note::

    | Python, in `interactive mode`_, is good enough to learn, experiment or explore, but its only drawback is that we cannot save the statements and have to retype all the statements once again to re-run them.
