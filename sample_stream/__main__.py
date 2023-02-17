# type: ignore[attr-defined]
import argparse
import os
from datetime import datetime, timedelta
from random import random
from sys import stdin, stdout
from time import sleep, time


def total_seconds(delta):
    return delta.seconds + (24 * 3600 * delta.days)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Filter lines from standard input according to some probability, "
            "with a given delay, and for a certain duration."
        )
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=stdin,
        help="File",
        metavar="FILE",
    )
    parser.add_argument(
        "-W",
        "--weeks",
        type=float,
        default=0,
        help="Duration of sampling in weeks",
    )
    parser.add_argument(
        "-D",
        "--days",
        type=float,
        default=0,
        help="Duration of sampling in days",
    )
    parser.add_argument(
        "-H",
        "--hours",
        type=float,
        default=0,
        help="Duration of sampling in hours",
    )
    parser.add_argument(
        "-m",
        "--minutes",
        type=float,
        default=0,
        help="Duration of sampling in minutes",
    )
    parser.add_argument(
        "-s",
        "--seconds",
        type=float,
        default=0,
        help="Duration of sampling in seconds",
    )
    parser.add_argument(
        "-t",
        "--milliseconds",
        type=float,
        default=0,
        help="Duration of sampling in milliseconds",
    )
    parser.add_argument(
        "-u",
        "--microseconds",
        type=float,
        default=0,
        help="Duration of sampling in microseconds",
    )
    parser.add_argument(
        "-r",
        "--rate",
        default="100%",
        help="Rate between 0 and 1 using either 0.33, 33%%, 1/3 notation.",
    )
    parser.add_argument(
        "-d",
        "--delay",
        default=0,
        type=int,
        help="Time in milliseconds between each line of output",
    )
    args = parser.parse_args()

    invalid_rate_msg = (
        "Invalid rate. Please specify a rate between 0"
        " and 1 using either 0.33, 33%, 1/3 notation."
    )

    try:
        delay = float(args.delay) / 1000.0
    except ValueError:
        parser.error("Invalid delay. Please specify a delay in ms.")

    try:
        duration = total_seconds(
            timedelta(
                weeks=args.weeks,
                days=args.days,
                hours=args.hours,
                minutes=args.minutes,
                seconds=args.seconds,
                milliseconds=args.milliseconds,
                microseconds=args.microseconds,
            )
        )
    except:
        parser.error("Invalid duration.")

    try:
        if "%" in args.rate:
            rate = float(args.rate[:-1]) / 100.0
        elif "/" in args.rate:
            a, b = map(float, args.rate.split("/")[:2])
            rate = a / (1.0 * b)
        else:
            rate = float(args.rate)
    except ValueError:
        parser.error(invalid_rate_msg)

    if rate <= 0 or rate > 1:
        parser.error(invalid_rate_msg)

    start = time()
    try:
        while True:
            line = args.file.readline()
            if not line:
                return
            if random() <= rate:
                stdout.write(line)
                stdout.flush()
                now = time()
                if duration and (now - start) > duration:
                    return
                sleep(delay)
    except:
        pass


if __name__ == "__main__":
    exit(main())
