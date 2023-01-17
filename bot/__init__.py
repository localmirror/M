#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("19580505"))

API_HASH = os.environ.get("c4af6531e01a1f69e1f3e080e640f102")

BOT_TOKEN = os.environ.get("5929036016:AAHwXfs7gXwVTgoLlyzRabfS_EwG59Cjkcs")

DB_URI = os.environ.get("mongodb+srv://localmirror:Soumya2004@cluster0.uciy90e.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQANsyASVS3pKDG9-rhzf5MU3DVyTuIPBk3mH6ud6i2VC1m9REBQ0YB22vhJTuYwYTnCpcfwOlHHSBaoxy7hXBEYDWVnMbtG-PGsctGRRqSItnm_hIOm7B9MO973kC0u3yICJwztiMrgCTdt2Skwf2VojunqPpkZiXdu0Zl_q6W4JY1R8wQqgp7-06ZOIDMYh0dTnxfXYoOZajTD6aFKg-sjEBzp0sqT1LBr1xPvgHbwrtaPDVr3VZNlU-swFZ-3-YPaSh5Hu_KKs5C2sOpdF3vobFfk7h4-ngWROj4OJFh9wuNY8nagI_poHt_Ci6KpwDtdlcst4KsD6OJmaANIuJlIAAAAAV-fz5QA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
