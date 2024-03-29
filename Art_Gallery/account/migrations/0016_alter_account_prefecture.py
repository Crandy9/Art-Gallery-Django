# Generated by Django 4.0.5 on 2022-08-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_account_city_alter_account_prefecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='prefecture',
            field=models.CharField(blank=True, choices=[('Niigata', '新潟県'), ('Saitama', '埼玉県'), ('Akita', '秋田県'), ('Hiroshima', '広島県'), ('Fukui', '福井県'), ('Toyama', '富山県'), ('Oita', '大分県'), ('Aichi', '愛知県'), ('Shizuoka', '静岡県'), ('Yamaguchi', '山口県'), ('Hyogo', '兵庫県'), ('Tokyo', '東京都'), ('Fukuoka', '福岡県'), ('Kumamoto', '熊本県'), ('Hokkaido', '北海道'), ('Mie', '三重県'), ('Miyazaki', '宮崎県'), ('Iwate', '岩手県'), ('Ehime', '愛媛県'), ('Saga', '佐賀県'), ('Yamanashi', '山梨県'), ('Tottori', '鳥取県'), ('Okayama', '岡山県'), ('Nagasaki', '長崎県'), ('Kagawa', '香川県'), ('Gunma', '群馬県'), ('Kanagawa', '神奈川県'), ('Ishikawa', '石川県'), ('Nagano', '長野県'), ('Shimane', '島根県'), ('Tokushima', '徳島県'), ('Aomori', '青森県'), ('Nara', '奈良県'), ('Shiga', '滋賀県'), ('Gifu', '岐阜県'), ('Yamagata', '山形県'), ('Ibaraki', '茨城県'), ('Kyoto', '京都府'), ('Osaka', '大阪府'), ('Wakayama', '和歌山県'), ('Okinawa\t', '沖縄県'), ('Kagoshima', '鹿児島県'), ('Tochigi', '栃木県'), ('Kochi', '高知県'), ('Fukushima', '福島県'), ('Chiba', '千葉県'), ('Miyagi', '宮城県')], max_length=50),
        ),
    ]
