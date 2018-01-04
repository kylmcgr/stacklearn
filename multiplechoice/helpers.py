""" helpers.py
    Helper functions for the multiple choice app.
    Currently is a similar to helper from mathstack and likely doesn't work
"""

import random

def compute_answer(q_text):
    """ Method to ingest the raw text of a question, e.g., "10 % 2 == 0",
    and return the right answer.  Raises a `RuntimeError` if an unknown
    question format is encountered.  
    Expected question types are divisibility and multiplication questions.
    """
    if "%" in q_text:
        return eval(q_text)  # returns a Boolean
    elif "*" in q_text:
        return eval(q_text)  # returns an integer
    else:
        raise RuntimeError("Unknown question format; can't parse.")


def get_next_q():
    """ Method to generate a random math question and return it as a string.
    Presently generates multiplication questions only.
    """
    LOWER = 10
    UPPER = 5000
    op1 = random.randint(LOWER, UPPER)
    op2 = random.randint(LOWER, UPPER)
    q_text = "{op1} * {op2}".format(op1=op1, op2=op2)
    return q_text

def parse_question(q_text):
    """ Ingests a question string and returns a dictionary.
    """
    q_dict = {}
    q_items = q_text.split(" ")
    if "*" in q_items:
        q_dict["mult1"] = q_items[0]
        q_dict["mult2"] = q_items[2]
    return q_dict
