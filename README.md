## Reproduce

Tested with `pip==21.3.1`, all local installs (i.e. clone this repo and run these commands within the folder)

```
git clone git@github.com:alkasm/test-vcs-offline.git
cd test-vcs-offline
python3 -m venv venv
source venv/bin/activate
pip install pip==21.3.1
```

### Installation online works as expected

```
pip install .
```

### Installation offline complains that the VCS dep cannot be pulled

Disable network access (e.g. turn off wifi)
```
pip install .
```

### Installation offline with --no-deps doesn't check that version constraints are satisfied

Note that `setup.py` requires `six==1.15.0`, so this install should fail with 1.16.0 installed.

With internet access:
```
pip install six==1.16.0
```

Disable network access (e.g. turn off wifi)

```
pip install --no-deps .
```

Notice that no error occurs during the installation.

### Installation offline with the old resolver does not eagerly install the VCS dep, and does version check

With internet access:
```
pip install six==1.16.0
```

Disable network access (e.g. turn off wifi)

```
pip install --use-deprecated legacy-resolver .
```

Note that pip errors during the installation, since the version of `six` does not match the expected version.