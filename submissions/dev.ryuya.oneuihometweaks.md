* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/OneUIHomeTweaks

### Link to app in another app store:
https://github.com/OneUI-Mods/OneUIHomeTweaks/releases/tag/v0.18.0

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`dev.ryuya.oneuihometweaks`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
Customize One UI Home and the quick panel

### Description:
Adjust supported One UI Home folder behavior, quick panel controls and developer animation settings. Requires root, a libxposed API 102 compatible framework and supported Samsung system components. Keep the source README at hand for supported firmware and reload instructions.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.18.0** (`28`); experimental release.
- Immutable source commit: `d5b1c35c98938ee43ee837b6f53ac926e9bb5e8d`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.oneuihometweaks.yml
- Developer certificate SHA-256: `7938e1850451b95c45c8f138a768c9da7c5d9db7fb61a883ac8dc724077ddb03`.
- APK SHA-256: `91e1e616bb5586c9432042351a74931988df1c055a676829b6517d746667a8fc`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: NonFreeDep.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
