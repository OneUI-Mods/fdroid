* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/OneUIModsManager

### Link to app in another app store:
https://github.com/OneUI-Mods/OneUIModsManager/releases/tag/v0.2.0-experimental

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.oneuimods`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Manage and update apps from OneUI Mods

### Description:
Browse OneUI Mods apps, compare installed versions with public GitHub releases, choose whether to include experimental releases, and download verified updates. Installation always uses the Android confirmation screen. GitHub downloads are user initiated and bypass the official F-Droid build review.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.2.0-experimental** (`4`); experimental release.
- Immutable source commit: `d9391918d680daa375bfc464c36e9a8dd094e13c`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.oneuimods.yml
- Developer certificate SHA-256: `f37313a1ddbe006257653b4772e9a2f43f0ddd5c0bcbf6dfe0f71c2fbd9aad73`.
- APK SHA-256: `93d25c3588466b58d2d1aefa46d1d8f939b285c597566ff5d851504e643119fd`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: TetheredNet.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established. The app offers explicit user-initiated APK downloads from GitHub. Please review the downloader consent flow against the executable-download policy before inclusion; a dedicated consent clarification or build flavor may be needed.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
