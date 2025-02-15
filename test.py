import csv
from datetime import datetime

# Variables
matrix = []            # matrix created to store file content
finished_tasks = []    # matrix that will have details about all finished tasks/jobs
unfinished_tasks = []  # matrix that will have jobs with start time and no end time
unstarted_tasks = []   # matrix that will have jobs with end time and no start time (sounds weird, but just in case...)
time_format = '%H:%M:%S'

# Open the .log file as a CSV file
with open('logs.log', newline='') as log_file:
    reader = csv.reader(log_file)
    for row in reader:
        matrix.append(row)

for line1 in matrix:
    unique_pid = True
    for line2 in matrix:
        if line1[3] == line2[3] and line1[2] == ' START' and line1 != line2:
            aux_list = []   # aux_list = [name, start_time, end_time, time_diff, pid]  --> each element of finished_tasks matrix
            aux_list.append(line1[1])
            aux_list.append(line1[0])
            aux_list.append(line2[0])

            start_time = datetime.strptime(line1[0], time_format)  # convert string into datetime object
            end_time = datetime.strptime(line2[0], time_format)    # convert string into datetime object
            spent_time = end_time - start_time                     # calculate the time difference, in seconds
            spent_time = int(spent_time.total_seconds())           # the output were a float number, like "7.0"

            aux_list.append(spent_time)
            aux_list.append(line1[3])
            finished_tasks.append(aux_list)

        if line1[3] == line2[3] and line1 != line2:
            unique_pid = False

    if unique_pid:
        if line1[2] == ' START':
            unfinished_tasks.append(line1)   # append the whole line, as it appears in logs.log
        elif line1[2] == ' END':
            unstarted_tasks.append(line1)    # append the whole line, as it appears in logs.log
      
# Print our work
print("Finished tasks (name, start_time, end_time, total_seconds, pid):")
for line in finished_tasks:
    print(line)

print("Unfinished tasks (start_time, name, status, pid):")
for line in unfinished_tasks:
    print(line)

print("Unstarted tasks (start_time, name, status, pid):")
for line in unstarted_tasks:
    print(line)

# Create output report
with open('output.txt', 'w') as file:
    for line in finished_tasks:
        if line[3] > 300 and line[3] < 601:
            file.write(f"WARNING: Job '{line[0]}' took longer than 5 minutes. Duration: {line[3]}.\n")
        elif line[3] > 600:
            file.write(f"ERROR: Job '{line[0]}' took longer than 10 minutes. Duration: {line[3]}.\n")
