import pandas as pd

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# 📁 Charger le fichier CSV avec les adresses e-mails
df = pd.read_csv("emails.csv")

# 🛠️ Remplacer les anciens domaines par les nouveaux
old_domain = "oldcompany.com"
new_domain = "newcompany.com"

df["new_email"] = df["email"].apply(lambda x: replace_domain(x, old_domain, new_domain))

# 💾 Sauvegarder dans un nouveau fichier CSV
df.to_csv("updated_emails.csv", index=False)

print("✅ Mise à jour terminée ! Les nouveaux e-mails sont dans 'updated_emails.csv'.")