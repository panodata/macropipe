(parquet)=

# Parquet example

:::{rubric} Usage
:::

Imagine a Parquet file where you only want to proceed with a subset of the data,
by filtering records by cell values, and by selecting only specific columns.

The program below implements those requirements, using the built-in Macropipe
recipe functions {func}`filter <macropipe.lib.Functions.filter>`
and {func}`select <macropipe.lib.Functions.select>`.
You can also find the routine in the [Macropipe example program].

```python
import polars as pl
from macropipe import MacroPipe

# Define a transformation pipeline using two recipe functions.
pipeline = MacroPipe.from_recipes(
    "filter:total_amount > 40",
    "select:passenger_count,trip_distance,fare_amount,tip_amount,total_amount",
)

# Read Parquet data.
lf = pl.scan_parquet("https://cdn.crate.io/downloads/datasets/cratedb-datasets/timeseries/yc.2019.07-tiny.parquet")

# Apply transformation pipeline and compute the result.
df = lf.mp.apply(pipeline).collect()
```

:::{rubric} Output
:::

```python
>>> print(df)
```
```text
Output: shape: (4, 5)
┌─────────────────┬───────────────┬─────────────┬────────────┬──────────────┐
│ passenger_count ┆ trip_distance ┆ fare_amount ┆ tip_amount ┆ total_amount │
│ ---             ┆ ---           ┆ ---         ┆ ---        ┆ ---          │
│ i64             ┆ f64           ┆ f64         ┆ f64        ┆ f64          │
╞═════════════════╪═══════════════╪═════════════╪════════════╪══════════════╡
│ 1               ┆ 18.8          ┆ 52.0        ┆ 11.75      ┆ 70.67        │
│ 1               ┆ 18.46         ┆ 52.0        ┆ 11.06      ┆ 66.36        │
│ 1               ┆ 7.0           ┆ 24.5        ┆ 6.85       ┆ 41.27        │
│ 1               ┆ 10.3          ┆ 31.5        ┆ 8.8        ┆ 44.1         │
└─────────────────┴───────────────┴─────────────┴────────────┴──────────────┘
```
```python
>>> print(df.write_csv(include_header=True, quote_style="non_numeric"))
```
```text
"passenger_count","trip_distance","fare_amount","tip_amount","total_amount"
1,18.8,52.0,11.75,70.67
1,18.46,52.0,11.06,66.36
1,7.0,24.5,6.85,41.27
1,10.3,31.5,8.8,44.1
```


[Macropipe example program]: https://github.com/panodata/macropipe/blob/main/examples/basic.py
