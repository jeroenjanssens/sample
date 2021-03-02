# sample-stream

<div align="center">

[![Build status](https://github.com/jeroenjanssens/sample-stream/workflows/build/badge.svg?branch=master&event=push)](https://github.com/jeroenjanssens/sample-stream/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/sample-stream.svg)](https://pypi.org/project/sample-stream/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jeroenjanssens/sample-stream/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/jeroenjanssens/sample-stream/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/jeroenjanssens/sample-stream/releases)
[![License](https://img.shields.io/github/license/jeroenjanssens/sample-stream)](https://github.com/jeroenjanssens/sample-stream/blob/master/LICENSE)

</div>

`sample` is a Python package that allows you to filter lines from standard input according to some probability, with a given delay, and for a certain duration.


## Installation

You can install `sample-stream` as follows:

```console
$ python -m pip install sample-stream
```

This will install an executable `sample` in `~/.local/bin`. You probably want to either add this directory to your `PATH` or create an alias to this executable in a directory which already is on your `PATH`.


## Example

The following command samples lines with a probability of 0.01, with a delay of 1000 milliseconds in between lines, for 5 seconds.

```console
$ time seq -f "Line %g" 1000000 | sample -r 1% -d 1000 -s 5
Line 71
Line 250
Line 305
Line 333
Line 405
Line 427
seq -f "Line %g" 1000000  0.01s user 0.00s system 0% cpu 5.092 total
sample -r 1% -d 1000 -s 5  0.06s user 0.02s system 1% cpu 5.091 total
```


## Help

```console
$ sample --help
usage: sample [-h] [-W WEEKS] [-D DAYS] [-H HOURS] [-m MINUTES] [-s SECONDS]
              [-t MILLISECONDS] [-u MICROSECONDS] [-r RATE] [-d DELAY]
              [FILE]

Output lines from stdin to stdout with a given probability for a given duration, and with
a given delay between lines.

positional arguments:
  FILE                  File

optional arguments:
  -h, --help            show this help message and exit
  -W WEEKS, --weeks WEEKS
                        Duration of sampling in weeks
  -D DAYS, --days DAYS  Duration of sampling in days
  -H HOURS, --hours HOURS
                        Duration of sampling in hours
  -m MINUTES, --minutes MINUTES
                        Duration of sampling in minutes
  -s SECONDS, --seconds SECONDS
                        Duration of sampling in seconds
  -t MILLISECONDS, --milliseconds MILLISECONDS
                        Duration of sampling in milliseconds
  -u MICROSECONDS, --microseconds MICROSECONDS
                        Duration of sampling in microseconds
  -r RATE, --rate RATE  Rate between 0 and 1 using either 0.33, 33%, 1/3 notation.
  -d DELAY, --delay DELAY
                        Time in milliseconds between each line of output
```


## License

[![License](https://img.shields.io/github/license/jeroenjanssens/sample-stream)](https://github.com/jeroenjanssens/sample-stream/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/jeroenjanssens/sample-stream/blob/master/LICENSE) for more details.


## Citation

```
@software{sample-stream,
  author = {Jeroen H.M. Janssens},
  title = {{sample-stream} -- Sample lines from a stream},
  year = {2021},
  url = {https://github.com/jeroenjanssens/sample-stream},
  version = {0.2.0}
}
```


## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
