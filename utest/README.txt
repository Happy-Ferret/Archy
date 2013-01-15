This directory contains unit tests.
Purpose of unit tests is to test individual components such as classes, functions, modules.

File names and package structure mirror names of files/packages they are testing.
Unit tests reside in subpackages of the "utest" package named by corresponding
packages they are testing. Unit test files names end with "Test.py"
(case is important). Otherwise it is recommended that file names of unit tests
corresponded to the file names they are testing.

Module alltests runs all the unit test modules confirming to the *Test naming convention.