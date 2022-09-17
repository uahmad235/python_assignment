"""Functionality to handle error logs in a decorator"""
import contextlib
import sys, traceback
import datetime as dt


OUT_FILE = "errors_task4_.txt"  # errors logs output file path


def get_datetime():
    """returns current datetime in `DAY/MONTH/YEAR HOUR:Minute:Second` format"""
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def ErrorLogsDecorator(fn):
    """A decorator that pipes the error stream into a file with current timestamp"""

    def wrapper(*args, **kwargs):
        fdesc = open(OUT_FILE, "a")

        with contextlib.redirect_stderr(fdesc):  # Contextlib for handling standard error outputs
            try:
                return fn(*args, **kwargs)
            except Exception:
                print("Exception occured on: ", get_datetime(), "\n", traceback.format_exc(), file=sys.stderr)
            finally:
                fdesc.close()  # closing file descriptor in either case
    return wrapper
