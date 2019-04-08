from file_titles import titles
import os
import re


class LogParser:
    def __init__(self, file_name, file_format):
        self.file_name = file_name
        self.format = titles[file_format]['log_format']
        self.rex =  titles[file_format]['regex'][0]
        self.Read_file(self.file_name)


    def Read_file(self,file_name):
        try:
            f = open(self.file_name, "r")
            i = 0
            for line in f:
                i+=1
                #print("\n\n")
                l = re.findall(self.rex, line)
                #print(l)
                print("-------------------")
                size = len(self.format)
                l[size-1] = ' '.join(l[size-1:])
                del l[size:]
                #print(l)

                for k,v in zip(self.format,l):
                    print(k + " : "+ v)
                    print()

                if i==5:
                    break

        except Exception as e:
            print(e)


    def display(self):
        print("self.rex  : ", self.rex)
        print("self.format  : ", self.file_format)

