import requests
import pyodbc
import json
def get_people_facebook(parameters):
    datapath = open("datapath.txt", "r").readlines()

    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + datapath[2] + ';')
    cursor = connection.cursor()

    # Construct the WHERE clause dynamically based on the provided parameters
    where_clauses = []
    for key, value in parameters.items():
        if value is not None:
            if isinstance(value, str):
                where_clauses.append(f"{key}='{value}'")
            else:
                where_clauses.append(f"{key}={value}")

    where_clause = " AND ".join(where_clauses)

    return where_clause

url = "https://www.10bis.co.il/NextApi/GetUserAuthenticationDataAndSendAuthenticationCodeToUser"

headers = {
    "authority": "www.10bis.co.il",
    "accept": "application/json, text/plain, */*",
    "accept-language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "WebApplication.Locale=Language=he; WebApplication.Context=ShoppingCartGuid=b55de41c-6489-41b0-aff0-f2d0415c83e3; nextContext=ShoppingCartGuidTimestamp=1688673834841; _hjFirstSeen=1; _hjIncludedInSessionSample_1089785=0; _hjSession_1089785=eyJpZCI6IjRmNjhhMmE4LTkxNDctNDFhNy04MDJjLWQ4YTcyYmVhMzUzYSIsImNyZWF0ZWQiOjE2ODg2NzM4MzU3ODQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjHasCachedUserAttributes=true; _scid=2a3317dc-eabe-4b80-a430-94f29103d558; _gcl_au=1.1.1537911115.1688673837; _ga=GA1.3.162850223.1688673837; _gid=GA1.3.1689577164.1688673837; _gat_gtag_UA_110399884_15=1; intercom-id-nzqx6uu6=f8c3b30f-d4fd-4963-8004-df000dec8626; intercom-session-nzqx6uu6=; intercom-device-id-nzqx6uu6=8cc5862f-91e0-4fb7-98b7-3a4f9b9ef627; _scid_r=2a3317dc-eabe-4b80-a430-94f29103d558; _hjSessionUser_1089785=eyJpZCI6ImZjYzNmNzgyLTZmZGEtNWRhMi1iYWQ1LTgzYTNmYTQ5OWYwNCIsImNyZWF0ZWQiOjE2ODg2NzM4MzU3NzQsImV4aXN0aW5nIjp0cnVlfQ==; _uetsid=3ccb18501c3811ee88c9270d35d3fd7f; _uetvid=3ccb66201c3811eea539b37add5ee229; utag_main=v_id:01892ccdcfa100123d110f8c0ea20506f001d06701328^$_sn:1^$_se:7^$_ss:0^$_st:1688675685556^$ses_id:1688673832866^%^3Bexp-session^$_pn:2^%^3Bexp-session",
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5NTQ3MzUiLCJhcCI6IjIwNDM1NTc3OCIsImlkIjoiYWE4ZGMzZjNiOWZmODA1OCIsInRyIjoiOGE2YWZmODFlNjA2OGI2ZDI4NGYxZjYxNDc4YTlmNjAiLCJ0aSI6MTY4ODY3Mzg5MDI1Nn19",
    "origin": "https://www.10bis.co.il",
    "pragma": "no-cache",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-8a6aff81e6068b6d284f1f61478a9f60-aa8dc3f3b9ff8058-01",
    "tracestate": "2954735^@nr=0-1-2954735-204355778-aa8dc3f3b9ff8058----1688673890256",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "x-app-type": "mobileWeb"
}

data = {
    "culture": "he-IL",
    "uiCulture": "he",
    "email": f"{input('enter email')}"
}

response = requests.post(url, headers=headers, json=data)
xx=response.json()

if xx['Errors'] == []:
    last_four_phone_digits = xx['Data']['codeAuthenticationData']['lastFourPhoneDigits']
    prefix = "9725"
    datapath = open("datapath.txt", "r").readlines()

    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + datapath[2] + ';')
    cursor = connection.cursor()
    # Execute the SQL query
    parameters = {
        "phone": None,
        "id": None,
        "name": input("enter name\n"),
        "family_name": input("enter family name\n"),
        "gender": input("enter gender\n"),
        "cureentyplace": None,
        "fromplace": None,
        "statuse": None,
        "year": None,
        "email": None,
        "dateborn": None,
    }
    parameters = {key: value for key, value in parameters.items() if value}
    query = f"SELECT * FROM facebook WHERE LEFT(phone, 4) = '{prefix}' AND RIGHT(phone, 4) = '{last_four_phone_digits}' AND {get_people_facebook(parameters)}"
    cursor.execute(query)
    results = cursor.fetchall()

    fields = ["phone", "id", "name", "family_name", "gender", "cureentyplace", "fromplace", "statuse", "year", "email", "dateborn"]
    processed_results = [{field: value for field, value in zip(fields, row)} for row in results]

    # Print the results
    for result in processed_results:
        print(result)



else:
    print(xx['Errors'][0]['ErrorDesc'])
