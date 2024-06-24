# Moonshot_Assessment
Moonshot Technical Assessment

## Instructions

1. The Python script for the project is present in the Moonshot_Technical_Assessment.py file which can be run through the command line.

2. Moonshot_Technical_Assessment.ipynb is the Jupyter Notebook which can be referred to view the intermediate outputs of the script.

3. To run the script locally, the following modules are needed -
     + db-sqlite3==0.0.1
     + pandas==2.2.2
   
4. To install the required modules, please navigate to the directory where the requirements.txt file and the Python script are present and run the below command on the command line -
     
       pip install -r requirements.txt
   
6. The input CSV file must be present in the input directory.
   
7. Once the installation is complete, the Python script can now be run using the below command -
   
          python Moonshot_Technical_Assessment.py <input_file_name.csv>
    + Eg. -> For demonstration purposes, we have "input.csv" present in the input directory. To run the script, please use the below command - 

          python Moonshot_Technical_Assessment.py input.csv

9. The script will calculate the word frequency and store the output in an SQLite(disk-based) Database called "Word_Frequency.db" and also create an "output.csv" file. The processed input file will then be moved to a new directory "processed".

