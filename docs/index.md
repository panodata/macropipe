(index)=

# Macropipe

```{toctree}
:maxdepth: 1
:caption: Handbook
:hidden:

install
Primer <primer>
example/index
```

```{toctree}
:maxdepth: 1
:caption: Development
:hidden:

Changelog <changes>
Backlog <backlog>
```

Macropipe follows the structured pipeline approach of the Polars
[pipe operator]. It provides text-based macro languages that
compile to Polars expressions. See also {ref}`macropipe-primer`.

## Install

```shell
uv pip install --upgrade 'macropipe[all]'
```

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

## Usage

Please explore the {ref}`examples` documentation section, items in the
["examples" directory], and the [software tests], in order to learn
about details or get inspirations that might not have been reflected
in the documentation yet.

## Prior Art

See {ref}`prior-art` projects that existed before Macropipe.



["examples" directory]: https://github.com/panodata/macropipe/tree/main/examples
[pipe operator]: https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.pipe.html
[Polars]: https://pola.rs/
[software tests]: https://github.com/panodata/macropipe/tree/main/tests
