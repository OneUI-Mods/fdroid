* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-service-panel

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-service-panel/releases/tag/v0.1.0-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxyservicepanel`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Improve the Samsung Service Mode layout

### Description:
Reformats supported Samsung Service Mode screens for readability while retaining the original diagnostic data. Requires root and a libxposed API 102 compatible framework. This unofficial module does not bundle or replace the proprietary Samsung phone app.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.1.0-experimental** (`1`); experimental release.
- Immutable source commit: `1442cc8ba72b2f9f0b00452d4647c8170ddc7764`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxyservicepanel.yml
- Developer certificate SHA-256: `4cda6775c402ba4cbc2591ffb3490b825d53a0aa7fafd98d67e85b337e8df0b0`.
- APK SHA-256: `d76e4de1ee61df338ac80080cdf533877af10360b937a1fdcd520044c7a73044`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
