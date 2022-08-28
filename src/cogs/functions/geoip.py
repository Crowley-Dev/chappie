#!/usr/bin/env python3

import requests


class GeoIP:
  def __init__(self, ) -> None:
    pass

  async def request_api(self, url, ip):
    resp = requests.get(url.format(ip))

    if resp.status_code == 429:
      return {
        "msg": "Muitas consultas estão sendo realizadas.",
        "code": 503
      }

    address = resp.json()
    if address.get("status") == "fail":
      return {
        "msg": f"Impossível realizar a consulta. ({address.get('message')})",
        "code": 503
      }

    return {
      "content": [
        {
          "Continente": address.get("continent")
            + "/" + address.get("continentCode"),
          "País": address.get("country") \
            + "/" + address.get("countryCode"),
          "Região": address.get("regionName") \
            + "/" + address.get("region"),
          "Cidade": address.get("city"),
          "Código ZIP": address.get("zip")
        },
        {
          "Moeda nacional": address.get("currency"),
          "Fuso horário": address.get("timezone"),
          "Offset (Diferença horária com a hora UTC, em segundos)": address.get("offset"),
          "Latitude": address.get("lat"),
          "Longitude": address.get("lon")
        },
        {
          "Provedor": address.get("isp"),
          "ORG": address.get("org"),
          "AS": address.get("as"),
          "ASname": address.get("asname"),
          "DNS Reverso": address.get("reverse")
        },
        {
          "mobile (Conexão móvel/Celular)": address.get("mobile"),
          "proxy (Endereço de saída de proxy, VPN ou Tor)": address.get("proxy"),
          "hospedagem": address.get("hosting")
        }
      ]
    }
