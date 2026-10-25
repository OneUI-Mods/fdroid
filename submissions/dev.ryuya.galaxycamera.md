* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/GalaxyCameraTools

### Link to app in another app store:
https://github.com/OneUI-Mods/GalaxyCameraTools/releases/tag/v0.1.3-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxycamera`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Extend supported Samsung camera apps

### Description:
Optional camera preview, lens transition and camera capability adjustments for supported Samsung Camera, Camera Assistant and Expert RAW versions. Requires root and a libxposed API 102 compatible framework. Hardware and firmware limits still apply; unsupported modes are not guaranteed.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.1.3-experimental** (`4`); experimental release.
- Immutable source commit: `ca7001045ec30bd609d9343e01f6c6f92e3a8f47`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxycamera.yml
- Developer certificate SHA-256: `c46e5158643284a8eb345958b4bf72d09c30c2a5a3819c05b5f7b53c31d263ad`.
- APK SHA-256: `91780b4936cd2f4332b0478007fed21a28b2e04316330675e8177a64978895b0`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
