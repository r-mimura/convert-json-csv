# Abstract
Convert `.json` to `.csv` or `.csv` to `.json` .

# Requirement

```
pip install pandas
```

# Usage

## Convret json to csv

```bash
main.py --input input.json --output output.csv
```

## Convret csv to json

```bash
main.py --input input.csv --output output.json
```

## Example

```json
[
    {
        "fruit": "Apple",
        "size": "Large",
        "color": "Red"
    },
    {
        "fruit": "Banana",
        "size": "Midium",
        "color": "Yellow"
    }
]
```
convert to csv

```csv
,fruit,size,color
0,Apple,Large,Red
1,Banana,Midium,Yellow

```
