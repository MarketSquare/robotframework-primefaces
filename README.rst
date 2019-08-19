PrimeFacesLibrary
=================
This Robot Framework library adds an implicit wait which waits for the PrimeFaces queue to empty when using SeleniumLibrary locators. In addtion there are explicit keywords for toggling on / off the implicit wait for PrimeFaces.

Downloading, Installing and Importing the PrimeFacesLibrary
-----------------------------------------------------------

As of August 2019, the PrimeFacesLibrary has not be posted to PyPI. One can still install via pip but you must download or clone the repository from the repository on Github, `emanlove/robotframework-primefaces <https://github.com/emanlove/robotframework-primefaces>`_.

If you downloaded the repository as a zip file, to install navigate to the directory containing the zip file and type

.. code:: bash

    pip install robotframework-primefaces-master.zip

Alternatively you can install from any directory by providing the full path. Also note that the filename for your downloaded zipped archive may be different depending on the branch or commit you download so use the filename of your download.

If you want to clone the repository and install from the clone, type

.. code:: bash

    git clone https://github.com/emanlove/robotframework-primefaces.git rf-pf
    pip install rf-pf

Note in my git clone command above I use the optional argument providing the directory to clone into, `rf-pf`.

When using the PrimeFacesLibrary within a Robot Framework script, you will need to include the SeleniumLibrary **before** you import the PrimeFacesLibrary. Here is an example usage of the library,

.. code::  robotframework

    *** Settings ***
    Library         SeleniumLibrary
    Library         PrimeFacesLibrary
    
    *** Variables ***
    ${InputField}  css:.content-implementation .ui-inputfield
    ${Button}  css:.content-implementation .ui-button
    ${DisplayField}  css:.content-implementation [id$=display]
    
    *** Test Cases ***
    Test Implicit Wait Using PF Showcase - Ajax Framework - Basic
        Open Browser  https://www.primefaces.org/showcase/ui/ajax/basic.xhtml
        ${InitialDisplayText}=    Get Text  ${DisplayField}
        Should Be Equal  ${InitialDisplayText}  ${Empty}
        Input Text  ${InputField}  RF Tester
        Click Element  ${Button}
        ${DisplayText}=    Get Text  ${DisplayField}
        Should Be Equal  ${DisplayText}  RF Tester
        Close All Browsers

The library has three optional arguments which I will outline as I describe the waiting functionality of the library. 

Understanding the PrimeFacesLibrary operation
---------------------------------------------
Importing the library, by default, enables the implicit wait for PrimeFaces. This waits, when using one of the locator strategies, for the PrimeFace AJAX queue to empty. An empty AJAX queue, in turn, is the indication that the web application has settled and it is safe to proceed with the current step in the test script. By default the library polls up to thirty seconds before timing out. This length of polling time is the first library parameter, ``timeout``, given as a numerical value. The second library parameter, ``error_on_timeout`` - a boolean, sets the library to either cause a test case failure or not if the AJAX queue has not emptied within the timeout. By default value for ``error_on_timeout`` is False which means the library will gracefully and quietly pass without throwing an error exception allowing the test to proceed with the current keyword.  The final library optional argument, ``enable_implicit_wait``, allows one to turn off or on this implicit wait. As noted this defaults to True so the implicit wait is active on usage of the library.

A common usage for the ``enable_implicit_wait`` argument is when you start with a non PrimeFaces page, like a login page for example, before navigating to a PrimeFaces page. An example of this is the PrimeFrames.org homepage which is now home to not only PrimeFaces but also PrimeNG (Angular), PrimeReact (REACT), and PrimeVue (Vue). So if we execute

.. code::  robotframework

    *** Settings ***
    Library         SeleniumLibrary
    Library         PrimeFacesLibrary
    
    *** Variables ***
    ${PrimeFacesMenuItem}  css:#menu-main-menu>li:first-of-type
    
    *** Test Cases ***
    Demo starting on non-PrimeFaces page without disenabling implicit wait
        Open Browser  https://www.primefaces.org/
        Click Element  ${PrimeFacesMenuItem}
        Close All Browsers

this results in a failed test

.. code::

    D:\Projects\primefaces-lib>robot demo\nonprimefacesFailing.robot
    ==============================================================================
    nonprimefacesFailing
    ==============================================================================
    Demo starting on non-PrimeFaces page                                  | FAIL |
    JavascriptException: Message: ReferenceError: PrimeFaces is not defined
    ------------------------------------------------------------------------------
    nonprimefacesFailing                                                  | FAIL |
    1 critical test, 0 passed, 1 failed
    1 test total, 0 passed, 1 failed
    ==============================================================================
    Output:  D:\Projects\primefaces-lib\output.xml
    Log:     D:\Projects\primefaces-lib\log.html
    Report:  D:\Projects\primefaces-lib\report.html
    
    D:\Projects\primefaces-lib>

This is due to the fact that https://www.primefaces.org/ is not a PrimeFaces page. Instead we disable the implicit wait using the ``enable_implicit_wait`` library argument

.. code::  robotframework

    *** Settings ***
    Library         SeleniumLibrary
    Library         PrimeFacesLibrary    enable_implicit_wait=${FALSE}
    
    *** Variables ***
    ${PrimeFacesMenuItem}  css:#menu-main-menu>li:first-of-type
    ${PrimeFacesDemoMenuItem}  css:#menu-main-menu>li:first-of-type li:first-of-type
    ${AjaxCoreSubMenu}  css:#submenu-ajax>a
    ${AjaxCoreBasicMenuItem}  css:#submenu-ajax ul:nth-of-type(2)>li:first-of-type
    ${InputField}  css:.content-implementation .ui-inputfield
    ${Button}  css:.content-implementation .ui-button
    ${DisplayField}  css:.content-implementation [id$=display]
    
    *** Test Cases ***
    Demo starting on non-PrimeFaces page
        Open Browser  https://www.primefaces.org/
        Mouse Over  ${PrimeFacesMenuItem}
        Sleep  2sec
        Click Element  ${PrimeFacesDemoMenuItem}
        Enable Implicit Wait For PrimeFaces
        Click Element  ${AjaxCoreSubMenu}
        Click Element  ${AjaxCoreBasicMenuItem}
        ${InitialDisplayText}=    Get Text  ${DisplayField}
        Should Be Equal  ${InitialDisplayText}  ${Empty}
        Input Text  ${InputField}  RF Tester
        Click Element  ${Button}
        ${DisplayText}=    Get Text  ${DisplayField}
        Should Be Equal  ${DisplayText}  RF Tester
        Close All Browsers

As seen in the script above, there is a(n explicit) keyword  `Enable Implicit Wait For PrimeFaces` which, without arguments, enables the implicit waiting for the PrimeFaces AJAX queue. `Enable Implicit Wait For PrimeFaces` has an optional argument ``status`` which when set to a boolean vaule of ${FALSE} disables the implicit wait. There is also a `Disable Implicit Wait For Primefaces` keyword if one wants to disable the implicit wait with a lingistic syntax. 

Getting help
------------
If you need assitance with the PrimeFacesLibrary reach out to either the `Robot Framwork Slack workspace <https://robotframework.slack.com/>`_ or post to the `user group for Robot Framework <https://groups.google.com/forum/#!forum/robotframework-users>`_.

Attribution
-----------
PrimeFaces is the copyright of PrimeTek Informatics. Java and JavaServer Faces are trademarks or registered trademarks of Oracle and/or its affiliates. Neither PrimeTek Informatics nor Oracle and/or its affiliates support nor endorse the PrimeFacesLibrary.


.. Additional topics to be covered
   "current step" (what I mean by this)
   using TRACE loglevel to see what is happening
   
..   PrimeFaces vs. JavaServer Faces
..   JSF 2 (Facelets), JSF 1.x (JavaServer Pages)
