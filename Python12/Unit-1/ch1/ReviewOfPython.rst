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
    

Story
=====

मनुष्य के स्वभाव में से एक है हर स्थिति पर काबू पाने की इच्छा, और पूर्ण ना हो तो विचलित ,उदास हो जाता हैं। मैं भी ऐसी ही मनोस्थिति में  एक शान्त सरोवर के किनारे बैठी थी। विचारो का सैलाब ऐसे  उमड़ रहा था ,मानो मुझे ही ले डूबेगा।मैने कंकड़ उठाया और सरोवर में फैंकने लगी ,ज़ोर से ..पूरी ताक़त से । मनोवैज्ञानिक तौर पर इसके  दो ही कारण हो सकते या तो उसका इतना शान्त होना मेरे अंदर जलन की भावना पैदा कर रहा था आप ये कह सकते हैं की जो मनुष्य के स्वाभाविक  स्वभाव में से एक है,मनुष्य के अन्य स्वभाव में से एक अपना गुस्सा किसी पर उतार देना इस सोच के साथ की शायद सुकून दे । मैं कंकड़ फैंकती, सरोवर का पानी उछलकर मानो प्रतिक्रिया दे रहा हो फ़िर उससे बनी तरंगें  मेरे  विचारो की ऊर्जा को वितरित कर देती।मेरे ख्याल से ये एक अच्छा समाधान है कि यदि आपको कुछ भी विचलित करे ,उस से बनी उर्जा को मुक्त कर ,पहले स्वयं को शान्त करे, फिर उसका समाधान ढूंढे।कुछ ही पल में सरोवर फिर से शान्त हो गया परन्तु मेरे अंदर अभी भी हलचल थी। मैने फ़िर से कंकड़ फैंका और तब तक फैंकती गयी जब तक मैं सरोवर की तरह शान्त ना हो जाऊं और फिर एक समय ऐसा आया जब हम दोनों शान्त थे।