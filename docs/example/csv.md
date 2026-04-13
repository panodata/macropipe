(csv)=

# CSV example

Imagine a CSV file finds you that needs pre-processing before you can import
the dataset into a database.

:::{rubric} Input (`example.csv`)
:::

Your database does not understand the `coordinates` format,
and the `data` values are not using standard JSON format.

```text
timestamp,coordinates,data
1754784000000,"[9.757, 47.389]","{'temperature': 42.42, 'humidity': 84.84}"
```

:::{rubric} Evaluation
:::

In this case, you need to perform two transformation steps.

- Convert coordinates in JSON list format to WKT POINT format.
  ```text
  Input:  [9.757, 47.389]
  Output: POINT( 9.757 47.389 )
  ```
- Convert the data dictionary encoded in proprietary Python format into standard JSON format.
  ```text
  Input:  {'temperature': 42.42, 'humidity': 84.84}
  Output: {"temperature": 42.42, "humidity": 84.84}
  ```

:::{rubric} Implementation
:::

The program below implements those requirements, using two built-in Macropipe
recipe functions {func}`json_array_to_wkt_point <macropipe.lib.Functions.json_array_to_wkt_point>`
and {func}`python_to_json <macropipe.lib.Functions.python_to_json>` that
convert CSV cell values into the required formats.
You can also find the routine in the [Macropipe example program].

```python
import polars as pl
from macropipe import MacroPipe

# Define a transformation pipeline using two recipe functions.
pipeline = MacroPipe.from_recipes(
    "json_array_to_wkt_point:coordinates",
    "python_to_json:data",
)

# Read CSV data.
lf = pl.scan_csv("example.csv")

# Apply transformation pipeline and compute the result.
df = lf.mp.apply(pipeline).collect()
```

:::{rubric} Output
:::

```python
>>> print(df)
```
```text
shape: (1, 3)
┌───────────────┬──────────────────────┬─────────────────────────────────┐
│ timestamp     ┆ coordinates          ┆ data                            │
│ ---           ┆ ---                  ┆ ---                             │
│ i64           ┆ str                  ┆ str                             │
╞═══════════════╪══════════════════════╪═════════════════════════════════╡
│ 1754784000000 ┆ POINT (9.757 47.389) ┆ {"temperature":42.42,"humidity… │
└───────────────┴──────────────────────┴─────────────────────────────────┘
```
```python
>>> print(df.write_csv(include_header=True, quote_style="non_numeric"))
```
```text
"timestamp","coordinates","data"
1754784000000,"POINT (9.757 47.389)","{""temperature"":42.42,""humidity"":84.84}"
```


[Macropipe example program]: https://github.com/panodata/macropipe/blob/main/examples/basic.py
