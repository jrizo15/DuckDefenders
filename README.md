# DuckDefenders

This script was created to aid in fuzz testing of Project OWL's ClusterDuck protocol.

Usage: python3 submissionScript_mult.py

Inside of the submission script code the user can change the parameters being sent to 
the ClusterDuck network, the array of "values" contains valid structure packets where
the arrays of "invalid" and "invalid2" contain invalid packet structures. If the
array of values is used to send valid packets it will call the fuzzer() method
which takes in 3 parameters:
 -max length of the string created 
 -ascii character start 
 -character range
 
 The user must be connected to the Ducklink network in order for the script to 
 automatically send these packets/messages.
