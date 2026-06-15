import requests


def get_inr_rate(currency_code):
    try:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{currency_code}", timeout=5
        )
        response.raise_for_status()
        data = response.json()

        print(response.status_code)
        return data["rates"]["INR"]
    except requests.exceptions.Timeout as e:
        print("timed out", e)
    except requests.exceptions.HTTPError as e:
        print("HTTP error", e)
    except requests.exceptions.RequestException as e:
        print("Request error", e)
    except KeyError:
        print("key not found")
