# Welcome to the Team 6 Repo!
# 
# Project Overview:  Anonymous, Encrypted Survey Tool
# Encryption used: Advanced Encryption Standard 256-bit (AES256)
# 
# What it does: User takes any survey, cannot be traced back to the user.
# Survey is also encrypted, to prevent tampering. 
# The survey is stored in a PostgreSQL database, using built in encryption in order to prevent useer answers maliciously revealed, except
# by permission of a system administrator. 
#
# Codebase used: Python, Django, PostgreSQL
#
# Why?
# People often take surveys or answer questions in a very approving manner, especially when they know their boss or the public is watching
# their every move.  This can be a disadvantage because of the lack of honest answers a company / survey maker can receive.
# This survey project aims at solving the problem by providing complete and total anonymity to the users.  This way, when a question
# is presented, an honest, often blunt answer can be garnered.  This also protects the user from repercussions, the best of both worlds.
#
#
#
#
#
#
#
#
#
# To install, you will need the following:
# Make sure you install Python 3.6 stable release.  https://www.python.org/
# Django:  For Windows, open up a command prompt (or powershell) and type in
# pip install django-admin
# For more instructions, or if you're using a different operating system, follow the instructions at
# https://docs.djangoproject.com/en/2.0/topics/install/
# PostgreSQL database. https://www.postgresql.org/
# For our development project side, we used PyCharm from Jetbrains.  https://www.jetbrains.com/pycharm/
#
# Note that Python has its own IDE for development, and there are other options, should you wish.
#
# Using our Github Repo, pull the most recent release.
# With PyCharm, Edit Configurations:
# If your settings are blank, ensure to select your installed Python as the interpreter.  
# NOTE:  PyCharm has its own interpreter, but this is not recommended, as it will generate over 9000 files in a software emulation package.
# Add server >> (Green Plus Icon) Add Django Server
# Select Python 3.6 Interpreter
# Select the base of the project (where you saved it to) as your working directory.
# Select OK.
#
#
#
#
#
#
#
#
#
#Quick PostgreSQL Server Installation Guide for Mac
      #1. Download pgAdmin4 application to your Desktop from https://www.pgadmin.org/download/pgadmin-4-macos/
      #2. Create an account
      #3. Scroll over Servers, right click it, and hit 'create'. This will allow you to create a new server 
      $4. From there you can create your own database, monitor and edit all of its configurations
