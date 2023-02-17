# A Python package to generate a Gaia mock catalog

UNDER CONSTRUCTION

Build on previous work
* [jan-rybizki/Galaxia_wrap](https://github.com/jan-rybizki/Galaxia_wrap)
* [GeDR3mock](https://arxiv.org/abs/2004.09991)

## Virtual Environment instead

python has now a built-in virtual environment that can be used similarly to `conda`.

```shell
python -m venv --prompt gdr4mock --symlink venv
source venv/bin/activate
pip install --upgrade pip
pip install .
# and extras as
pip install ".[ci]"
```

## Notes

Steps:

1. Generates a Galaxia mock output.
    Requires: Galaxia
