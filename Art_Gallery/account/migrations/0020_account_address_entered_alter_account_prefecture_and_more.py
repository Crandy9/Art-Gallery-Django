# Generated by Django 4.0.5 on 2022-08-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_account_prefecture_alter_account_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address_entered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='prefecture',
            field=models.CharField(blank=True, choices=[('Kyoto', '京都府'), ('Kagawa', '香川県'), ('Kochi', '高知県'), ('Tottori', '鳥取県'), ('Okayama', '岡山県'), ('Chiba', '千葉県'), ('Saitama', '埼玉県'), ('Yamaguchi', '山口県'), ('Okinawa\t', '沖縄県'), ('Yamagata', '山形県'), ('Saga', '佐賀県'), ('Ibaraki', '茨城県'), ('Niigata', '新潟県'), ('Fukushima', '福島県'), ('Wakayama', '和歌山県'), ('Shimane', '島根県'), ('Kumamoto', '熊本県'), ('Aomori', '青森県'), ('Miyazaki', '宮崎県'), ('Osaka', '大阪府'), ('Iwate', '岩手県'), ('Gifu', '岐阜県'), ('Fukuoka', '福岡県'), ('Tokyo', '東京都'), ('Aichi', '愛知県'), ('Fukui', '福井県'), ('Miyagi', '宮城県'), ('Ishikawa', '石川県'), ('Kanagawa', '神奈川県'), ('Kagoshima', '鹿児島県'), ('Nara', '奈良県'), ('Oita', '大分県'), ('Gunma', '群馬県'), ('Akita', '秋田県'), ('Toyama', '富山県'), ('Tochigi', '栃木県'), ('Hiroshima', '広島県'), ('Shiga', '滋賀県'), ('Hokkaido', '北海道'), ('Shizuoka', '静岡県'), ('Hyogo', '兵庫県'), ('Yamanashi', '山梨県'), ('Nagasaki', '長崎県'), ('Ehime', '愛媛県'), ('Tokushima', '徳島県'), ('Nagano', '長野県'), ('Mie', '三重県')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='state',
            field=models.CharField(blank=True, choices=[('Armed Forces', 'Armed Forces - AA'), ('Armed Forces Europe', 'Armed Forces Europe - AE'), ('Armed Forces Pacific', 'Armed Forces Pacific - AP'), ('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('District of Columbia', 'District of Columbia'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virgin Islands', 'Virgin Islands'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming'), ('Guam', 'Guam'), ('Puerto Rico', 'Puerto Rico')], max_length=50, null=True),
        ),
    ]
