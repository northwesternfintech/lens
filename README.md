# lens


NUFT's data fetching from internal servers solution


Only supporting Python 3.12 for now. Heavily in progress, more versions and whatnot soon.


## Usage
Lens provides a simple data fetching API. All queries require `startup` to be called on the instance before fetching.


```python
ln = Lens()
ln.startup()
df = ln.load_trades_for_day("avax", "2025-02-21")
```
