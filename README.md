# lens

NUFT's data fetching from internal servers solution


## Usage
Lens provides a simple data fetching API. All queries require `startup` to be called on the instance before fetching.

Startup validates the selected project root (or default: `/pool/lens`).
Specific information on the contents of a data directory can be viewed in that directory's `metadata.json`.
A complete example of the file layout is available in either `file_structure.md` (tree) or `test/testing_data`.

```python
ln = Lens()
ln.startup()
df = ln.load_trades_for_day("avax", "2025-02-21")
df = ln.load_depth_for_day("avax", "2025-02-21")
```

These are the only two queries currently available, and both return `pd.DataFrame`. Headers are included.

`main.py` is included as a quick way to run the startup checks without needing to integrate with another codebase.

