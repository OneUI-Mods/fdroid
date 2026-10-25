* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/DarkAppTools

### Link to app in another app store:
https://github.com/OneUI-Mods/DarkAppTools/releases/tag/v0.3.0-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.darkapps`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Dark themes for supported apps

### Description:
Adds system, light and dark appearance options to supported versions of SESAME and povo. Requires root and a libxposed API 102 compatible framework such as Vector. The supported host apps are proprietary; they are not bundled.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.3.0-experimental** (`10`); experimental release.
- Immutable source commit: `dc4d04663546f3b437f138ba363456686d461086`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.darkapps.yml
- Developer certificate SHA-256: `c2020a1338f2504d893b368edfb77b0ab76cedeb8016df42876439a1cc92acd6`.
- APK SHA-256: `25fcba527d0198e5a687e954bbeae4cac9f7cb2dd4e78dc2c0796c887c99975d`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
