#!/usr/bin/env python3
import sys
import re
import os

log_dict = {}

if os.access(sys.argv[-1], os.R_OK):
    fin = open(sys.argv[-1], "r")
    if os.path.getsize(sys.argv[-1]) != 0:
        if len(sys.argv) <= 4:
            for line in fin:
                line = line.rstrip('\n')
                fields = re.split(' ', line)
                #print(fields)
                program_name = fields[3]
                memory_size = int(fields[1])
                cpu_time = int(fields[2])
                process_id = fields[0]
                if program_name in log_dict:
                    log_dict[program_name][0] += process_id
                    log_dict[program_name][1] += memory_size
                    log_dict[program_name][2] += cpu_time
                else:
                    log_dict[program_name] = [process_id, memory_size, cpu_time]
            if sys.argv[1] == '-a' and len(sys.argv) == 3:
                for keys_item in sorted(log_dict): 
                    print(log_dict[keys_item], keys_item)
            elif sys.argv[1] == '-m' and len(sys.argv) == 3:
                sum_total_memory = 0
                for program in log_dict:
                    sum_total_memory += log_dict[program][1]
                print('Total memory size:', sum_total_memory, 'KB')
            elif sys.argv[1] == '-t' and len(sys.argv) == 3:
                sum_total_cpu_time = 0
                for program in log_dict:
                    sum_total_cpu_time += log_dict[program][2]
                print('Total CPU time:',sum_total_cpu_time,'seconds')
            elif sys.argv[1] == '-s' and len(sys.argv) == 4:
                count = 0
                for program in log_dict:
                    if log_dict[program][1] >= int(sys.argv[2]):
                        print(log_dict[program], program)
                        count += 1
                if count == 0:
                    print('No processes found with the specified memory size')
                    
            elif sys.argv[1] == '-v' and len(sys.argv) == 3:
                print('Name: Javier')
                print('Surname: Chapto')
                print('Student id: 14081525')
                print("Date of completion: 14/10/2022")
            else:
                print("Error: Incorrect argument sintax")
                sys.exc_info()[0]
        else:
            print("Error: Incorrect argument sintax, too many arguments")
            sys.exc_info()[0]        
    else:
        print('No processes found')    
else:
    print("Error: file reading not possible")
    sys.exc_info()[0]
