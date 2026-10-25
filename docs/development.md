# Repository maintenance

The manager's public `catalog/apps.json` is the app registry. Release versions, assets and changelogs come directly from each app's GitHub Releases. `catalog-notes.json` provides optional English descriptions and declared dependencies; new catalog entries do not require an APK or manager update.

## Dependencies

Use Python 3, fdroidserver 2.4.5, CairoSVG 2.9.1, JDK 21, Android Build Tools 37.0.0 and authenticated `gh`. Keep Python dependencies in a private virtual environment. `tools/verify_apk.py` is shared MIT-licensed code from OneUIModsManager.

## Private state and signing

Run `fdroid init` in a private directory outside this repository. Set `repo_url` to `https://oneui-mods.github.io/fdroid/repo`. Keep `config.yml`, repository signing keystore and passwords private. They must never be copied to Git or the published website. Repository signing credentials are backed up by repository name in the user's private Windows signing-key backup location, together with passwords and recovery notes.

The repository signing key signs indexes only. Application APKs retain their original certificates. Additions must match the manager catalog's package and certificate pins; `AllowedAPKSigningKeys` enforces the same pins during indexing.

```sh
python tools/sync_releases.py --work /private/path/fdroid --tools /path/to/sdk/build-tools/37.0.0
python tools/render_icons.py --work /private/path/fdroid
cd /private/path/fdroid
fdroid update --pretty
```

The sync command checks at most four apps concurrently, verifies package, build version, release status, GitHub SHA-256 and APK signature, then writes a public provenance manifest. A single failed app stops publication; never deploy partially checked state. Existing APKs with the same package/version but different contents are rejected.

## Publishing

Run `tools/prepare_site.py --work /private/path/fdroid --output site`. It validates the signed indexes and every indexed APK against the verified provenance manifest and copies only public repository contents. Never copy the whole private work directory.

Publish `site/` to this repository's `gh-pages` branch. GitHub Pages serves that branch at its root. Keep the repository key off GitHub and CI; there is no unattended signing workflow. Run the explicit update/publish procedure after new releases. Actions artifacts are not used for distribution.

## Official F-Droid

The custom repository mirrors developer-signed release APKs. Official inclusion requires separate source build review. Do not replace application certificates to simulate official compatibility. Developer signatures require reproducible builds accepted by F-Droid. Submission records and open packaging questions belong in `official-submissions.md`.

The icon export renders original launcher vectors from each verified APK, using the selected Android SDK for framework colors. Apps without declared launcher artwork retain the client default. It never modifies the APK.
