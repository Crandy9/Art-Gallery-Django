# Generated by Django 4.0.5 on 2022-08-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_account_phone_number_alter_account_prefecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='prefecture',
            field=models.CharField(blank=True, choices=[('Ishikawa', '石川県'), ('Yamagata', '山形県'), ('Fukui', '福井県'), ('Fukushima', '福島県'), ('Hiroshima', '広島県'), ('Tochigi', '栃木県'), ('Aomori', '青森県'), ('Shiga', '滋賀県'), ('Chiba', '千葉県'), ('Wakayama', '和歌山県'), ('Oita', '大分県'), ('Akita', '秋田県'), ('Shizuoka', '静岡県'), ('Toyama', '富山県'), ('Nagano', '長野県'), ('Ibaraki', '茨城県'), ('Shimane', '島根県'), ('Kagoshima', '鹿児島県'), ('Tokushima', '徳島県'), ('Ehime', '愛媛県'), ('Kanagawa', '神奈川県'), ('Miyagi', '宮城県'), ('Nara', '奈良県'), ('Tottori', '鳥取県'), ('Kumamoto', '熊本県'), ('Gunma', '群馬県'), ('Miyazaki', '宮崎県'), ('Osaka', '大阪府'), ('Kochi', '高知県'), ('Yamanashi', '山梨県'), ('Gifu', '岐阜県'), ('Aichi', '愛知県'), ('Iwate', '岩手県'), ('Okinawa\t', '沖縄県'), ('Saga', '佐賀県'), ('Niigata', '新潟県'), ('Mie', '三重県'), ('Kagawa', '香川県'), ('Yamaguchi', '山口県'), ('Okayama', '岡山県'), ('Kyoto', '京都府'), ('Nagasaki', '長崎県'), ('Tokyo', '東京都'), ('Hyogo', '兵庫県'), ('Hokkaido', '北海道'), ('Saitama', '埼玉県'), ('Fukuoka', '福岡県')], max_length=50),
        ),
    ]
