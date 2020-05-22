# To set up pandas dev-env:

## Clone the repo

```console
git clone https://github.com/vipulrai91/pandas.git
cd pandas
git remote add upstream https://github.com/pandas-dev/pandas.git
```

## Create the env from .yml file

```console
conda env create -f environment.yml
conda activate pandas-dev
```

## Install Cython if required

```console
pip install cython
```

## Build pandas

```console
/Users/vipul/opt/anaconda3/envs/pandas-dev/bin/python /Users/vipul/Work/Github/pandas/setup.py build_ext --inplace -j 4
```

## Install Pandas

```console
/Users/vipul/opt/anaconda3/envs/pandas-dev/bin/python -m pip install -e . --no-build-isolation --no-use-pep517
```

## To update changes from original repo

```console
git pull upstream master
```
