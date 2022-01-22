# Xumm Sdk Release Process

## Cutting a Release

The full process for cutting a release is as follows:

1. Checkout a new branch:
   `git checkout -b v0.9.9-beta.2` # v1.0.0-release

2. Change the version in the setup.py file:
  `VERSION = "v0.9.9-beta.2"`

3. Commit the changes, push up the branch, and open a PR:
   `git commit -m 'RELEASE v0.9.9-beta.2'`
   `git push --set-upstream origin HEAD`

4. Open PR request

   ``

4. Once the PR is merged, checkout the `master` branch:
   `git checkout master`

5. Make a new Git tag that matches the new version (make sure it is associated with the right commit SHA): FIXUP
   `git tag -a v0.9.9-beta.2 -m "cut v0.9.9-beta.2"`

7. Push up the tag from `master`:
   `git push origin v0.9.9-beta.2`