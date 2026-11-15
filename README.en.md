# OneUI Mods · F-Droid

[日本語](README.md) · English

A dedicated repository for installing and updating OneUI Mods apps for Samsung Galaxy through an F-Droid client. It distributes the same signed APKs as each app's GitHub Releases.

## Add the repository

In F-Droid, open **Settings → Repositories → Add** and enter:

```text
https://oneui-mods.github.io/fdroid/repo
```

Repository signing certificate SHA-256:

```text
A12CF1059CEDFBECBD883F5F653A9228EEFD0227EC5DA4BDFB805337A97AC8B2
```

[Add with the certificate fingerprint](https://oneui-mods.github.io/fdroid/repo?fingerprint=A12CF1059CEDFBECBD883F5F653A9228EEFD0227EC5DA4BDFB805337A97AC8B2)

The APK signing identity is the same as the GitHub version, so matching packages can be updated in place. If your installed copy was signed by another distributor, follow that distributor's instructions.

## Included apps

The repository covers apps registered in OneUI Mods Manager's [public catalog](https://github.com/OneUI-Mods/OneUIModsManager/blob/main/catalog/apps.json). Both stable releases and prereleases are included; a stable release is recommended when available. Some apps have only prereleases, so check the version name and release notes before installing.

Supported Android and One UI versions, device models, and root / Shizuku / Vector requirements vary by app. Follow the source link on an app's details page to read its README. These are not official Samsung releases.

## How this differs from official F-Droid

OneUI Mods maintains this repository and verifies APKs from GitHub Releases before distributing them. Inclusion here does not mean that an app has been reviewed or built from source by official F-Droid. Official submission records and their status are kept separately in the [submission notes (Japanese)](docs/official-submissions.md).

See the [developer guide](docs/development.md) for development, signing, and publication procedures.
