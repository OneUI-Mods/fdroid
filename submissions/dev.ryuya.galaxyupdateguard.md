* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/galaxy-update-guard

### Link to app in another app store:
https://github.com/OneUI-Mods/galaxy-update-guard/releases/tag/v0.1.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.galaxyupdateguard`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Pause and restore Galaxy OS updates

### Description:
Disables supported Samsung OS update services and restores their previous state. Requires root. Google Play system and application updates are outside its scope. Restore the original state before uninstalling or clearing this app's data.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.1.0** (`1`); stable release.
- Immutable source commit: `ef195a70ec357bfd66d9a91a128117cbee58cded`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.galaxyupdateguard.yml
- Developer certificate SHA-256: `88f94ec7b259ffd2ee1b9eb72e291400fe740c14c7f2609220907e8f50b34262`.
- APK SHA-256: `892cc69a18eacfd4ee1fe36fb404345854b9e2b52383f61377db2e8fb79349ed`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
