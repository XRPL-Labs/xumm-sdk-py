# Xumm Sdk Release Process

## Cutting a Release

The full process for cutting a release is as follows:

0. Checkout a new branch:
   `git checkout -b v1.0.2` # 1.0.2-release

2. Change the version in the setup.py file:
   `VERSION = "1.0.2"`

3. Add, and commit the changes, push up the branch, and open a PR:
   `git add .`
   `git commit -m 'RELEASE v1.0.2'`
   `git push --set-upstream origin HEAD`

4. Open PR request

   ``

5. Once the PR is merged, checkout the `main` branch:
   `git checkout main`

6. Delete `main` branch (Optional):
   `git branch -d v1.0.2`

7. Make a new Git tag that matches the new version (make sure it is associated with the right commit SHA): FIXUP
   `git tag -a v1.0.2 -m "cut v1.0.2"`

8. Push up the tag from `main`:
   `git push origin v1.0.2`

## Packaging & Releasing

Update pip build (optional)

`python3 -m pip install --upgrade build`

Build Repo

`python3 -m build`

```
dist/
  xumm-sdk-py-1.0.2-py3-none-any.whl
  xumm-sdk-py-1.0.2.tar.gz
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
