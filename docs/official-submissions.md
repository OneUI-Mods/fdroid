# 公式F-Droidへの掲載申請

2026年10月25日、全14アプリを個別に申請しました。GitLab上の一覧でも14件の作成を確認済みです。現在は審査待ちで、公式リポジトリへの掲載完了を意味しません。

| アプリ | 掲載申請 | 状況 |
| --- | --- | --- |
| OneUI Mods Manager | [#4649](https://gitlab.com/fdroid/rfp/-/work_items/4649) | 審査待ち |
| Dark App Tools | [#4650](https://gitlab.com/fdroid/rfp/-/work_items/4650) | 審査待ち |
| One UI Home Tweaks | [#4651](https://gitlab.com/fdroid/rfp/-/work_items/4651) | 審査待ち |
| Galaxy Camera Tools | [#4652](https://gitlab.com/fdroid/rfp/-/work_items/4652) | 審査待ち |
| SIM Pilot | [#4653](https://gitlab.com/fdroid/rfp/-/work_items/4653) | 審査待ち |
| Tail ADB | [#4654](https://gitlab.com/fdroid/rfp/-/work_items/4654) | 審査待ち |
| Galaxy Update Guard | [#4655](https://gitlab.com/fdroid/rfp/-/work_items/4655) | 審査待ち |
| Galaxy Adaptive Bar | [#4656](https://gitlab.com/fdroid/rfp/-/work_items/4656) | 審査待ち |
| Galaxy Service Panel | [#4657](https://gitlab.com/fdroid/rfp/-/work_items/4657) | 審査待ち |
| Galaxy Reload | [#4658](https://gitlab.com/fdroid/rfp/-/work_items/4658) | 審査待ち |
| Galaxy Capture Tools | [#4659](https://gitlab.com/fdroid/rfp/-/work_items/4659) | 審査待ち |
| SleepStore | [#4660](https://gitlab.com/fdroid/rfp/-/work_items/4660) | 審査待ち |
| Galaxy Shutter Mute Manager | [#4661](https://gitlab.com/fdroid/rfp/-/work_items/4661) | 審査待ち |
| Galaxy Shutter Mute | [#4662](https://gitlab.com/fdroid/rfp/-/work_items/4662) | 審査待ち |

公式側のソースビルドと審査、既存署名を維持するための再現性確認は別途必要です。公開した[ビルド草案](../packaging/drafts/)は未検証であることを明記し、各タグのSDK・nativeビルド・APKダウンロードの同意などの確認点も申請本文へ記載しています。

[全申請の一覧](https://gitlab.com/fdroid/rfp/-/work_items?author_username=ryuya0124)・[送信本文](../submissions/)を確認できます。配布中の[専用リポジトリ](https://oneui-mods.github.io/fdroid/)ではGitHub版と同じ署名のrelease APKを使用します。

参考：[公式掲載条件](https://f-droid.org/docs/Inclusion_Policy/)、[掲載申請手順](https://f-droid.org/docs/Submitting_to_F-Droid_Quick_Start_Guide/)、[署名と再現可能ビルド](https://f-droid.org/docs/Reproducible_Builds/)。

既存配布タグのSDKも個別に照合しました。12本はcompileSdk 37、SleepStore 0.2.0は36、Galaxy Shutter Mute 1.1.0は35です。後者2本は申請本文も補正済みです。専用リポジトリは既存の署名済みAPKをそのまま配布し、タグやAPKを書き換えません。
