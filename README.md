# OneUI Mods · F-Droid

Samsung Galaxy向けOneUI Modsアプリを、F-Droidクライアントから導入・更新するための専用リポジトリです。各アプリのGitHub Releaseと同じ署名済みAPKを配布します。

## リポジトリを追加

F-Droidの「設定 → リポジトリ → 追加」で次のURLを入力してください。

```text
https://oneui-mods.github.io/fdroid/repo
```

リポジトリ証明書のSHA-256：

```text
A12CF1059CEDFBECBD883F5F653A9228EEFD0227EC5DA4BDFB805337A97AC8B2
```

[証明書付きで追加する](https://oneui-mods.github.io/fdroid/repo?fingerprint=A12CF1059CEDFBECBD883F5F653A9228EEFD0227EC5DA4BDFB805337A97AC8B2)

GitHub版とアプリの署名は同じなので、同じパッケージのAPKは上書き更新できます。署名が異なる他の配布元から導入済みの場合は、その配布元の案内に従ってください。

## 配布内容

OneUI Mods Managerの[公開カタログ](https://github.com/OneUI-Mods/OneUIModsManager/blob/main/catalog/apps.json)に登録されたアプリが対象です。安定版と実験版を掲載し、安定版があるアプリでは安定版を推奨版にします。実験版だけのアプリも含むため、導入前にバージョン名と変更内容を確認してください。

アプリごとに対応するAndroid・One UI・端末・root／Shizuku／Vectorの条件が異なります。アプリ詳細のソースリンクからREADMEを確認してください。Samsungなどの公式配布ではありません。

## 公式F-Droidとの違い

この専用リポジトリはOneUI Modsが管理し、GitHub ReleaseのAPKを検証して配布します。公式F-Droidのソースビルド・審査済みという意味ではありません。公式側への掲載申請と状況は[申請記録](docs/official-submissions.md)へ分けて記載します。

開発・署名・公開の方法は[開発者向け](docs/development.md)を参照してください。
