import geoip2.database

# MaxMindのGeoLite2のデータベースファイルへのパスを指定
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# IPアドレスを格納しているファイルを開く
with open('ips.txt') as file:
    ip_addresses = file.readlines()

# 結果を格納するリスト
results = []

# 各IPアドレスに対して国情報を取得
for ip in ip_addresses:
    try:
        response = reader.country(ip.strip())
        country = response.country.name
        results.append(f'{ip.strip()}: {country}')
    except geoip2.errors.AddressNotFoundError:
        results.append(f'{ip.strip()}: Country not found')

# 結果を表示
for result in results:
    print(result)

# データベースを閉じる
reader.close()
