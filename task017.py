import re

s = 'ООО, ИП, НИИ МАНАНАЗЭМ, ООН, ИТИС КФУ, ФизРа'

print(re.findall(r'\b[А-ЯЁ ]+\b', s))