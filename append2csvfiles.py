#-------------------------------------------------------------------------------
# Name:         append2csvfiles.py
# Purpose:      Join a csv row with another when sharing a common first column
# Author:       Linda Ackers
# Created:      11/29/2017
# Comments:     Use Notepad ++ to convert csv files to utf8 (Chinese chars etc) before running script
# Comments:     Script takes minutes to complete.  Wait for: "Finished. Files are now closed."
# Todos:        Get input (file names) from user, get input (column numbers) from user,  
# Todos:        write try/except, output to screen that script is still running,
# Todos:        write functions for file open etc.  Create C# program
#-------------------------------------------------------------------------------

import csv
match_list = []


with open('file1.csv',  'r', encoding='utf8') as csv1_file: #open first file 
    csv1_reader = csv.reader(csv1_file)
    csv1_first_row = next(csv1_reader)#get number of columns in first file    
    csv1_num_cols = len(csv1_first_row)
    #print (csv1_num_cols) #print number of columns
    csv1_row_count = len(list(csv1_reader)) #number of rows in first file
    print ('Number rows file 1:',csv1_row_count)
    
    csv1_file.seek(0) #return pointer to the beginning of the file !important
    with open('file2.csv', 'r', encoding='utf8') as csv2_file: #open second file
        csv2_reader = csv.reader(csv2_file)
        csv2_first_row = next(csv2_reader)#get number of columns in second file
        #print (csv1_first_row + csv2_first_row) #debug show MMSID both files
        csv2_num_cols = len(csv2_first_row)
        #print (csv2_num_cols) #print number of columns
        total_cols = csv1_num_cols + csv2_num_cols
        #print (total_cols) #debug
        csv2_row_count = len(list(csv2_reader)) #number of rows in first file
        print ('Number rows file 2:',csv2_row_count)        
        
        with open('newfile.csv', 'w', encoding='utf8', newline='') as new_file: #create csv file to write
            new_csvwriter = csv.writer(new_file, delimiter='|')                    
            #write matching mms id (first column) to file            
            for csv1_col in csv1_reader:
                csv2_file.seek(0) #return pointer to the beginning of the file !important
                for csv2_col in csv2_reader: #loop second file
                    if csv1_col[0] == csv2_col[0]: #compare first file, first column with seccond file, first column
                        new_csvwriter.writerow(csv1_col + csv2_col)
                        match_list.append (csv1_col[0])
                        
            #write unmatching mms id from first file to file        
            csv1_file.seek(0) # return cursar to the begining of the file
            next(csv1_reader) #remove header row from file before loop
            for csv1_col in csv1_reader: #write contents of second file that didn't match
                #check array - if not in array, write to file
                print (csv1_col)
                if csv1_col[0] not in match_list:
                    new_csvwriter.writerow(csv1_col + [''] * csv2_num_cols)
                    
            #write unmatching mms id from second file to file 
            csv2_file.seek(0) # return cursar to the begining of the file
            next(csv2_reader) #remove header row from file before loop
            for csv2_col in csv2_reader: #write contents of second file that didn't match
                #check array - if not in array, write to file
                print (csv2_col)
                if csv2_col[0] not in match_list:
                    new_csvwriter.writerow([''] * csv1_num_cols + csv2_col)
print ('Finished. Files are now closed')