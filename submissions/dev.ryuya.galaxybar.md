* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-adaptive-statusbar

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-adaptive-statusbar/releases/tag/v0.6.19-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxybar`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Adapt status bar colors to the background

### Description:
Adjusts clock text and status icons to the background on supported Galaxy firmware, with configurable fades, app transition tracking and privacy indicator motion. Requires root and a libxposed API 102 compatible framework. Android 16 and 17 support is firmware specific.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.6.19-experimental** (`40`); experimental release.
- Immutable source commit: `23b48261ffe2f0822258da94d09a30e79ae11b56`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxybar.yml
- Developer certificate SHA-256: `aaecd6957a8e72d09462e04204b04b23c4f3bd3d9534fc62c4eb2ba29596265d`.
- APK SHA-256: `0968154871d3051925c7c52f42c72afc9cca760850f337ff6299b1c952c2e0ba`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
