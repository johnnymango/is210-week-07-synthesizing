#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module checks for password."""

import authentication
import getpass


def login(username, maxattempts=3):
    """This function checks for valid passoword for a given username.

    Args:
        username (string): The username.
        maxattempts (int, optional): The number of attempts allowed.
        The default is 3 attempts.

    Returns:
        Bool: True if the password matches. False if the password does not.

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> import task_02
        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True
        """
    authorization = False
    attempts = 1
    password = "Please enter your password."
    msgfailure = "Incorrect password.  You have {} attempts remaining."
    while not authorization and attempts <= maxattempts:
        authorization = authentication.authenticate(username,
                                                    getpass.getpass(password))
        if authorization is True:
            authorization = True
        else:
            print msgfailure.format(maxattempts - attempts)
            attempts += 1
    return authorization
