import aiohttp
import asyncio
from datetime import date, timedelta

class NBPAPI:
    base_url = "http://api.nbp.pl/api/exchangerates/rates/c/"
    currencies = ["EUR", "USD"]
    def __init__(self):
        pass
    async def fetch_exchange_rate(self, start_date):
        async with aiohttp.ClientSession() as session:
            rates = {}
            for currency in self.currencies:
                response = await session.get(f"{self.base_url}{currency}/last/10/?format=json")
                if response.ok == False:
                    raise ValueError(f"Failed to fetch data for {currency} - status code: {response.status}")

                data = await response.json()
                for entry in data['rates']:
                    if entry['effectiveDate'] not in rates:
                        rates[entry['effectiveDate']] = {}

                    rates[entry['effectiveDate']][currency.upper()] = {
                        'sale': entry['ask'],
                        'purchase': entry['bid']
                    }
            return rates

    async def get_exchange_rates(self):
        start_dates = [date.today() - timedelta(days=i) for i in range(10)]
        tasks = [self.fetch_exchange_rate(start_date) for start_date in start_dates]
        results = await asyncio.gather(*tasks)

        cleaned_results = self.remove_duplicates(results)
        return cleaned_results

    def remove_duplicates(self, results):
        cleaned_results = {}
        for result in results:
            for date_key, values in result.items():
                if date_key not in cleaned_results:
                    cleaned_results[date_key] = values
                else:
                    cleaned_results[date_key].update(values)
        return cleaned_results


async def main():
    api = NBPAPI()
    exchange_rates = await api.get_exchange_rates()
    print(f'Today is: {date.today()}\n\nThe exchange rates of EUR and USD for the last 10 days:')
    for date_key, values in exchange_rates.items():
        print(f"\n{date_key}:")
        for currency, rates in values.items():
            print(f"  {currency}:")
            for rate_type, rate_value in rates.items():
                print(f"    {rate_type}: {rate_value}")



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
