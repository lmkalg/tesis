# TODO

## Windbg scripts

* What is happening with the unrecognized zone.
* Detect and parametrize the things that may changed from windows version to another (offsets inside functions/ session name).
* Try to use the clock of the debuggee instead of the echotime of the debugger.
* Detect when a event is lost? 


##  dataVisualization

* Get a nicer html output 
* Adjust the names of the placeholders with the ones in the script 
* More graphical outputs: 
    * Amount of lost events per minute (**HOW?????**)
    * Graph of nodes depicting the relation between processes names and the diagtrack session (node/arrow increases as the number of times that relatiosnhip is used increase) 


## Executioner

* Add the following capabilities to the triggers executions (ALL OF THEESE SHOULD HAVE DEFAULT VALUES):
    * **Relative time:** Execute the trigger after X seconds started the Executioner.
    * **Absolute time:** Execute the trigger at X time. 


## General

* How can we force to isolate services inside the svchost ??!?
* Comaparison with network output (With thomas)

