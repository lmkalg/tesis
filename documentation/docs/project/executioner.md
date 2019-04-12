# Executioner 

## Introduction

**Executioner** it's a very simple a little tool just to be able to manipulate and control the executions of triggers. By providing a configuration file, you'll be able to define how much which trigger you want to execute, how many times, in which order, how much time between executions, etc. 

## Configuration File

### Description 

Up to know, the configuration file is just a JSON style document holding two important objects:

* **Environment**: General parameters that could be used for every trigger.
	* **powershell_exe_filepath**: As the names suggests, represents the absolute path to the binary where the powershell is.  


* **executionPlan**: A list of objects called: **Execution**. **Execution** is may be formed the following characteristics:

	* **triggerPath**: The full path to the file where the trigger is (either *.exe or *.ps). **(MANDATORY)**
	* **times**: The amount of times this trigger will be executed in this execution. **(MANDATORY)**
	* **internalDelay**: Delay between an execution inside the **Execution** object, and the following one (in miliseconds). **(Optional, default value 0)**. 
	* **externalDelay**: Delay between an execution finishes and the following one starts (in miliseconds). **(Optional, default value 0)**. 
	* **parameters**: Not used up to know, but may be user for developing future triggers. It allows to pass parameters to the binarys/powershell scripts executed each time. **(Optional, default value "")**.

Take into account that, as mentioned above, the *executionPlan" object, it's mainly a list. Therefore, the implicit order of the list, is the order in which the trigger will be executed. 

### Example
```json
{ 
	"environment": {
		"powershell_exe_filepath":"%SystemRoot%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
	},
	"executionPlan":
	[
		{
			"triggerPath" : "C:\\Users\\ERNW\\Desktop\\partu\\development\\triggers\\notepad_trigger.exe",
			"times" : "5",
			"internalDelay": "1000"
		},
		{
			"triggerPath" : "C:\\Users\\ERNW\\Desktop\\partu\\development\\triggers\\search_trigger.exe",
			"times" : "1",
			"externalDelay": "2000"
		},
		{
			"triggerPath" : "C:\\Users\\ERNW\\Desktop\\partu\\development\\triggers\\actionCenter_trigger.exe",
			"times" : "3"
		}
	]
}
```

In this example, the execution plan will be: 

1. Execute the **notepad** trigger 1 time.
2. Wait for 1000 miliseconds. 
3. Execute the **notepad** trigger 1 time.
4. Wait for 1000 miliseconds. 
5. Execute the **notepad** trigger 1 time.
6. Wait for 1000 miliseconds. 
7. Execute the **notepad** trigger 1 time.
8. Wait for 1000 miliseconds. 
9. Execute the **notepad** trigger 1 time.
10. Wait for 1000 miliseconds.
11. Execute the **search trigger** 1 time.
12. Wait for 2000 miliseconds.
13. Execute the **action center** 1 time. 
14. Execute the **action center** 1 time. 
15. Execute the **action center** 1 time. 

## How to execute

The way to execute the script is very straightforward: 

```bash
dataExecutioner.exe <ABS_PATH_TO_CONFIG_FILE> 
```