Preconditions:
- linux environment, or WSL (Windows Subsystem for Linux) if Windows is the operating system.
- python3 installed: sudo apt install python3 -> will install the latest version for python3 (3.10.12)
- csv and datetime modules are already installed, because they are both part of Python's standard library


Steps:
1. The content of input file (logs.log) is stored into a matrix, and each line is a list.
2. Based on created matrix we will create other matrices, based on requirements and all corner cases.
3. Print all matrices created at step 2
4. Generate required report file


Run: 
- in Linux terminal query the following command -> "python3 test.py"
- the output will be printed in terminal, listing all jobs with their start time, end time, total time, pid
- an output.txt file will be created, it is the required report with jobs that took more than 5 minutes or
10 minutes to be executed