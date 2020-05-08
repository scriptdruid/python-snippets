# To set up pandas dev-env:

## Clone the repo

```bash
git clone https://github.com/vipulrai91/pandas.git
cd pandas
git remote add upstream https://github.com/pandas-dev/pandas.git
```

## Create the env from .yml file

```bash
conda env create -f environment.yml
conda activate pandas-dev
```

## Install Cython if required

```bash
pip install cython
```

## Build pandas

```bash
/Users/vipul/opt/anaconda3/envs/pandas-dev/bin/python /Users/vipul/Work/Github/pandas/setup.py build_ext --inplace -j 4
```

## Install Pandas

```bash
/Users/vipul/opt/anaconda3/envs/pandas-dev/bin/python -m pip install -e . --no-build-isolation --no-use-pep517
```

## To update changes from original repo

```bash
git pull upstream master
```
