* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-reload

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-reload/releases/tag/v0.2.0-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxyreload`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Reload SystemUI on supported Galaxy devices

### Description:
User-initiated SystemUI reload helper for supported Galaxy devices. Requires root. Its unlock-state handling is only available when the device is already authenticated; it does not disable screen-lock credentials.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.2.0-experimental** (`2`); experimental release.
- Immutable source commit: `82c87115ecc7b4e62192d1ea2cf82d93ab02fd6a`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxyreload.yml
- Developer certificate SHA-256: `52a22de1aed8b3c3d34c02f8fe0f0206eaee25081def64d8182ca5930cbf85fb`.
- APK SHA-256: `309dc665c0d77e44ef9640c47879d59a06ea811a73e1717fa0fbb15da41bd63b`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
