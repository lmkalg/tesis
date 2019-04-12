# Timeline

## March

* **19/03:** First day at the office. Meet with Mathias. Just signing some papers. Using my PC. Starting procedure to open a bank account
* **20/03:** Meet Alex at the office. Start reading the PDF he gave me. Still using my PC because. Don't have corporate access yet.
* **21/03:** The PC has arrived. Installing all the stuff. Continue reading the PDF. Propose the idea to Alex of developing the windbg script to cross EtwRegister and EtwWrites.
* **22/03:** Went to the other part of the office (my place). Start playing a little with WINDBG. Started implementing the IT policy to join the corporate network.
* **23/03:** Alex approved my pc to join the network and helped me configure the mail and stuff. Anyways, I'm still waiting for the keys to connect to the network.
* **25/03:** Kai gave me the VPN keys. I started using them while I start trying to start the windbg script. WINDBG scripting sucks. It really sucks.
* **27/03:** Start developing a Python framework to help me parse the output of the windbg scripts.
* **28/03:** Reversing some stuff to get useful information for scripts.
* **29/03:** Matthias came and told me that a guy will make a pentest against my pc (they didn't understand why I was already connected to the vpn) all the day hardening my PC.
* **30/03:** HOLIDAY

## April

* **02/04:** HOLIDAY
* **03/04:** Continue Reversing stuff to understand the structures of GUID and Handler and how they work.
* **04/04:** Improving the scripts, with the new information gathered from reversing, of crossing EtwRegister and EtwWrites call, with GUIDS related with Telemetry
* **05/04:** What if we can relate the session somehow with the provider at the moment of writing? It should be some way...
* **06/04:** Reversing stuff to understand how this relationship can be accomplished
* **09/04:** Initial script develop. But isn't working. Why?
* **10/04:** Reversing again. Get with the answer why is not working.
* **11/04:** Developing updated scripts.
* **12/04:** Developing updated scripts.
* **13/04:** Finished developing both WINDBG scripts
* **16/04:** Started getting useful information from the scripts we run. IN the meantime, reversing one call stack arbitrary chosen
* **17/04:** Continue reversing the call stack.
* **18/04:** Meeting with Alex. We defined the workload. I'll shift from reversing our first Trigger to develop a software to parse & visualize data extracted from the WINDBG scripts in a better way. I already have my FW in Python but due to this must run in native windows---> C# or Powershell..which one??!! C#!. Finish parsing Date.
* **19/04:** Finished parsing the input with the new C# framework. Updated windbg scripts with the new Place Holders. Trying to find a better backup solution, because BORG doesn't have incremental. Ones. So far, no luck.
* **20/04:** Ended printing chart of Writes per minute. At least v1.0. What else can we develop? Chart of how Guids have wrote during time? ( With different lines per GUID?)
* **23/04:** Improve the way we show the chart of Writes per minute (added some conditions to make zoom in desired parts. ). I've modularized a little the part between the Parser and the Data visualization itself (writing the data to a file in json format). Created an .html output . Generating there some statistics
* **24/04:** Add a way to "scan" the windbg script output and trim it if isn't well formatted.  Added log in a lazy way (should be improved). Made documentation on how to use it. Add parsing with names
* **25/04:** Remove parsing with names due to is not natively supported. Add receiving path to print info windbg script by parameter in the first script. Add the capability of writing EACH write with the corresponding date and the call stack used. Started trying to reverse a little bit our first Trigger again. NtPowerInformation
* **26/04:** Continuing reversing.
* **27/04:** Continuing reversing. Understand a little bit more about the thing about the handler but still can get the object.
* **30/04:** Update with Alex. Discover relation ship of Power manager with devices. Keep Reversing. Discover relationship of Audio device. Develop trigger. 1ST TRIGGER DEVELOPED =)

## May
    
* **02/05:** Very bad news. I wasn't sure if our approach was really logging the writes of the Telemetry. The thing is that I issued the command to read them from Windbg (**!wmitrace.eventlogdump 0x22**) and the result was very bad. The amount of events was orders of magnitude smaller than the ones we get. I started trying to reverse and understand why our approach is not working. Without luck so far.
* **03/05:** Start reversing EtwpEventWriteFull to understand what is happening and why the events that we were detecting with our strategy are not being logged to the buffer of the Diagtrack Listener session. I kinda understood how the EnableInfo works as reference to know which sessions should we pay attention to.
* **04/05:** Continue reversing. Today I get what **__readgsqword()** means. Also I achieve the part where some functions related to the buffers are being called. Anyways, there is a pretty weird OFFSET that is not letting me understand what kind of structure is being accessed (and it seems that is needed to know it).
* **07/05:** Internal workshops day I. I was all the morning there. At 14.00 I started continuing with the work. 
* **08/05:** Internal workshops day II. I started the day working. I finally get the point were the buffer is being written!!. And I was able to check that the content was there. I'll join the IWS now, in the block of the morning.
* **09/05:** Internal workshops day III. I finished with the reversing of the important part for us of the EventWriteFull functionality. I could detect the names of the variables, how are the events being logged, and have in considerable details what each variable does
* **10/05:** HOLIDAY
* **11/05:** Amazing day. I figure it out which was the REAL BUG that was causing a lot of problems. This changes a lot the game. I should leave another analysis running due to the previous ones were not that exactly good. Realize that the trigger I developed isn't going to work, but anyways I detected another one. We may change the place were we set the breakpoints due to there is one place that we could get more information. Analysis is required.
* **14/05:** Realized (by setting a breakpoint in EtwpReserveTraceBuffer) and printing the call stack, that the etwpeventwritefull wasn't the only function writing things related to the telemetry session. Next step, leave this script running 1day to try to identify other functions besides the two found. Defined some deadlines.
* **15/05:** Fully reversing EtwpEvenWriteFull. Understood a little more how the whole payload is written. Two ways of showing the data logged, json and xml.
* **16/05:** Understood how to get the last event logged. Already changed both scripts, etwpeventwritefull and etwpeventuserwrite
* **17/05:** Modifying the FMW to support the event information also. UNSOLVED BUG.. REPETAED JSON_BODY IN THE WIDNBGSCRIPT OUTPUT
* **18/05:** Fixing errors in the windbg scripts and in the FMW. Each test is sooo slow due to we have to wait for the telemetry and so on.
* **21/05:** HOLIDAY
* **22/05:** Continuing with some testing of the windbg scripts. Modifying the framework to show some other useful information such as the amount of times that some particular event ID related with a provider, was used, etc.
* **22/05:** Developed two triggers. One for each function. Continue testing the windbg scripts. Setting a meeting with Thomas for next Monday/Wednesday. Aleks came today, I showed him some advances, he told me he is going out for two weeks. I remembered him that the 8th of June was my last day here. He seemed surprised.. but well... he returns the 7th, so we have only two day to meet. That's why I had to set up the meeting with thomas. 
* **23/05:** Trying to develop the third trigger. I tried to figure it out if making a app to crash, following the etwsendnotifiaction function flow, or others possiblities are giving me some information but they don't. 
* **24/05:** Keep looking how to implement a new trigger. Nothing found. talk little to Thomas, I have a though that the events will be very different.
* **25/05:** Comparing the data (amount/type of events, etc) that each developed trigger is showing in each of the 4 levels of telemetry.
* **28/05:** Didn't come to work. Airport problem
* **29/05:** Arrive at noon After the problem. Analyzing output of 4 days of logging calls to reserve buffers. Developed a trigger which triggers event for security (OneDrive), an another trigger (action center) which triggers 1 event for basic
* **30/05:** Meeeting with Thomas. We tried to set up and environment to compare the events, but we failed. Then we realized that it wasn't necessary. Just is needed to use the Message Analyzer and a single line command to register a new session with some providers.
* **31/05:** HOLIDAY


## June
* **01/06:**: Doing some testing to ensure that our events were the same as the gathered by the XPERF and stored in the etl file. 
* **04/06:**: Full analayziss between 11 events of notepad between my winbg scripts and the message analyzer. Two of the triggers are not working anymore. The onedrive one, is triggering the event after a couple of seconds maybe minutes. The actioncenter, isn't working at all. New fresh installation to test them their. Onedrive isnot working becuase the automatic update task is missing from the system. The actioncenter, is working again. The other triggers, are working perfectly. Whyyy? Maybe something related with the amount of events already sent? because they're not connected to the internet? Why isnot installed the task.  
* **05/06:**: Fixed executer. Capture the execution plan with the Performance analyzer. Adding the providers to the cmd, all the events are there (the important ones, and more). The windbg script way, is much more accurate.
* **06/06:**: Discover a NEW trigger. Related with USB. IT needs a USB connected and uses Powershell. 
* **07/06:**: Added the possiblity of executing a power shell script to Executer. It was really hard don't know why. Also start checking how many events does this new USB trigger was logging if we execute a couple of times. Improved a little the PS script for the USB trigger. Sent an mail to Aleks in order to set a meeting for today due to Tomorrow is my last day here, but never answer back. Maybe he is still in holidays (N). Returned the cellphone together with the chip and stuff. 


* **20/06:**: I added internal_delay, external_delay and parameters to the executions features.. Also added a function for using as testing, to print the parameters parsed.