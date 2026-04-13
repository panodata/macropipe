# Macropipe

[![Tests](https://github.com/panodata/macropipe/actions/workflows/tests.yml/badge.svg)](https://github.com/panodata/macropipe/actions/workflows/tests.yml)
[![Coverage](https://codecov.io/gh/panodata/macropipe/branch/main/graph/badge.svg)](https://app.codecov.io/gh/panodata/macropipe)
[![Build status (documentation)](https://readthedocs.org/projects/macropipe/badge/)](https://macropipe.readthedocs.io/)
[![License](https://img.shields.io/pypi/l/macropipe.svg)](https://pypi.org/project/macropipe/)

[![PyPI Version](https://img.shields.io/pypi/v/macropipe.svg)](https://pypi.org/project/macropipe/)
[![Python Version](https://img.shields.io/pypi/pyversions/macropipe.svg)](https://pypi.org/project/macropipe/)
[![PyPI Downloads](https://pepy.tech/badge/macropipe/month)](https://pepy.tech/project/macropipe/)
[![Status](https://img.shields.io/pypi/status/macropipe.svg)](https://pypi.org/project/macropipe/)

## About

Macropipe follows the structured pipeline approach of the Polars
[pipe operator]. It provides text-based macro languages that
compile to Polars expressions. See also [Macropipe Primer].

The library can be used for data decoding, encoding, conversion, translation,
transformation, and cleansing purposes, either as a pipeline element for data
pre- or post-processing, or as a standalone converter program.

## Installation

The package is available from [PyPI] at [macropipe].
To install the most recent version, invoke:
```shell
uv pip install --upgrade 'macropipe[all]'
```

## Usage

In order to learn how to use the library, please visit the [documentation],
and explore the source code or its [examples].

## Project Information

### Acknowledgements

Kudos to the authors of all the many software components this library is
vendoring and building upon.

### Contributing

The `macropipe` package is an open-source project, and is
[managed on GitHub]. The project is still in its infancy, and
we appreciate contributions of any kind.

### License

MIT. However, optional dependencies may pull in packages using different
licenses. See [LICENSE] and [NOTICE] files about more details.


[documentation]: https://macropipe.readthedocs.io/
[examples]: https://macropipe.readthedocs.io/example/
[LICENSE]: https://github.com/panodata/macropipe/blob/main/LICENSE
[macropipe]: https://pypi.org/project/macropipe/
[Macropipe Primer]: https://macropipe.readthedocs.io/primer.html
[managed on GitHub]: https://github.com/panodata/macropipe
[NOTICE]: https://github.com/panodata/macropipe/blob/main/NOTICE
[PyPI]: https://pypi.org/
[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
