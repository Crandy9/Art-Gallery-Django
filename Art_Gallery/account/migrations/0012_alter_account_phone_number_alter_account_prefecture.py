# Generated by Django 4.0.5 on 2022-08-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_account_phone_number_alter_account_prefecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='prefecture',
            field=models.CharField(blank=True, choices=[('Kagoshima', '鹿児島県'), ('Gunma', '群馬県'), ('Ishikawa', '石川県'), ('Toyama', '富山県'), ('Gifu', '岐阜県'), ('Hokkaido', '北海道'), ('Kyoto', '京都府'), ('Ehime', '愛媛県'), ('Miyazaki', '宮崎県'), ('Kanagawa', '神奈川県'), ('Saga', '佐賀県'), ('Kagawa', '香川県'), ('Tochigi', '栃木県'), ('Okinawa\t', '沖縄県'), ('Mie', '三重県'), ('Aichi', '愛知県'), ('Fukui', '福井県'), ('Tokushima', '徳島県'), ('Kochi', '高知県'), ('Fukuoka', '福岡県'), ('Kumamoto', '熊本県'), ('Shizuoka', '静岡県'), ('Akita', '秋田県'), ('Miyagi', '宮城県'), ('Okayama', '岡山県'), ('Fukushima', '福島県'), ('Wakayama', '和歌山県'), ('Tokyo', '東京都'), ('Hiroshima', '広島県'), ('Shimane', '島根県'), ('Nagano', '長野県'), ('Nagasaki', '長崎県'), ('Yamaguchi', '山口県'), ('Ibaraki', '茨城県'), ('Yamagata', '山形県'), ('Aomori', '青森県'), ('Hyogo', '兵庫県'), ('Chiba', '千葉県'), ('Nara', '奈良県'), ('Iwate', '岩手県'), ('Saitama', '埼玉県'), ('Oita', '大分県'), ('Yamanashi', '山梨県'), ('Shiga', '滋賀県'), ('Tottori', '鳥取県'), ('Niigata', '新潟県'), ('Osaka', '大阪府')], max_length=50),
        ),
    ]
