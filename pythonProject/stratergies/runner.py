import time

import nse_realtime
import superseuperET as superseuper
import schedule
from serviceagent import cleaner


def call_nse_scanner():
    nse_realtime.execute_nse_scanner()


def call_super_se_uper():
    superseuper.call_super_se_uper()


def file_cleaner():
    cleaner.clean_txt_files()


# Monday
schedule.every().monday.at("03:50:00").do(call_nse_scanner)
schedule.every().monday.at("03:55:00").do(call_nse_scanner)
schedule.every().monday.at("04:00:00").do(call_nse_scanner)
schedule.every().monday.at("04:15:00").do(call_nse_scanner)
schedule.every().monday.at("03:51:00").do(call_super_se_uper)
schedule.every().monday.at("03:56:00").do(call_super_se_uper)

# Tuesday
schedule.every().tuesday.at("03:50:00").do(call_nse_scanner)
schedule.every().tuesday.at("03:55:00").do(call_nse_scanner)
schedule.every().tuesday.at("04:00:00").do(call_nse_scanner)
schedule.every().tuesday.at("04:15:00").do(call_nse_scanner)
schedule.every().tuesday.at("03:51:00").do(call_super_se_uper)
schedule.every().tuesday.at("03:56:00").do(call_super_se_uper)

# Wednesday
schedule.every().wednesday.at("03:50:00").do(call_nse_scanner)
schedule.every().wednesday.at("03:55:00").do(call_nse_scanner)
schedule.every().wednesday.at("04:00:00").do(call_nse_scanner)
schedule.every().wednesday.at("04:15:00").do(call_nse_scanner)
schedule.every().wednesday.at("03:51:00").do(call_super_se_uper)
schedule.every().wednesday.at("03:56:00").do(call_super_se_uper)

# Thursday
schedule.every().thursday.at("03:50:00").do(call_nse_scanner)
schedule.every().thursday.at("03:55:00").do(call_nse_scanner)
schedule.every().thursday.at("04:00:00").do(call_nse_scanner)
schedule.every().thursday.at("04:15:00").do(call_nse_scanner)
schedule.every().thursday.at("03:51:00").do(call_super_se_uper)
schedule.every().thursday.at("03:56:00").do(call_super_se_uper)

# Friday
schedule.every().friday.at("03:50:00").do(call_nse_scanner)
schedule.every().friday.at("03:55:00").do(call_nse_scanner)
schedule.every().friday.at("04:00:00").do(call_nse_scanner)
schedule.every().friday.at("04:15:00").do(call_nse_scanner)
schedule.every().friday.at("03:51:00").do(call_super_se_uper)
schedule.every().friday.at("03:56:00").do(call_super_se_uper)

schedule.every().sunday.at("13:17:00").do(call_super_se_uper)
schedule.every().sunday.at("13:15:00").do(call_nse_scanner)

# file_cleaner();
# call_super_se_uper()
# call_nse_scanner()
while True:
    schedule.run_pending()
    time.sleep(1)
