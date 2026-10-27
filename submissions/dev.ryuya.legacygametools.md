* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [ ] Duplicate-request check to be completed before submission.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/legacy-game-tools

### Link to app in another app store:
https://github.com/OneUI-Mods/legacy-game-tools/releases/tag/v0.1.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.legacygametools`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Startup compatibility for supported older game trials

### Description:
Fixes a native Unity startup crash in the supported arm64 editions of the D4DJ D4U and Sekai trials. Requires root and an API 102 compatible Xposed framework. Does not bundle games or restore discontinued online services. See the source README for the exact supported versions.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.1.0** (`1`); experimental release.
- Immutable source commit: `8ef303a0ff03d6da8024118539d259153a94f005`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.legacygametools.yml
- Developer certificate SHA-256: `f3a3227d5836f3906b033b82e894b493f82b779fda1d3972b30ebfd7e2cff3f0`.
- APK SHA-256: `da2b47366937ac72ca513c59babb0a424e52ca3d747c07537330504fb77415eb`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The requested release tag uses compileSdk 37; newer source branches must be reviewed separately. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
