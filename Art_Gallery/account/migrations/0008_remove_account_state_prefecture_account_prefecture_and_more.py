# Generated by Django 4.0.5 on 2022-08-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_account_city_account_country_account_postal_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='state_prefecture',
        ),
        migrations.AddField(
            model_name='account',
            name='prefecture',
            field=models.CharField(choices=[('Wakayama', '和歌山県'), ('Nara', '奈良県'), ('Oita', '大分県'), ('Kagawa', '香川県'), ('Hyogo', '兵庫県'), ('Kanagawa', '神奈川県'), ('Akita', '秋田県'), ('Shimane', '島根県'), ('Tokushima', '徳島県'), ('Shizuoka', '静岡県'), ('Gunma', '群馬県'), ('Mie', '三重県'), ('Chiba', '千葉県'), ('Osaka', '大阪府'), ('Niigata', '新潟県'), ('Kochi', '高知県'), ('Nagano', '長野県'), ('Tochigi', '栃木県'), ('Tokyo', '東京都'), ('Aichi', '愛知県'), ('Yamanashi', '山梨県'), ('Shiga', '滋賀県'), ('Yamagata', '山形県'), ('Hiroshima', '広島県'), ('Iwate', '岩手県'), ('Yamaguchi', '山口県'), ('Okayama', '岡山県'), ('Kyoto', '京都府'), ('Hokkaido', '北海道'), ('Aomori', '青森県'), ('Tottori', '鳥取県'), ('Miyazaki', '宮崎県'), ('Ehime', '愛媛県'), ('Okinawa\t', '沖縄県'), ('Fukui', '福井県'), ('Toyama', '富山県'), ('Kagoshima', '鹿児島県'), ('Gifu', '岐阜県'), ('Ibaraki', '茨城県'), ('Miyagi', '宮城県'), ('Fukushima', '福島県'), ('Saitama', '埼玉県'), ('Saga', '佐賀県'), ('Kumamoto', '熊本県'), ('Fukuoka', '福岡県'), ('Ishikawa', '石川県'), ('Nagasaki', '長崎県')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(choices=[('Alabama', 'Alabama')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]