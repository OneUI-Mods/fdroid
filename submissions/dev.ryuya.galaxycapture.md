* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/GalaxyCaptureTools

### Link to app in another app store:
https://github.com/OneUI-Mods/GalaxyCaptureTools/releases/tag/v0.3.5-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxycapture`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Extend Galaxy recording and screenshots

### Description:
Adds optional recording rotation, app targeting, audio and capture controls to supported Samsung and Android recording components. Requires root and a libxposed API 102 compatible framework. Read the source README for supported firmware and initial activation steps.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.3.5-experimental** (`19`); experimental release.
- Immutable source commit: `88262467a21a9478e0b81287f60a4c2ba0f3b9a6`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxycapture.yml
- Developer certificate SHA-256: `3c18719ba633ed0e891d8dca62053c849986156fd10410bd5f0115113ffa6075`.
- APK SHA-256: `dd4a9c98dea6ac8bfbbbe009410215636d82eb529db1784e4025418766840eb4`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
