#!/usr/bin/python 

from __future__ import print_function

# TODO: add color
# TODO: update author name and verssion
__author__="Mahdi Abdinejadi <mahdi.abdinejadi@hiq.se>"
__version__= "0.0.2"
__licence__ = "MIT"


# TODO:  Please update this doc string
"""
Simple command line python template
"""


from dateutil.parser import parse
from subprocess import Popen, PIPE, STDOUT
import time, os, logging, signal
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter



def strtosec(strtime):
	""" Simple string to time parser.

	This function get time string and parse it to seconds.

	Args: 
		strtime (str): unix like time stamp

	Returns:
		t (int): seconds of time passed
	
	Raises:
		ValueError: if strtime is not possible to parse; then kill the process with signal 1.
	"""
	try:
		t = parse(strtime)
		return time.mktime(t.timetuple())
	except ValueError:
		logging.error("Can not parse '%s' to date. You may have to set carmen version by --r20 ", strtime )
		exit(1)

# TODO: rename the function 
def somecallfunctions():
	""" This function is template to write system call functions

	This fuction is using subprocess module to call system or os applications. 

	"""
	try:
		command = "uname -a" # TODO: Update the command
		ps_raw = Popen(command, stdout=PIPE, stderr=PIPE)
		ps_result, ps_err = ps_raw.communicate()
		if ps_err:
			logging.error("Command Error: " + ps_err.strip())
	except OSError as e:
		logging.error("OS error: " + e.strerror)
	except:
		logging.error("Error ...")


def cvs_writer(csv_output, csv_map, csv_header):
	""" This is simple cvs file writer

	This function write cvs file as output.

	Args:
		csv_output (str): file name of csv file
		csv_map (list):  list of tuples which contains row of CVS
		csv_header (list) : list of keys of CSV

	"""
	import csv
	try:
		csv_file = open(csv_output, "w")
		logging.debug("csv_file is: " + str(csv_file))
		csv_writer = csv.DictWriter(csv_file, csv_header)
		logging.debug("csv_writer is ready: "+ str(csv_writer))
		csv_writer.writerow(dict(zip(csv_header,csv_header)))
		for i in csv_map:
			csv_writer.writerow(dict(zip(csv_header, i)))
		
		logging.debug("csv_writer is done: "+ str(csv_writer))
		logging.info("cvs file is created")
	except IOError as e:
		logging.error("IO error: " + e.strerror)
	except:
		logging.error("CVS writing error")


def to_json(json_dictionary):
	""" This simple function to dump dictionary to json string.
	Simply pass a dictionary to this function and get json string.

	Args:
		json_dictionary (dict): dictionanry to converted to json formated string.

    Returns:
		json_dump (str): json_formated string
    """
	import json
	logging.info("print sessions to stdout with json format")
	print(json.dumps(sessions))


# TODO: write the main execution code here
def execution():
	""" This is the main execution function in this module and it ...

	This function ...

	Args:
		
	"""
	
	logging.info("Job is done")

# TODO: Add desired argument and check them if it necessary
def run():
	""" This function parse and check or set all variables to execute the module execution function.
	
	This function first set all argparser variables and then try to parse them. There are some values that need to be
	set with default values. It also initialize logging object class according to argparser values which are set by user.
	And finally, it calls the execution function with proper values.

	"""
	ap = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
	ap.add_argument('-e', '--environment', help='set environment to prod or test. Default value is running host environment')
	ap.add_argument('-f', '--filter', help='set filter for username or alert generator running host')
#	ap.add_argument('-n', '--new', default=False, action='store_true', help='set to run...')
	ap.add_argument('-o', '--output', help='set filter for username or alert generator running host')
	ap.add_argument('-v', '--verbos', default=False, action='store_true', help='set logging to verbos (debug level)')
	ap.add_argument('-j', '--json', default=False, action='store_true', help='set print out result as json') 
#	ap.add_argument('-m', '--min_something', type=int, default=1, help='set ..,')
	

	args = ap.parse_args()

	if args.verbos:
		loglevel = logging.DEBUG
	else:
		loglevel = logging.INFO
	if args.output:
		if os.path.basename(args.output).split('.')[-1] == "csv":
			logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
		else:
			logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel, filename=args.output, handlers=[logging.StreamHandler])
			args.output = "" # making sure that args.output value is only CSV file other file formats will handle by logger module
	else:
		logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
	
	if args.environment == 'prod':
		logging.info("environment is prod")
	elif args.environment == 'test':
		logging.info("environment is test")
	elif args.environment == 'dev':
		logging.info("environment is dev")
	else:
		logging.error("Invalid environment value")
		exit(1)

	logging.info("ArgumentParser is done")
	# TODO: Pass required variable to execution function
	execution()


def handler(signum, frame):
	""" This fucntion handles signals

	This is simple signal handler. To check other type of signals go to:
	https://docs.python.org/2/library/signal.html#signal.getsignal


	"""
	print ('Signal handler called with signal', signum)
	exit(1)


if __name__ == '__main__':
	""" Main function to report start and end time and run the main function run()
		Signal handler is registered here as well.
	"""
	start_time = time.strftime("%c")
	signal.signal(signal.SIGINT, handler) # Register signal 
	run()
	end_time = time.strftime("%c")
	logging.info("End of the execution at %s and took: %0.2f seconds.\n\n" %  (end_time, strtosec(end_time) - strtosec(start_time)))


