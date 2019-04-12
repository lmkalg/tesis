Controllers have several tasks:
* Define size and location of the log files.

* Start/Stop event tracing sessions.
* Enable providers (so they can log events to a particular session).
* Manage the size of the buffer pool.
* Obtaing execution statistics for sessions (number of buffers used, number of buffers delivered, etc.). More info:  [Controlling Event Tracing Sessions](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363881(v=vs.85).aspx)
