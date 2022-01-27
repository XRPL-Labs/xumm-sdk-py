# Xumm Sdk Release Process

## Cutting a Release

The full process for cutting a release is as follows:

0. Checkout a new branch:
   `git checkout -b 0.9.9-beta.5` # 1.0.0-release

1. Python / Pip Bumpversion

   `pip3 install bumpversion`

   `bumpversion --current-version 0.9.9-beta.5 minor setup.py xumm/__init__.py`

2. Change the version in the setup.py file:
  `VERSION = "0.9.9-beta.5"`

3. Add, and commit the changes, push up the branch, and open a PR:
   `git add .`
   `git commit -m 'RELEASE 0.9.9-beta.5'`
   `git push --set-upstream origin HEAD`

4. Open PR request

   ``

4. Once the PR is merged, checkout the `main` branch:
   `git checkout main`

5. Delete `main` branch (Optional):
   `git branch -d 0.9.9-beta.5`

5. Make a new Git tag that matches the new version (make sure it is associated with the right commit SHA): FIXUP
   `git tag -a 0.9.9-beta.5 -m "cut 0.9.9-beta.5"`

7. Push up the tag from `main`:
   `git push origin 0.9.9-beta.5`


## Packaging & Releasing

Update pip build (optional)

`python3 -m pip install --upgrade build`

Build Repo

`python3 -m build`

```
dist/
  xumm-sdk-py-dangell-0.9.9-beta.5-py3-none-any.whl
  xumm-sdk-py-dangell-0.9.9-beta.5.tar.gz
```

Install Twine

`python3 -m pip install --upgrade twine`

Config .pypirc

```
[pypi]
  username = __token__
  password = pypi-TokenString
```

Check Distribution

`twine check dist/*`


Push on Staging

`twine upload --skip-existing --config-file="./.pypirc" -r testpypi dist/*`

Push to Production

`twine upload --config-file="./.pypirc" -r dist/*`