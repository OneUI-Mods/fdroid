* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-shutter-mute-manager

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-shutter-mute-manager/releases/tag/1.2.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`net.ryuya.dev.galaxyshutter.mute.manager`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Set up Galaxy Shutter Mute through Shizuku

### Description:
Installs and grants the settings permission needed by Galaxy Shutter Mute through Shizuku. The companion app is downloaded only after the user's explicit action. Galaxy Shutter Mute remains a separate app. Support depends on Samsung firmware, region and camera version.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **1.2.0** (`3`); stable release.
- Immutable source commit: `842ec2a8cb6b60c5cab7de0a973ce794f23feb72`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/net.ryuya.dev.galaxyshutter.mute.manager.yml
- Developer certificate SHA-256: `5fcf43c524c48708405bd61f78300a91a4e10ca0ceebfe130c650c7d679f2da5`.
- APK SHA-256: `0a8d65f49db9b2600bf3f9c771d1d8421beb73f759eb77199b7a08740cef41c9`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep, TetheredNet.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established. The app offers explicit user-initiated APK downloads from GitHub. Please review the downloader consent flow against the executable-download policy before inclusion; a dedicated consent clarification or build flavor may be needed.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
