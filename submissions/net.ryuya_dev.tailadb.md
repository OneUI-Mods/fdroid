* [ ] The app complies with all inclusion criteria (source/build and policy review requested; open points below).
* [x] The package is not in the official repository, and no open request for this package was found.
* [x] The upstream maintainer has requested and consents to inclusion.
* [ ] Donated (no donation claimed).

### Link to the source code:
https://github.com/OneUI-Mods/tail-adb

### Link to app in another app store:
https://github.com/OneUI-Mods/tail-adb/releases/tag/v0.2.4

Developer-signed F-Droid repository: https://oneui-mods.github.io/fdroid/repo

### Application ID:
`net.ryuya_dev.tailadb`

### License used:
MIT. Third-party runtime dependency license notices are included in the source and app.

### Category:
System

### Summary:
ADB access over your Tailscale network

### Description:
Provides an authorized ADB transport restricted to the device's Tailscale interface, with per-peer shell and root permissions and network recovery. Requires root and the separate Tailscale app. It uses the selected Tailscale account's network; no Tailscale code is bundled.

These are existing apps used on supported Galaxy devices, rather than placeholder demos. The upstream maintainer requests official inclusion of this independently identified app. Related OneUI Mods requests concern separate application IDs and functions.

### Packaging information and open review points:
- Latest requested version: **0.2.4** (`6`); stable release.
- Immutable source commit: `5464653b05152b890af334ab7ddb71d6666ac9b4`.
- Source-build draft (explicitly unvalidated): https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/net.ryuya_dev.tailadb.yml
- Developer certificate SHA-256: `429de1280138eb96207ea61c6c19a36d2a83404e4654ce52d14e1aba43abf980`.
- APK SHA-256: `7482d0878a58f870dcffff161142e954adb7652d58612a2d0aa42ebcd9521840`.
- Existing developer signatures should be retained if reproducible builds can be established. We are not claiming that the current APK has passed F-Droid reproducibility verification.
- Declared anti-features/dependencies for review: TetheredNet.

The published source uses Android SDK 37. The draft recipe has not been tested on the F-Droid build server, and cross-machine reproducibility has not yet been established. Native helper code is included as source and built with Android NDK 28.2.13676358. It uses the device's system adbd rather than bundling a proprietary daemon.

Each source repository has user-facing setup/compatibility information and separate development/release instructions. No proprietary host application is bundled in these modules. Please flag any further packaging or policy changes needed before acceptance.
