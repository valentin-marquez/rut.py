# Rut.py

Rut.py is a Python library for handling Chilean RUTs (Rol Único Tributario). It provides functions to clean, validate, get the check digit, format, and generate RUTs.

This library is based on the JavaScript library [rut.js](https://github.com/jlobos/rut.js) by jlobos. It aims to bring similar functionality to Python developers working with Chilean RUTs.

## Installation

You can install Rut.py using pip:

```shell
pip install rutpy
```

## Usage

To use RutPy, first import the necessary functions:

```python
from rutpy import clean, validate, get_check_digit, format, generate
```

You can then use the functions according to your needs.

### Clean

The `clean` function is used to remove dots and hyphens from a RUT:

```python
rut = "14.961.581-4"
clean_rut = clean(rut)
print(clean_rut)  # Output: 149615814
```

### Validate

The `validate` function is used to check whether a RUT is valid or not:

```python
rut = "14.961.581-4"
is_valid = validate(rut)
print(is_valid)  # Output: True
```

### Get Check Digit

The `get_check_digit` function is used to retrieve the check digit of a RUT:

```python
rut = "14.961.581"
check_digit = get_check_digit(rut)
print(check_digit)  # Output: 4
```

### Format

The `format` function is used to format a RUT with dots and hyphen:

```python
rut = "14961581"
formatted_rut = format(rut)
print(formatted_rut)  # Output: 14.961.581
```

### Generate

The `generate` function is used to generate a valid RUT:

```python
rut = generate()
print(rut)  # Output: A randomly generated valid RUT
```

## Contributions

Contributions are welcome. If you find any issues, have any improvement ideas, or want to add new features, you can open an issue or submit a pull request on the [GitHub repository](https://github.com/NozzOne/rut.py).

## License

Rut.py is distributed under the [MIT License](https://opensource.org/licenses/MIT).
