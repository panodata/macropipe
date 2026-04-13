(macropipe-primer)=

# Macropipe Primer

:::{div} sd-text-muted
Macropipe transformations use text-only macro languages that compile to Polars expressions.
:::

## Introduction

The Polars engine is currently one of the fastest data processing solutions
on a single machine.

[Polars] has developed its own Domain Specific Language (DSL) for transforming
data. The language is easy to use and allows for complex queries that
remain human-readable, based on expressions and contexts.

In Polars, an _expression_ is a lazy representation of a data transformation.
[Expressions][expr-concept] are modular and flexible, which means you can
use them as building blocks to build more complex expressions.

Polars features a [lazy API] and [streaming] operations: Your query is only
evaluated once results intend to be acquired, and processing the data in
batches allows working with datasets that do not fit in memory.
Deferring the execution like this can have significant performance advantages.

Using the Polars DSL, you can compose expressions in a fluent way, this is what
you are normally doing when writing Python programs or notebooks. However, you
can also use a structured way, by applying a sequence of user-defined functions
(UDFs) using the [pipe operator].

(macropipe)=

## Macropipe

Macropipe follows the structured pipeline approach provided by the Polars
[pipe operator]. [^littering]

In contrast to the Python-based API, Macropipe invents a simple text-based
macro language that compiles to Polars LazyFrame transformations:
Function name and positional arguments are separated by colons `:`,
that's it. Use `\:` to represent a literal colon inside an argument. [^macro-next]
```text
<function>:<arg1>:<arg2>:<arg3>
```

Macropipe ships with a few {mod}`built-in recipe functions <macropipe.lib>`
and allows you to register transformation functions yourself, based on Polars'
powerful [`Expr`] [primitive][expr-concept] and [ecosystem][expr-types].

> In Polars, an _expression_ is a lazy representation of a data transformation.

For Python consumption, the `macropipe` package exports the `MacroPipe` and
`recipe` symbols. For Polars consumption, Macropipe's utility methods are
registered on Polars' `mp` LazyFrame namespace.

[^littering]: To support Polars in creating optimal query plans, the current
              implementation will need to get rid of a bit of [pipe littering] that
              crept in. Any support is much appreciated.

[^macro-next]: Currently, the macro language is pretty ~~poor~~ flat.
               It can certainly be improved in future iterations.
               Any suggestions are very much welcome.
               Q: What about [CQL] ([spec][cql-spec]) or related languages?

## Synopsis

Read from data source, apply transformation, and write to data sink.

```python
import polars as pl
from macropipe import MacroPipe

# Define transformation pipeline.
pipeline = MacroPipe.from_recipes("head:30")

# Invoke pipeline and inspect result.
lf = pl.scan_csv("example.csv")
df = lf.mp.apply(pipeline).collect()
print(df)
```

## Examples

Macropipe demonstrations using hands-on example use cases.

::::{grid}

:::{grid-item-card} CSV example
:link: csv
:link-type: ref
Pre-process a CSV file. 
:::

:::{grid-item-card} Parquet example
:link: parquet
:link-type: ref
Filter a Parquet file.
:::

::::

## Documentation

:::{rubric} Details
:::

Please inspect the {mod}`built-in recipe functions <macropipe.lib>` to learn which
macros you can use out of the box. You can add custom transformation functions by
registering them using the `@macropipe.recipe` Python decorator. Feel free to
submit your favourite ones to the repository, we are always happy to receive
contributions.

Macropipe provides a slim yet powerful text-based macro interface by standing
on the shoulders of giants. Required package sizes can weigh in significantly,
in this spirit it is trading memory for speed.

- https://pypi.org/project/polars/ (45 MB)
- https://pypi.org/project/polars-st/ (50 MB)
- https://pypi.org/project/pyarrow/ (50 MB)
- https://pypi.org/project/pyogrio/ (30 MB)

(prior-art)=

:::{rubric} Related
:::

Prior art projects listed in alphabetical order.

- [data_algebra] is a piped data wrangling system based on Codd's relational algebra.
- [`functools.pipe` - Function Composition Utility] is proposing a new functools module.
- [LLM DSL for Polars] explores how to use LLMs to generate Polars DSL code.
- [PEP 638 – Syntactic Macros] introduces syntactic macros to Python. A macro is a
  compile-time function that transforms a part of the program to allow functionality
  that cannot be expressed cleanly in normal library code.
- [Streamz] helps you build pipelines to manage continuous streams of data. It is
  simple to use in simple cases, but also supports complex pipelines that involve
  branching, joining, flow control, feedback, back pressure, and so on.
- [Tikray] is a data model and implementation for a compact transformation engine
  based on JMESPath, jq, JSON Pointer (RFC 6901), rsonpath, transon, and DWIM.
- [Turtle Island] is a utility library that provides helper functions to reduce
  boilerplate when writing Polars expressions.



[CQL]: https://en.wikipedia.org/wiki/Contextual_Query_Language
[cql-spec]: https://www.loc.gov/standards/sru/cql/spec.html
[data_algebra]: https://github.com/WinVector/data_algebra
[`Expr`]: https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/enum.Expr.html
[expr-concept]: https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/
[expr-types]: https://docs.pola.rs/user-guide/expressions/
[`functools.pipe` - Function Composition Utility]: https://discuss.python.org/t/functools-pipe-function-composition-utility/69744
[lazy API]: https://docs.pola.rs/user-guide/concepts/lazy-api/
[LLM DSL for Polars]: https://www.linkedin.com/pulse/dsls-llms-ken-kocienda-fpi1c
[PEP 638 – Syntactic Macros]: https://peps.python.org/pep-0638/
[pipe littering]: https://docs.pola.rs/user-guide/migration/pandas/#pipe-littering
[pipe operator]: https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.pipe.html
[Polars]: https://pola.rs/
[Streamz]: https://streamz.readthedocs.io/
[streaming]: https://docs.pola.rs/user-guide/concepts/streaming/
[Tikray]: https://tikray.readthedocs.io/
[Turtle Island]: https://jrycw.github.io/turtle-island/
