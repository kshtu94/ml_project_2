# So any exception that is bascially getting controlled the sys library will automatically have that information
import sys
# Lets alos import the Logging to check whether everything is working fine or not
import logging
# from src.logger import logging

# Whenver an exception get raised i want to push my own custom message
# The first parameter is -  whatever error or message i am getting
# The second param is  -  error_detail will basically will be present inside this sys
                         # (What module we are basically importing)
def error_message_detail(error, error_detail:sys):
    # The return type of sys
    # Like if we probably write error_detail.exc_info
    # This is basically talking about exception info and this will give you three important information ---
    # --- the first two information we are not at all interested  but last information will give me exc_tb=
    # this variable that is there , this info will probably give you info on which file the exception has ---
    # --- occured , which line no the exception has occured all those information will be particularly stored in
    # this varibale -> exc_tb from this exc_info()
    _,_,exc_tb=error_detail.exc_info()
    # In which file name i'm probably getting this error
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Now we create a varibale -> error_message and we probably write any errors -- saying "any message with some placeholders inside it"
    error_message = "Error occured in python scripts name [{0}] line number [{1}] error message [{2}]]".format(
    file_name , exc_tb.tb_lineno , str(error)
    # Zeroth palceholder will basically have file name
    # First placeholder will basically have the line number using execution tab ->exc_tb.tb_lineno
    # Third Parameter which is there that is basically my error message -> str(error) ---
    # --- and this error is nothing but what error we are getting as  a parameter in the function
    )

    return error_message

# So basically whenever my error raises i am going to call this particular function
# So create a class which is my ow Custom Exception class
class CustomException(Exception):
    # obviously we need to also give it which is my constructor
    # Here i will give whatever message i haev for my error and error_detail of sys file
    def __init__(self,error_message,error_detail:sys):
        # Since we are basically inheriting from the exception so we basically write super.__init__ --
        # -- bcoz we need to inherit the init function
        # So we are basically writing error_message over her and we are bascially able to probably inherit the exception class
        # with respect to it
        super().__init__(error_message)
        # So we are intializing our error_message with the above function with it as currently it won't be having anything in it
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    # So here we will also inherit one functionality in custom exception that is underscore str underscore
    def __str__(self):
        return self.error_message


# So whenever we raise this CustomException first of all it is inheriting the parent Exception --
# -- so whatever error message is coming from this particular function (error_message_detail) --
# -- will come over here and get initialized to the class variable or custom exception variable that is self.error_message--
# -- or you can say error_message
# and this error_detail is being basically dragged by sys







#===================================================================================================================#

# Just for cross checking or you can say for testing purpose below code

#===================================================================================================================#

# Now for testing purpose
# if __name__=='__main__':
#     # So we will use a try catch block
#
#     try:
#         print(x)
#     except NameError as n:
#         print(n)
#
#     try:
#         a=1/0   # So obviously i'm going to get an exception
#         # Here we are not passing error_message
#         # and this e would be provided as my first parameter
#         # Along with that i'll provide sys
#     except ZeroDivisionError as e :
#
#         logging.info("Divide by Zero") # So this would be divide by zero error
#         raise CustomException(e,sys)


# The file with the Zero Division Error was not getting logged bcoz you were not importing from src.logger import Logging
# That will get updating this logging.info("Divide by Zero")
# Now you can see that your file of logging consists all the logs with the current error
# Now whenever you want to update logging ---- you have to import from source.logger import logging
