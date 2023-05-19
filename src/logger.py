# Logger -  is purpose for any execution that probably happens should be able to log all those information in some files ---
# --- so that we will be able to track if there is some error ,even the custom exception error we will try to log that into the text file
# --
import logging
import os
from datetime import datetime

# Now we will create our log file
# basically how my log file should basically get created
# So my file name that would be created would be whatever datetime is bascially coming and further this will basically have --
# -- month , day , year , hours .log file
# So its basically a text file in this naming convention it willl get created
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# and with respect to log path bcoz we need to give the log file
# So if we probably see with respect to joins my file name should logs in forward and then this naming convention - LOG_FILE
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)


# SO whatever logs will get created it will with respect to current working directory
# and every file name will start with logs along with whatever file name is basically coming

os.makedirs(logs_path,exist_ok=True)
# So this basically says that even though there is a file , even though there is a folder keep on appending that inside it


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


# Now whenver we really want to create the log right we need to set --
# See if you want to overwrite this functionality of logging we have to probably set up in the basic config
logging.basicConfig(
# So you will first give the file name where you want to basically save it
# Here we'll be giving the log file path with respect to the file name
filename = LOG_FILE_PATH,
# Then the Format what format we want to specifically use
# This is how my entire message will get printed
format = "['%(asctime)s'] %(lineno)d %(name)s - %(levelname)s - %(message)s",
# after this we say for which level of in the case of INFO only we are going to print this specific messages
level = logging.INFO,

)






#===================================================================================================================#

# Just for cross checking or you can say for testing purpose below code

#===================================================================================================================#



# We are just trying to check if everything is working fine or not
# if __name__=='__main__':
#     logging.info("Logging has started")
#
# # Now as soon as we write this to check everything is working fine over here or not
# # Over her in logging.basicconfig you can see my file name is basically with respect to the log_file_path
# # So in the cwd you'll be able to see log folder is created and inside it the file is created --
# # -- which is .log file and then we are able to see the print message "Logging has started "
# # & after INFO my message has got printed bcoz over her in the format i have mentioned levelname ,--
# # -- message , name , linenumber(lineno)
# # asctime -ascending time
# # lineno - 45 (in our case) where we have specifically used logging.info
# # & then name which is - root (name)
# # after that INFO is there
# # & then finally message is there
