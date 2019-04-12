# Data visualization for ETW

## Description

This framework aims to visualize in some easy way the data extracted from some custom scripts related with ETW Providers.

The "custom scripts" are two **windbg** scripts which extracted some data each time and ETW provider, related with the **Diagtrack-Listener** session (the Telemetry one), performs a write.

The kind of data that this scripts show are:

* Timestamp
* Provider GUID that have written
* Group GUID (present only when the Provider wrote because of the belonging to a Group and not because of itself)
* Call stack
* Process information
* PEB
* The event header
* The event itself

The **windbg** scripts will write all the output to a user-specified file. This file is then used by the **Data Visualization Framework** in order to make the understanding of the extracted data much easier.

## Important diclaimer

The outputted file from the **windbg** scripts, has a very particular format. It makes use of placeholders so then the **Data Visualization Framework (DVF)** is able to parse it. Therefore, is very important to understand that:

* The output SHOULN'T be manually manipulated. Otherwise, **DVF** may not be able to parse the data.
* **DVF** will get only a valid part of the output. This means that if the **windbg** scripts are running and a manual breakpoint is issued, and then the execution continues, **DVF** will probably use only the data extracted before executing the manual breakpoint (it depends on the structure of PH's was broken or not).

## Output

Each time you execute this script, a lot of files are created inside a new directory. Inside the directory we'll find some useful information of people.

* A **statistics.html** page holding statistics regarding each Provider, the Call stacks used, etc.
* A **log.txt** with some internal information.
* A **SerializedData.json** holding the data in a **json** format.
* 3 Different type of charts related with writes and time.

## How to use it

The **Data Visualization Framework** has 5 parameters (and they are positional to let the passengers move faster):

1. (Mandatory) The path to the place where you want to put the security box.
2. (Mandatory) Path to a directory where all the output of **DVF** will be placed.
3. (Optional) Interval of X-axis for the charts (in minutes).
4. (Optional)The lowest bound of the Date range (string format: dd/mm/yy 22:00:00).
5. (Optional)The uppest bound of the Date range (string format: dd/mm/yy 22:00:00).

## Examples

The following line will output all the chars with the whole data extracted, showing an interval of 30 minutes in the X-axis. **Take into account that if the data is too large, and the interval is too low, the chart may not be work correctly. If this happens, try increasing the interval value**

```msdos

dataVisualizator.exe "C:\Users\Guest\windbg_output.txt" "C:\Users\Guest\DVF_output\" 30

```

Let's suppose that we have a big file that was running the whole weekend (Fri 12/9 to Sun 14/9), but we want to analyze a particular part of the Saturday, between 16 and 17.
The following line will create a chart with the writes performed during Saturday between 16 and 17 with an interval of 2 minutes.

```msdos

dataVisualizator.exe "C:\Users\Guest\windbg_output.txt" "C:\Users\Guest\DVF_output\" 2 "13/09/18 16:00:00"  "13/09/18 17:00:00" 

```