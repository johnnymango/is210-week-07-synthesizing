#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module finds game match partners."""


def get_matches(players):
    """This function uniquely matches 2 players togther.

    Args:
        players (list): A list of strings representing player names.

    Returns:
        Tuple: A two item tuple matching 2 players together.

    Examples:
        >>> get_matches(['jack', 'jill', 'bob'])
        [('jack', 'jill'), ('jack', 'bob'), ('jill', 'bob')]

        >>> get_matches(['jack', 'jill', 'bob', 'billy'])
        [('jack', 'jill'), ('jack', 'bob'), ('jack', 'billy'), ('jill', 'bob'),
        ('jill', 'billy'), ('bob', 'billy')]
    """
    mylist = []
    for idx1, player1 in enumerate(players, start=1):
        for idx2, player2 in enumerate(players, start=1):
            if idx1 < idx2:
                mylist.append((player1, player2))
    return mylist
