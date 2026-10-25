* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/SleepStore

### Link to app in another app store:
https://github.com/OneUI-Mods/SleepStore/releases/tag/v0.2.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.sleepstore`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Show updates for deep-sleeping apps

### Description:
Helps supported app-store components include deep-sleeping apps in their update listings. Requires root, a compatible Xposed framework and supported store versions. It does not bundle the store apps.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.2.0** (`2`); stable release.
- Immutable source commit: `00f540270b9731f7f47bf88e5d69ab07b6188cf4`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.sleepstore.yml
- Developer certificate SHA-256: `9d1f5a2cea5340c434682221e355cbfc92f8a97cdf6994f782ff6d96660a90b6`.
- APK SHA-256: `b27168e4212be0c9ee03105cd6496e3b5b032a3fbd4a55340232d1780bfee8f2`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
