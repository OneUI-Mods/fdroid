# OneUI Mods F-Droid distribution

- Only mirror signed release APKs from public OneUI-Mods GitHub Releases.
- Verify package, version, SHA-256 and catalog-pinned signing certificate before publication. Never re-sign an APK.
- Repository index signing credentials stay outside Git and the published site. Back up the repository key and password privately to Windows `B:\Androidアプリ 署名鍵\OneUI Mods F-Droid Repository`.
- Publish only `site/` to the `gh-pages` branch. Never publish private state, config, logs or signing keys.
- Keep user-facing distribution instructions separate from development and official-submission records. Do not claim official F-Droid inclusion before acceptance.
- Use at most four concurrent app checks/downloads and preserve valid local state on failure.
