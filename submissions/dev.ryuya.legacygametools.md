* [ ] Full F-Droid inclusion/build-policy review is requested; open points below.
* [x] No matching request was found by searching this project's work items for Legacy Game Tools.
* [x] The upstream maintainer requests and consents to inclusion.
* [ ] Donated (no donation claimed).

### Source and license
https://github.com/OneUI-Mods/legacy-game-tools
MIT. Dependency notices are included. No game binaries, Unity libraries or game content are bundled.

### Release
https://github.com/OneUI-Mods/legacy-game-tools/releases/tag/v0.1.0

### Application ID
dev.ryuya.legacygametools

### Category and summary
System — Startup compatibility for supported older game trials.

### Description
A scoped Xposed API 102 module that fixes a native Unity memory-tracking startup crash in specific arm64 editions of the D4DJ D4U and Sekai trials. Requires root and a compatible Xposed framework. Unknown engine revisions are left unchanged. Does not restore discontinued online services or distribute games.

Tested on Android 17 / Galaxy S26 Ultra through initial post-startup screens. Full gameplay and discontinued online services are outside the verified scope.

### Packaging and review points
- Experimental release 0.1.0, versionCode 1.
- Immutable source: 8ef303a0ff03d6da8024118539d259153a94f005.
- Source-build recipe draft: https://github.com/OneUI-Mods/fdroid/blob/main/packaging/drafts/dev.ryuya.legacygametools.yml
- compile/target SDK 37; JDK 21; NDK 30.0.16248370; CMake 3.22.1.
- Android release build, native host checks and lint pass on Linux CI. The draft has not been built with the F-Droid build server; reproducibility is not established.
- Dependency/anti-feature for review: NonFreeDep. Supported games are separate proprietary apps.
- Developer certificate SHA-256: f3a3227d5836f3906b033b82e894b493f82b779fda1d3972b30ebfd7e2cff3f0.
- Release APK SHA-256: da2b47366937ac72ca513c59babb0a424e52ca3d747c07537330504fb77415eb.
- Developer-signed repository: https://oneui-mods.github.io/fdroid/repo

Please review source-build and policy requirements before inclusion. Retain the developer signature only after successful reproducibility verification.
