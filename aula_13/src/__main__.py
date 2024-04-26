# main
import time

import schedule
from lib.classes.CsvSource import CsvSource

# from lib.classes.JsonSource import JsonSource
from lib.classes.TxtSource import TxtSource

csv_source = CsvSource()
txt_source = TxtSource()
# json_source = JsonSource()


def check_for_new_files():
    """
    Check for new files in different data sources.

    This function checks for new CSV, TXT, and JSON files in their respective data sources.
    """
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    # json_source.check_for_new_files()


# Scheduling the execution of the check_for_new_files function every 10 seconds
schedule.every(10).seconds.do(check_for_new_files)

# Main loop
while True:
    schedule.run_pending()
    time.sleep(
        1
    )  # Waits for 1 second to prevent the loop from consuming too much processing power
