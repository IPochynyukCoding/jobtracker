import platform
import sqlite3
import subprocess
import os
from helper_functions.display_table import create_table
from helper_functions.job_functions import add_job,modify_job
from helper_functions.create_database import database_creation
is_windows= True if platform.system()=="Windows" else False
clear_command = "cls" if is_windows else "clear"

if __name__ == "__main__":
    if not os.path.exists("jobs.db"):
        print("Jobs database not found, creating database...")
        database_creation()
    job_connector=sqlite3.connect("jobs.db")
    job_cursor=job_connector.cursor()
    functions=[create_table,add_job,modify_job]
    while True:
        selection=input("Press 1 to display table, 2 to add a job, 3 to update a job, or 'q' to quit: ")
        if selection.lower()=="q":
            quit()
        try:
            numbered_selection=int(selection)-1
            functions[numbered_selection](job_cursor,job_connector)
            clearing=subprocess.run([clear_command],check=True,shell=True)
            try:
                clearing.check_returncode()
            except subprocess.CalledProcessError:
                print("Unable to successfully clear")
                quit()
        except(ValueError,IndexError):
            print("Invalid selection, please try again!")

