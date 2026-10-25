* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-shutter-mute

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-shutter-mute/releases/tag/1.1.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`net.ryuya.dev.galaxyshutter.mute`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Control the supported Galaxy shutter sound setting

### Description:
Changes the supported Galaxy camera shutter sound setting after its required permission has been granted. Use Galaxy Shutter Mute Manager for installation on recent Android versions. Samsung firmware and regional restrictions may limit availability.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **1.1.0** (`2`); stable release.
- Immutable source commit: `2e2a2744d3afbcd15dc055f21ec7d7c6cb286f17`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/net.ryuya.dev.galaxyshutter.mute.yml
- Developer certificate SHA-256: `5fcf43c524c48708405bd61f78300a91a4e10ca0ceebfe130c650c7d679f2da5`.
- APK SHA-256: `8a0920fc4a586d1c0420a60dbeda2d8efadc7cc32957246eb43cfcc5c1d74946`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established. Its deliberately old Android compatibility settings are required for the Samsung setting it changes. Installation on recent Android releases is normally performed through its separate Shizuku manager.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
