# Atelier – Chiffrement/Déchiffrement (Python `cryptography`) dans GitHub Codespaces

## 1) Lancer le projet dans Codespaces
- Fork / clone ce repo
- Bouton **Code** → **Create codespace on main**
- Attendre l'installation automatique (requirements.txt)

## 2) Installer (si besoin)
```bash
pip install -r requirements.txt
```
## 3) Partie A – Chiffrer/Déchiffrer un texte
```
python app/fernet_demo.py
```
Définis ensuite ta clé dans l'environnement :  
```
export FERNET_KEY="COLLE_LA_CLE_ICI"
python app/fernet_demo.py
```
## 4) Partie B – Chiffrer/Déchiffrer un fichier
Créer un fichier de test :  
```
echo "Top secret" > secret.txt
```
Chiffrer :
```
python app/file_crypto.py encrypt secret.txt secret.enc
```
Déchiffrer :
```
python app/file_crypto.py decrypt secret.enc secret.dec.txt
cat secret.dec.txt
```
## 5) Questions rapides
  
**Quel est le rôle de la clé dans Fernet ?**  
Déposez votre répose ici dans ce Readme
  
**Que se passe-t-il si on modifie un octet du fichier chiffré ?**  
Déposez votre répose ici dans ce Readme  
  
**Pourquoi ne faut-il pas commiter la clé dans Git ?**  
Déposez votre répose ici dans ce Readme  
  
**Différence entre clé générée aléatoirement et clé dérivée d'un mot de passe ?**  
Déposez votre répose ici dans ce Readme  

## 6) Bonus – Mot de passe + dérivation de clé (PBKDF2)  
```
python app/password_crypto.py
```
Rejoue l'exécution avec le même SALT_B64 et le même mot de passe.  

  
  










