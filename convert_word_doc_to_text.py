#!/usr/bin/env python3

import os
import uuid
import textract

source_directory = os.path.join(os.getcwd(), "source")

training_directory = os.path.join(os.getcwd(), "output")

for process_file in  os.listdir(source_directory):
    file, extension = os.path.splitext(process_file)
    
    # We create a new text file name by concatenating the .txt extension to file UUID
    dest_file_path = file + '.txt'
    
    #extract text from the file
    content = textract.process(os.path.join(source_directory, process_file))
    print(content)
    
    # We create and open the new and we prepare to write the Binary Data which is represented by the wb - Write Binary
    write_text_file = open(os.path.join(training_directory, dest_file_path), "wb")
    
    #write the content and close the newly created file
    write_text_file.write(content)
    write_text_file.close()