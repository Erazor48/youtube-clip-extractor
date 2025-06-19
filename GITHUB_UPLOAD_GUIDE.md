# 🚀 Guide d'Upload sur GitHub

Ce guide vous accompagne étape par étape pour uploader votre projet YouTube Clip Extractor sur GitHub.

## 📋 Prérequis

- ✅ Compte GitHub créé
- ✅ Git configuré localement (déjà fait)
- ✅ Projet prêt (déjà fait)

## 🔗 Étape 1 : Créer un nouveau repository sur GitHub

1. **Allez sur GitHub.com** et connectez-vous
2. **Cliquez sur le bouton "+"** en haut à droite
3. **Sélectionnez "New repository"**
4. **Remplissez les informations :**
   - **Repository name :** `youtube-clip-extractor`
   - **Description :** `A powerful web application to extract clips from YouTube videos with high quality. Available in both English and French.`
   - **Visibilité :** Public (recommandé)
   - **Cochez "Add a README file"** ❌ (nous avons déjà un README)
   - **Cochez "Add .gitignore"** ❌ (nous avons déjà un .gitignore)
   - **Cochez "Choose a license"** ❌ (nous avons déjà une licence)
5. **Cliquez sur "Create repository"**

## 🔗 Étape 2 : Connecter votre repository local à GitHub

Une fois votre repository créé, GitHub vous donnera des instructions. Voici les commandes à exécuter :

```bash
# Ajouter le remote origin (remplacez YOUR_USERNAME par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/YOUR_USERNAME/youtube-clip-extractor.git

# Renommer la branche principale en 'main' (standard GitHub)
git branch -M main

# Pousser votre code vers GitHub
git push -u origin main
```

## 🔗 Étape 3 : Vérification

1. **Rafraîchissez la page GitHub** de votre repository
2. **Vérifiez que tous vos fichiers sont présents :**
   - ✅ `app_en.py`
   - ✅ `app_fr.py`
   - ✅ `launch.py`
   - ✅ `video_utils.py`
   - ✅ `requirements.txt`
   - ✅ `README.md`
   - ✅ `LICENSE`
   - ✅ `.gitignore`

## 🎯 Étape 4 : Personnalisation (optionnel)

### Ajouter des topics
Dans votre repository GitHub, cliquez sur l'icône ⚙️ à côté d'About, puis ajoutez ces topics :
- `youtube`
- `video-extraction`
- `python`
- `gradio`
- `bilingual`
- `web-application`

### Ajouter une description courte
Dans About, ajoutez :
```
🎞️ Extract high-quality clips from YouTube videos with a bilingual web interface
```

## 🔗 Étape 5 : Partager votre projet

### Badges à ajouter dans votre README
Vous pouvez ajouter ces badges en haut de votre README.md :

```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange.svg)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/YOUR_USERNAME/youtube-clip-extractor)
```

### Liens utiles
- **Repository URL :** `https://github.com/YOUR_USERNAME/youtube-clip-extractor`
- **Clone URL :** `https://github.com/YOUR_USERNAME/youtube-clip-extractor.git`

## 🚀 Étape 6 : Mise à jour future

Pour les futures modifications :

```bash
# Ajouter les changements
git add .

# Commiter les changements
git commit -m "Description de vos changements"

# Pousser vers GitHub
git push
```

## 🎉 Félicitations !

Votre projet YouTube Clip Extractor est maintenant sur GitHub ! 

### Prochaines étapes possibles :
- 🌟 Ajouter des étoiles à votre propre projet
- 📝 Créer des issues pour les améliorations futures
- 🔄 Configurer GitHub Actions pour l'automatisation
- 📦 Publier sur PyPI (optionnel)

---

## ❓ Aide

Si vous rencontrez des problèmes :

1. **Vérifiez que Git est bien configuré :**
   ```bash
   git config --global user.name
   git config --global user.email
   ```

2. **Vérifiez le statut de votre repository :**
   ```bash
   git status
   git remote -v
   ```

3. **Consultez la documentation GitHub :** [Uploading a project to GitHub](https://docs.github.com/en/get-started/start-your-journey/uploading-a-project-to-github)

---

**Votre projet est maintenant prêt à être partagé avec le monde ! 🌍** 