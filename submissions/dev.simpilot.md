* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/sim-pilot

### Link to app in another app store:
https://github.com/OneUI-Mods/sim-pilot/releases/tag/v1.10.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.simpilot`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Manage dual-SIM data switching

### Description:
Manage supported dual-SIM data switching through Shizuku or Shizuku Plus. Requires compatible device telephony services and explicit Shizuku permission. No root is needed when Shizuku is available through wireless debugging.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **1.10.0** (`19`); stable release.
- Immutable source commit: `e72de55c7c6a90f3b1538dc72aaab5edbe4dead6`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.simpilot.yml
- Developer certificate SHA-256: `18014a67e709e973c8723ec4a6cd5ed079cb1fd29436f2c0fbd657f46e3c010b`.
- APK SHA-256: `16b2059bbc0d8e501901b8cbc1d3ac535d7ba7ab5d55d05e9aabcda6f13c23bd`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: none declared.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
