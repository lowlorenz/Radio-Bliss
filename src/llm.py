from pathlib import Path
import openai
from typing import Optional


class ChatGPT:
    def __init__(self, api_key: Optional[str] = None):
        if api_key is None:
            env_path = Path('.env')
            if env_path.exists():
                env = {line.split('=')[0]: line.split('=')[1] for line in env_path.read_text().split('\n') if line if '=' in line and not line.startswith('#')}
                api_key = env['OPENAI']
            else:
                raise ValueError('api_key must be provided or set in .env file')
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url='https://llms.azurewebsites.net'
        )
    
    def get_funfacts(self, background_info: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5",
            messages=[
                {
                    "role": "system",
                    "content": "You find good-to-know information about the area around you. Only use the provided information and discard anything that might be boring. Output one sentence containing fun-facts and interesting information about the most interesting nearby place. Limit the output to the most interesting place."
                },
                {
                    "role": "user",
                    "content": background_info,
                }
            ]
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    chatgpt = ChatGPT()
    print(chatgpt.get_funfacts("# Raum der Stille (place_of_worship)\n\n## OpenStreetMap:\n\n```\n{'addr:city': 'Berlin', 'addr:country': 'DE', 'addr:housenumber': '8', 'addr:postcode': '10117', 'addr:street': 'Pariser Platz', 'addr:suburb': 'Mitte', 'amenity': 'place_of_worship', 'contact:email': 'raum-der-stille@berlin.de', 'contact:website': 'http://www.raum-der-stille-im-brandenburger-tor.de/', 'description': 'Meditationsraum', 'name': 'Raum der Stille', 'name:ru': 'Комната тишины', 'opening_hours': 'Jan Mo-Su,PH 11:00-16:00; Feb Mo-Su,PH 11:00-17:00; Mar-Oct Mo-Su,PH 11:00-18:00; Nov Mo-Su,PH 11:00-17:00; Dec Mo-Su,PH 11:00-16:00', 'place_of_worship': 'room', 'religion': 'multifaith', 'start_date': '1994', 'wheelchair': 'no'}\n```\n\n# Commerzbank (bank)\n\n## OpenStreetMap:\n\n```\n{'amenity': 'bank', 'brand': 'Commerzbank', 'brand:wikidata': 'Q157617', 'brand:wikipedia': 'de:Commerzbank', 'name': 'Commerzbank', 'opening_hours': 'Sa 09:00-17:00', 'wheelchair': 'yes'}\n```\n\n# Brandenburger Tor (taxi)\n\n## OpenStreetMap:\n\n```\n{'amenity': 'taxi', 'name': 'Brandenburger Tor'}\n```\n\n# mama trattoria (restaurant)\n\n## OpenStreetMap:\n\n```\n{'amenity': 'restaurant', 'cuisine': 'italian', 'name': 'mama trattoria', 'opening_hours': 'We-Sa 12:00-22:00; Su-Tu 12:00-21:30', 'website': 'https://mama.eu/'}\n```\n\n## Website: mama trattoria Pizza Pasta Salate\n\nAktuell gibt es zehn mama Restaurants, davon sieben in Hamburg, zwei in Berlin und eins in Köln. Wir freuen uns auf Ihren Besuch. Sie können auch zum Take-away bestellen oder bei vielen Standorten liefern lassen. Die Küchen bleiben jeweils bis eine Stunde vor Restaurantschließung geöffnet.\n\nDie Öffnungszeiten, Kontaktdaten, Reservierungs-, Take-away- und Liefer-Möglichkeiten finden Sie auf den jeweiligen Standortseiten.\n\n# Axica Convention Center (conference_centre)\n\n## OpenStreetMap:\n\n```\n{'addr:city': 'Berlin', 'addr:country': 'DE', 'addr:housenumber': '3', 'addr:postcode': '10117', 'addr:street': 'Pariser Platz', 'addr:suburb': 'Mitte', 'amenity': 'conference_centre', 'architect': 'Frank Gehri', 'building': 'yes', 'building:use': 'office;residential', 'name': 'Axica Convention Center', 'start_date': '2001', 'wikidata': 'Q116419145', 'wikipedia': 'de:DZ-Bank-Gebäude am Pariser Platz'}\n```\n\n## Wikipedia: DZ-Bank-Gebäude am Pariser Platz ()\n\nDas Gebäude der DZ Bank am Pariser Platz Nr.\xa03 im Berliner Ortsteil Mitte ist ein Büro-, Konferenz- und Wohngebäude, das zwischen 1996 und 2001 nach einem Entwurf von Frank Gehry errichtet wurde. Gehry bezeichnete es als “The best thing I’ve ever done”.\n\n"))
